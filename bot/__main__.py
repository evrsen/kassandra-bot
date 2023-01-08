import asyncio
import asyncpg
import aio_pika

from bot.bot import Kassandra
from bot import token, intents, prefix, pg_user, pg_db, pg_pass


async def main():
    async with Kassandra(
        command_prefix=prefix,
        intents=intents,
    ) as bot, asyncpg.create_pool(
        user=pg_user,
        password=pg_pass,
        database=pg_db,
        host="localhost"
    ) as apg_pool, aio_pika.connect_robust(
        "amqp://guest:guest@localhost/",
    ) as rmq_conn:

        @bot.event
        async def on_message(message):
            channel = await rmq_conn.channel()
            await channel.default_exchange.publish(
                aio_pika.Message(body=message.content),
                routing_key="messages"
            )

        @bot.command()
        async def getmsgs(ctx):
            async with apg_pool.acquire() as conn:
                data = await conn.fetch("SELECT message FROM messages")
                await ctx.send(str(data))

        await bot.start(token)

asyncio.run(main())
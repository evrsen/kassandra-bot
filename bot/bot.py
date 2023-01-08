from discord.ext.commands import Bot

class Kassandra(Bot):
    async def setup_hook(self) -> None:
        await self.tree.sync()
FROM fnndsc/python-poetry

WORKDIR /bot
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

CMD ["poetry", "run", "python", "-m", "bot"]
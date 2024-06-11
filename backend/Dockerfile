FROM python:3.8-slim

# Poetryインストール
RUN pip install --upgrade pip && \
    pip install poetry

WORKDIR /src

# Poetry関連ファイルをコピー
COPY pyproject.toml* poetry.lock* ./

RUN apt update && apt upgrade -y && \
    apt install --no-install-recommends -y tzdata && \
    apt install -y python3-dev default-libmysqlclient-dev build-essential && \
    apt install -y pkg-config && \
    apt clean

# poetryでライブラリをインストール (pyproject.tomlが既にある場合)
RUN poetry config virtualenvs.in-project true && \
    poetry config virtualenvs.create true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
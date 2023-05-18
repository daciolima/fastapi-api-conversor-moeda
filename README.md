#### Projeto de Conversor de Moeda Fidunciária desenvolvido em Framework FastAPI
Consumindo de uma API terceira e retornando por um endpoint a conversão da moeda

**Framework e Libs**
    - Poetry
    - FastAPI
    - Pydantic
    - Requests

**Iniciando Poetry** (Gerenciador de pacote e gerenciador de ambiente. Poetry == pip + venv)
Arquivo: pyproject.toml
```shell
# Instalando o poetry
curl -sSL https://install.python-poetry.org | python3 -

# Criando projeto poetry
poetry init
```

**Comandos Docker**
```shell
# Cria container
docker-compose up -d

# Lista os container em UP
docker ps | grep pg

# Stop no referido container conforme ID
docker stop <id> && docker rm <id>
```

**UP Aplicação**
```shell
uvicorn main:app --port 8080 --reload
```

**Export variável de ambiente**
```shell
source .env 
```

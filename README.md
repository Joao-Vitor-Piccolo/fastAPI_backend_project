# FastAPI User Auth

Backend para sistema de cadastro, login e gerenciamento de usuários, com frontend estático integrado.

## Estrutura do Projeto

```
fastAPI_course/
│
├── .env                          # Variáveis de ambiente (DB, configs)
├── README.md                     # Este arquivo
│
├── src/
│   ├── fastapi_course/
│   │   ├── __init__.py
│   │   ├── app.py                # FastAPI app principal
│   │   ├── database.py           # Configuração do SQLAlchemy
│   │   ├── models.py             # Modelos ORM
│   │   ├── schemas.py            # Schemas Pydantic
│   │   ├── settings.py           # Configurações (env)
│   │   └── ...
│   │
│   └── static_files/
│       ├── index.html
│       ├── pages/
│       │   ├── cadastro.html
│       │   └── pos_login.html
│       └── src/
│           ├── css/
│           │   ├── styles.css
│           │   ├── cadastro.css
│           │   └── post_login.css
│           └── js/
│               ├── script.js
│               └── script_post_login.js
│
├── migrations/                   # Migrations Alembic
├── tests/                        # Testes automatizados
│   ├── conftest.py
│   ├── test_app.py
│   └── test_db.py
└── pyproject.toml
```

## Principais Funcionalidades

- **API RESTful** com FastAPI para cadastro, login, atualização e remoção de usuários.
- **Banco de dados** via SQLAlchemy (PostgreSQL, configurável via .env).
- **Frontend estático** com HTML, CSS e JS para login, cadastro e pós-login.
- **Migrations** com Alembic.
- **Testes automatizados** com Pytest.

## Como rodar o projeto

1. **Clone o repositório**
    ```sh
    git clone https://github.com/seu-usuario/fastAPI_course.git
    cd fastAPI_course
    ```

2. **Configure o ambiente**
    - Crie e edite o arquivo .env na raiz do projeto:
      ```
      DATABASE_URL=postgresql://usuario:senha@localhost:5432/seubanco
      ```

3. **Instale as dependências**
    ```sh
    poetry install
    # ou
    pip install -r requirements.txt
    ```

4. **Rode as migrations**
    ```sh
    alembic upgrade head
    ```

5. **Inicie a API**
    ```sh
    poetry run fastapi dev app.py --port 8000
    # ou
    uvicorn src.fastapi_course.app:app --reload
    ```

6. **Acesse o frontend**
    - [http://localhost:8000/static/index.html](http://localhost:8000/static/index.html)

## Comandos `taskipy` (se configurado no pyproject.toml)

```toml
[tool.taskipy.tasks]
run = 'fastapi dev app.py --port 8000'
test = 'pytest --cov=src/fastapi_course -vv'
post_test = 'coverage html'
```

## Testes

Execute os testes com:
```sh
pytest
```

## Observações

- O caminho do banco de dados no `.env` deve ser ajustado conforme seu ambiente.
- O frontend estático está em `src/static_files/`.
- As migrations são gerenciadas pelo Alembic.
- O projeto é modular e fácil de expandir.

---

## Licença

MIT

---

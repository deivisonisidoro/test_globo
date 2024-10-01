# Teste Técnico da Globo - Backend FastAPI

Este projeto é um backend desenvolvido em FastAPI que permite inserir, armazenar, listar, recuperar e deletar URLs do YouTube. A aplicação foi criada como parte de um teste técnico para a Globo.

## Arquitetura Limpa

Foquei em construir uma **arquitetura limpa** para esta aplicação, seguindo os princípios de separação de preocupações e modularidade. A arquitetura limpa traz os seguintes benefícios:

- **Manutenibilidade**: A estrutura organizada do código facilita a identificação e correção de problemas, permitindo que desenvolvedores trabalhem de forma mais eficiente.
- **Testabilidade**: Com a separação de responsabilidades, cada componente da aplicação pode ser testado de forma isolada, aumentando a cobertura de testes e a confiabilidade do software.
- **Escalabilidade**: Uma arquitetura bem projetada permite que a aplicação cresça facilmente. Novas funcionalidades podem ser adicionadas sem impactar outras partes do sistema.
- **Flexibilidade**: Alterações em um componente têm pouco ou nenhum impacto em outros, permitindo adaptações rápidas às necessidades do negócio.

## Funcionalidades

A aplicação oferece as seguintes funcionalidades:

- **Inserir e armazenar uma URL do YouTube**: Você pode adicionar novas URLs do YouTube ao banco de dados.
- **Listar as URLs salvas**: A aplicação pode retornar todas as URLs armazenadas.
- **Recuperar a URL e tocar através da solução**: É possível recuperar uma URL específica e reproduzi-la.
- **Deletar a URL**: Você pode remover uma URL do banco de dados.

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/): Framework web para construir APIs rápidas e de alto desempenho.
- [SQLAlchemy](https://www.sqlalchemy.org/): ORM para interagir com o banco de dados.
- [PostgreSQL](https://www.postgresql.org/): Sistema de gerenciamento de banco de dados.
- [Alembic](https://alebic.sqlalchemy.org/): Ferramenta de migração para bancos de dados SQL.
- [Poetry](https://python-poetry.org/): Gerenciador de dependências e empacotador para Python.
- [pytest](https://pytest.org/): Framework de testes para Python.

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado em sua máquina:

- [Poetry](https://python-poetry.org/docs/#installation)
- **PostgreSQL**: A aplicação requer um banco de dados PostgreSQL, que pode ser instalado localmente ou executado via Docker.

### Executando PostgreSQL via Docker

Se você preferir usar o Docker, pode executar o seguinte comando para iniciar um contêiner do PostgreSQL:

```bash
docker run --name postgres_db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres:14
```

## Rodando Localmente

1. **Instalar Dependências com Poetry:**

   ```bash
   poetry install
   ```

2. **Executar a Aplicação:**

   ```bash
   poetry run uvicorn src/presentation/main.py --host 0.0.0.0 --port 8000 --reload
   ```

## Swagger e Redoc

A aplicação inclui uma interface do Swagger para visualizar e testar as rotas da API. Acesse [http://localhost:8000/docs](http://localhost:8000/docs) para interagir com a API.

Além disso, você pode acessar a documentação Redoc da API em [http://localhost:8000/redoc](http://localhost:8000/redoc) para uma visualização mais detalhada.

## Testes

A aplicação possui testes unitários, de integração e e2e. Cada conjunto de testes está separado em suas respectivas pastas. Para facilitar a execução, utilizei `pytest` e adicionei markers que permitem executar os testes separadamente. No entanto, você também pode executar todos os testes de uma vez, caso deseje.

### Exemplos de Markers

Os seguintes markers estão disponíveis para execução dos testes:

- `unit`: Para testes unitários.
- `integration`: Para testes de integração.
- `e2e`: Para testes de ponta a ponta (end-to-end).

### Executando os Testes

Para rodar todos os testes, use o comando:

```bash
pytest
```

Para executar testes específicos, utilize os markers definidos nas pastas de testes. Por exemplo:

```bash
pytest -m "unit"
```

## Documentação com MkDocs

A documentação deste projeto foi gerada usando o MkDocs com o tema Material. Ela permite visualizar todas as informações detalhadas sobre o código e a arquitetura da aplicação.

### Visualizando a Documentação Publicada

Você pode acessar a documentação completa e publicada deste projeto através do link:

**[Documentação MkDocs](https://deivisonisidoro.github.io/test_globo/)**

### Visualizando a Documentação Localmente

1. **Inicie o Servidor de Desenvolvimento**: Execute o seguinte comando na pasta do seu projeto:

   ```bash
   mkdocs serve
   ```

Após isso, a documentação estará disponível no GitHub Pages.
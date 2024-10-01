# Teste Globo

Este é um monorepo que contém dois projetos: um backend em FastAPI e um frontend em Next.js. O objetivo deste repositório é fornecer uma solução completa para inserção, armazenamento, recuperação e deleção de URLs do YouTube.

## Clonando o Projeto

Para clonar este projeto, utilize o seguinte comando:

```bash
git clone https://github.com/deivisonisidoro/test_globo.git
```

## Rodando com Docker Compose

Para executar o projeto utilizando Docker Compose, siga os passos abaixo:

1. **Navegue até o diretório do projeto**:

   ```bash
   cd test_globo
   ```

2. **Execute o Docker Compose**:

   ```bash
   docker-compose up
   ```

   O comando acima irá construir e iniciar todos os serviços definidos no arquivo `docker-compose.yml`, incluindo o Nginx. Os serviços serão executados em contêineres Docker, e você poderá acessar o backend e o frontend conforme configurado nas portas especificadas.

### Acessando a Aplicação

- **Frontend**: A aplicação frontend estará disponível em [http://localhost:8081](http://localhost:8081).
- **Backend**: A API do backend estará disponível em [http://localhost:8080](http://localhost:8080).
- **Nginx**: O Nginx, que serve como um proxy reverso, estará disponível em [http://localhost:3050](http://localhost:3050).

## Publicação

Caso você deseje publicar a aplicação frontend, será necessário substituir o `Dockerfile` padrão pelo `Dockerfile.deploy` localizado na pasta do frontend. Este arquivo está configurado para otimizar a construção da aplicação para produção.

## Documentação Adicional

Para mais detalhes sobre cada projeto, consulte os READMEs individuais:

- **[Backend (FastAPI)](backend/README.md)**: Instruções e informações sobre o projeto backend.
- **[Frontend (Next.js)](frontend/README.md)**: Instruções e informações sobre o projeto frontend.


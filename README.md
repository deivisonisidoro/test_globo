# Teste Globo

Este é um monorepo que contém dois projetos: um backend em FastAPI e um frontend em Next.js. O objetivo deste repositório é fornecer uma solução completa para inserção, armazenamento, recuperação e deleção de URLs do YouTube.

## Notas de Versão

Para visualizar as notas de versão detalhadas, incluindo funcionalidades, bugs, observações e pontos de melhoria, acesse [Release Notes](release_notes.md).

## Documentação Adicional

Para mais detalhes sobre cada projeto, consulte os READMEs individuais:

- **[Backend (FastAPI)](backend/README.md)**: Instruções e informações sobre o projeto backend.
- **[Frontend (Next.js)](frontend/README.md)**: Instruções e informações sobre o projeto frontend.

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

- **Frontend**: A aplicação frontend estará disponível em [http://localhost:3000](http://localhost:3000).
- **Backend**: A API do backend estará disponível em [http://localhost:8080](http://localhost:8080).
- **Nginx**: O Nginx, que serve como um proxy reverso, estará disponível em [http://localhost:3050](http://localhost:3050).

## Publicação

Para publicar a aplicação, utilize o Docker Compose para construir e implantar os serviços de forma simplificada. Siga as instruções abaixo:

### Construção e Publicação com Docker Compose

1. **Construir as Imagens Docker**:

   Para construir todas as imagens definidas no arquivo `docker-compose.yml`, execute o seguinte comando:

   ```bash
   docker-compose build
   ```

2. **Publicar as Imagens no Docker Hub**:

   Após a construção das imagens, você pode publicá-las no Docker Hub usando:

   ```bash
   docker-compose push
   ```

   **Observação**: Certifique-se de que suas imagens estão configuradas corretamente no `docker-compose.yml` com os nomes apropriados para o Docker Hub.

3. **Implantar no Kubernetes**:

   Se você já tiver configurado seu cluster Kubernetes, aplique as configurações contidas na pasta `k8s` com o seguinte comando:

   ```bash
   kubectl apply -f k8s
   ```

   **Nota**: Para implantar em um cluster Kubernetes, você pode usar serviços como Google Kubernetes Engine (GKE), Amazon EKS, ou configurar um cluster local com Minikube ou Kind. Consulte a [documentação do Kubernetes](https://kubernetes.io/docs/setup/) para mais informações sobre como criar e configurar um cluster.

### Acesso à Aplicação

Após a implantação, você poderá acessar sua aplicação nos seguintes endereços:

- **Frontend**: [http://localhost:3000](http://localhost:3000)
- **Backend**: [http://localhost:8080](http://localhost:8080)
- **Nginx**: [http://localhost:80](http://localhost:80)

## Configurações do Kubernetes

Uma pasta chamada `k8s` foi adicionada ao projeto, contendo os arquivos de configuração do Kubernetes. Esses arquivos são usados para implantar e gerenciar a aplicação no cluster Kubernetes.

### Estrutura da Pasta k8s

- **configmap.yaml**: Configuração para variáveis de ambiente e configurações do aplicativo.
- **db-deployment.yaml**: Configuração para o deployment do banco de dados.
- **fastapi-deployment.yaml**: Configuração para o deployment do backend (FastAPI).
- **ingress-service.yml**: Configuração para expor os serviços através do Ingress.
- **nextjs-deployment.yaml**: Configuração para o deployment do frontend (Next.js).

## Workflows

Foram criados workflows para automatizar o processo de integração contínua (CI) dos projetos de frontend e backend. Esses workflows estão configurados para rodar testes e outras ações em cada push ou pull request.

### Estrutura dos Workflows

- **Frontend**: O workflow do frontend está localizado em `frontend/.github/workflows/deploy-to-eks.yml`.
- **Backend**: Os workflows do backend estão localizados em:
  - `backend/.github/workflows/deploy-to-eks.yml`
  - `backend/.github/workflows/python-tests.yml`
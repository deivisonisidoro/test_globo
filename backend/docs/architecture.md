# Arquitetura do Projeto

Este projeto segue os princípios da **Arquitetura Limpa** (Clean Architecture), com o objetivo de garantir uma organização modular e separação clara de responsabilidades. A arquitetura está dividida em quatro camadas principais: **Application**, **Domain**, **Infrastructure** e **Presentation**.

## Camadas da Arquitetura

### 1. Application

A camada **Application** é responsável por orquestrar a lógica da aplicação, conectando a camada de apresentação à lógica de negócio. Aqui estão os casos de uso (use cases) que implementam as regras de negócio e controlam o fluxo dos dados.

### 2. Domain

A camada **Domain** contém as regras de negócio puras e as entidades centrais do sistema. Esta camada é independente das demais e tem como objetivo manter a lógica essencial do negócio.

### 3. Infrastructure

A camada **Infrastructure** lida com as implementações concretas, como repositórios de dados, serviços externos e comunicação com o banco de dados.

### 4. Presentation

A camada **Presentation** é responsável pela interação com o usuário final, lidando com as requisições e respostas HTTP. Neste projeto, utilizamos o **FastAPI** para definir as rotas e os endpoints da API.

Exemplos de funcionalidades da camada de apresentação incluem:

- **Rotas (routers)**: São responsáveis por mapear as URLs para os controladores correspondentes. Cada rota define um endpoint da API.
- **Schemas**: Especificam a estrutura dos dados que serão recebidos e enviados pelas rotas, garantindo validações apropriadas.

Essa camada cuida da interação entre o usuário e a aplicação, garantindo que as informações fluam de maneira eficiente e com segurança.

## Benefícios da Arquitetura

Ao organizar o sistema em camadas, ganhamos os seguintes benefícios:

- **Manutenibilidade**: As camadas são independentes, facilitando a manutenção e evolução do sistema.
- **Escalabilidade**: O projeto pode ser facilmente expandido, com novas funcionalidades adicionadas sem impactar o funcionamento existente.
- **Testabilidade**: A separação de responsabilidades torna cada camada isolada, facilitando a criação de testes unitários e de integração.

---

Essa arquitetura modular facilita o desenvolvimento de um sistema escalável, flexível e preparado para crescer à medida que novas demandas surgirem.

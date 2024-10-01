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

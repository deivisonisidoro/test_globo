# Teste Técnico da Globo - Frontend Next.js

Este projeto é um frontend desenvolvido em **Next.js** que permite inserir, armazenar, listar, recuperar e deletar URLs do YouTube. A aplicação foi criada como parte de um teste técnico para a Globo.

## Funcionalidades

A aplicação oferece as seguintes funcionalidades:

- **Inserir e armazenar uma URL do YouTube**: Permite que os usuários adicionem novas URLs do YouTube ao sistema.
- **Listar as URLs salvas**: Mostra uma lista de todas as URLs armazenadas no backend.
- **Recuperar a URL e tocar através da solução**: Os usuários podem reproduzir URLs específicas diretamente pela aplicação.
- **Deletar a URL**: Possibilita a remoção de URLs indesejadas do sistema.

## Tecnologias Utilizadas

- [Next.js](https://nextjs.org/): Framework React para construção de interfaces web rápidas e escaláveis.
- [Tailwind CSS](https://tailwindcss.com/): Framework CSS para estilização utilitária.
- [shadcn](https://ui.shadcn.com/): Biblioteca de componentes para construção de interfaces modernas e responsivas.
- [Lucide](https://lucide.dev/): Conjunto de ícones que podem ser facilmente integrados à interface.
- [React Hook Form](https://react-hook-form.com/): Biblioteca para gerenciar formulários de maneira simples e eficiente.
- [Zod](https://zod.dev/): Biblioteca para validação de esquemas e tipos de dados, facilitando a validação de entrada no frontend.

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado em sua máquina:

- **Node.js**: Certifique-se de ter o Node.js instalado. Você pode baixar a versão mais recente [aqui](https://nodejs.org/).
- **pnpm**: Você pode instalar o pnpm globalmente com o seguinte comando:

   ```bash
   npm install -g pnpm
   ```

## Rodando Localmente

1. **Instalar Dependências:**

   Execute o seguinte comando na raiz do projeto para instalar todas as dependências necessárias:

   ```bash
   pnpm install
   ```

2. **Executar a Aplicação:**

   Após instalar as dependências, você pode iniciar a aplicação localmente com o comando:

   ```bash
   pnpm dev
   ```

   A aplicação estará disponível em [http://localhost:3000](http://localhost:3000).

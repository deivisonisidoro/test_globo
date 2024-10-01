FROM node:22-alpine

RUN npm install -g pnpm

WORKDIR /app

COPY pnpm-lock.yaml ./ 
COPY package.json ./

RUN pnpm install

COPY . .

RUN pnpm build

EXPOSE 3000

CMD ["pnpm", "start"]

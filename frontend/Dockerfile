FROM node:22-alpine

RUN apk add --no-cache curl

RUN npm install -g pnpm

WORKDIR /app

COPY pnpm-lock.yaml ./ 
COPY package.json ./

ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=http://localhost:8080/api

RUN pnpm install

COPY . .

RUN pnpm build

EXPOSE 3000

CMD ["pnpm", "start"]

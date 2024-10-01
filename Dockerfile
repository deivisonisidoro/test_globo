# Use Node.js official image as the base
FROM node:22-alpine

# Install pnpm globally
RUN npm install -g pnpm

# Set working directory inside the container
WORKDIR /app

# Copy only the pnpm-lock.yaml and package.json first for better caching
COPY pnpm-lock.yaml ./
COPY package.json ./

# Install dependencies using pnpm
RUN pnpm install

# Copy the rest of the application files to the container
COPY . .

# Build the Next.js application
RUN pnpm build

# Expose port 8081
EXPOSE 8081

# Start the Next.js application
CMD ["pnpm", "start"]

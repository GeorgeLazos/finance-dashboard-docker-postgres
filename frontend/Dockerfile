#First stage: use node.js 18 as base image 
FROM node:18 AS builder

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the rest of the source files and build the app
COPY . .
RUN npm run build

# Second stage: use nginx as base image
FROM nginx:alpine

# Copy folder from stage 1 to nginx html directory
COPY --from=builder /app/dist /usr/share/nginx/html

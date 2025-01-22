FROM node:19-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm install @react-pdf/renderer
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
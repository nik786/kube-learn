FROM node:20-alpine

WORKDIR /app

ENV NPM_CONFIG_FUND=false
ENV NPM_CONFIG_AUDIT=false

COPY package.json package-lock.json* ./


RUN npm install

RUN npm install lucide-react react-markdown framer-motion



COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]


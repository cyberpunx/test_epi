# etapa de compilación
FROM node:14.17.3-alpine as build-stage
WORKDIR /code
COPY package*.json ./
RUN npm install
COPY . /code/.
RUN npm run build

# etapa de producción
FROM nginx:1.13.12-alpine as production-stage
COPY --from=build-stage /code/dist /usr/share/nginx/html
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
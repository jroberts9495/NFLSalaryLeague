# Stage 1: Build
FROM node:20-alpine AS build
WORKDIR /app

# Copy configuration files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application (output goes to /app/dist/<project-name>)
RUN npm run build --configuration=production

# Stage 2: Serve
FROM nginx:alpine

# Copy the build output from the build stage to Nginx's html folder
# Note: Replace 'my-angular-app' with your project name from angular.json
COPY --from=build /app/dist/my-angular-app/browser /usr/share/nginx/html

# Copy a custom nginx config if you have one (optional but recommended for SPAs)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
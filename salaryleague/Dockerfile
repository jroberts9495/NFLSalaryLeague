# Use the official Node image
FROM node:20-slim

# Set working directory
WORKDIR /app

# Install Angular CLI globally
RUN npm install -g @angular/cli

# Copy package files first for better caching
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the default Angular port
EXPOSE 4200

# Run ng serve
# --host 0.0.0.0 is MANDATORY to allow connections from outside the container
# --poll 2000 ensures changes are detected on some file systems (like Windows/Docker)
CMD ["ng", "serve", "--host", "0.0.0.0", "--poll", "2000"]
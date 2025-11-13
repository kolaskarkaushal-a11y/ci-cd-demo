# Use an official Node.js 18 image (based on Alpine Linux — lightweight)
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy only the package files first (for better caching)
COPY package*.json ./

# Install dependencies inside the container
RUN npm install

# Copy the rest of the application files
COPY . .

# Expose port 3000 (the port your app listens on)
EXPOSE 3000

# Start the app
CMD ["node", "server.js"]

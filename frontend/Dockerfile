# Use the official Node.js image as the base image
FROM node:20.9.0-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json files to the working directory
COPY package.json .
COPY ./package-lock.json .

# Install npm dependencies based on the package.json
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 3000

CMD ["npm", "run", "start:watch"]

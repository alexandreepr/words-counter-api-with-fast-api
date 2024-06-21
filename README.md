# Words Counter

This project is a solution to the Voxy code challenge using ReactJS and FastAPI.

## Requirements

- Docker
- docker-compose

## Installation

1. **Clone the project:**

   ```bash
   git clone https://github.com/alexandreepr/voxy-code-challenge.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd voxy-code-challenge
   ```

3. **Build and start the containers:**

   ```bash
   docker-compose up --build
   ```

4. **Access the application:**

   Open your web browser and go to [http://localhost](http://localhost)

## Run Backend Tests

1. **Access the container:**

   ```bash
   docker exec -it <container_id> bash
   ```

2. **Run the tests:**

   ```bash
   pytest
   ```

## Run Frontend Tests

1. **Access the container:**

   ```bash
   docker exec -it <container_id> sh
   ```

2. **Run the tests:**

   ```bash
   npm run test
   ```

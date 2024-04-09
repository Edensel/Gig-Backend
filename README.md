# Backend API Project README

This project is a Flask-based backend API for managing orders and user authentication. It provides endpoints for user registration, login, order creation, retrieval, updating, and deletion.

## Setup

1. **Clone the repository**: Clone this repository to your local machine.

2. **Install dependencies**: Install the required Python packages using pip.

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**: The project uses SQLite as the database. Run the following command to create the initial database file.

   ```bash
   python create_db.py
   ```

4. **Set up environment variables**: Create a `.env` file in the project directory and set the following environment variables:

   ```
   SECRET_KEY=your_secret_key_here
   ```

   Replace `your_secret_key_here` with a random secret key. This key is used for securely signing session cookies and should be kept secret.

## Usage

- **Running the server**: Start the Flask server by running the following command:

  ```bash
  python app.py
  ```

- **API Endpoints**:
  - `POST /register`: Register a new user.
  - `POST /login`: Log in with existing user credentials.
  - `POST /order`: Create a new order (requires authentication).
  - `GET /order`: Retrieve all orders (requires authentication).
  - `GET /order/<id>`: Retrieve a specific order by ID (requires authentication).
  - `PUT /order/<id>`: Update a specific order by ID (requires authentication).
  - `DELETE /order/<id>`: Delete a specific order by ID (requires authentication).

## Authentication

- User authentication is implemented using JWT (JSON Web Tokens). After a successful login, the server returns an access token, which should be included in the Authorization header of subsequent requests to authenticated endpoints.

## Error Handling

- The server provides error handlers for common HTTP errors (404, 400, 500) to return informative error messages.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
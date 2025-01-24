# Security Asset Dashboard Backend

FastAPI backend for the Security Asset Dashboard application. This backend provides API endpoints for managing security assets and their vulnerabilities.

## Features

- CRUD operations for security assets
- Vulnerability management
- Search, filter, and sort functionality
- MySQL database integration
- Docker support

## Tech Stack

- FastAPI
- SQLAlchemy
- MySQL
- Docker
- Pydantic

## Getting Started

### Using Docker

1. Make sure you have Docker and Docker Compose installed
2. Run the following command:
   ```bash
   docker-compose up --build
   ```
3. The API will be available at `http://localhost:8000`
4. API documentation will be available at `http://localhost:8000/docs`

### Manual Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in `.env` file:
   ```
   MYSQL_USER=your_user
   MYSQL_PASSWORD=your_password
   MYSQL_HOST=localhost
   MYSQL_PORT=3306
   MYSQL_DATABASE=security_assets
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

- `GET /api/v1/assets/`: List all assets
- `POST /api/v1/assets/`: Create a new asset
- `GET /api/v1/assets/{asset_id}`: Get asset details
- `PUT /api/v1/assets/{asset_id}`: Update an asset
- `DELETE /api/v1/assets/{asset_id}`: Delete an asset
- `GET /api/v1/assets/{asset_id}/vulnerabilities/`: List vulnerabilities for an asset
- `POST /api/v1/assets/{asset_id}/vulnerabilities/`: Add vulnerability to an asset

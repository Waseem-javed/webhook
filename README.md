# Meesaw Webhook Service

A modular FastAPI application for receiving, validating, and storing webhook events.

## Features

- **Signature Verification**: Securely validates incoming webhooks using a shared secret.
- **Duplicate Detection**: Prevents processing the same event multiple times using `event_id`.
- **Modular Architecture**: Organized following best practices for scalability and maintainability.
- **Automated Documentation**: Interactive Swagger UI with detailed models and schema validation.

## Project Structure

```text
app/
├── api/                # API routes and endpoints
│   ├── v1/             # Versioned API
│   │   ├── endpoints/  # Specific endpoint logic
│   │   └── api.py      # Router aggregator
│   └── deps.py         # Dependencies (e.g., database session)
├── core/               # Configuration and security settings
├── db/                 # Database initialization and session management
├── models/             # SQLAlchemy database models
├── schemas/            # Pydantic data validation schemas
└── main.py             # Application entry point
```

## Getting Started

### Prerequisites

- Python 3.8+
- SQLite (default) or PostgreSQL

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd lennert
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables (create a `.env` file):
   ```env
   SHARED_SECRET=your_secret_here
   ```

### Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The service will be available at `http://localhost:8000`.

## API Documentation

The interactive API documentation (Swagger UI) is automatically generated and can be accessed at:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

The root URL (`/`) also automatically redirects to the Swagger documentation for convenience.

## Usage

### Receive a Webhook

**Endpoint**: `POST /webhooks/webhook`

**Headers**:
- `x-signature`: Must match the `SHARED_SECRET` in your configuration.

**Payload**:
```json
{
  "event_id": "unique-event-123",
  "data": { ... }
}
```

### View All Webhooks

**Endpoint**: `GET /webhooks/all`

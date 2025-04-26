# FastAPI Agent Creation API

This project provides a FastAPI backend with a `/create-agent` endpoint that allows users to create agents using either the VAPI or Retell provider. The endpoint maps user-provided parameters to the appropriate provider's API format and makes an HTTP POST request to create the agent.



## Running the Application
Start the FastAPI application using Uvicorn:
```bash
uvicorn main:app --reload
```
The application will be available at `http://127.0.0.1:8000`.

## API Documentation
FastAPI automatically generates interactive API documentation. You can access it at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoint
### POST `/create-agent`
#### Request Body
- **For VAPI**:
  ```json
  {
    "name": "Test Agent",
    "language": "en",
    "provider": "vapi"
  }
  ```

- **For Retell**:
  ```json
  {
    "name": "Test Agent",
    "description": "This is a test agent for demonstration purposes.",
    "language": "en",
    "phone_number": "+1234567890",
    "provider": "retell"
  }
  ```

#### Response
- **Success**:
  ```json
  {
    "status": "success",
    "data": { ... }
  }
  ```
- **Error**:
  ```json
  {
    "detail": "Error message"
  }
  ```

## Configuration
Update the `CONFIG` dictionary in `main.py` with your API keys:
```python
CONFIG = {
    "vapi": {
        "url": "https://api.vapi.ai/assistant",
        "api_key": "your_vapi_api_key_here"
    },
    "retell": {
        "url": "https://api.retellai.com/agents/create",
        "api_key": "your_retell_api_key_here"
    }
}
```


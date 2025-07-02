# API Server Guide

This guide explains how to start and use the FastAPI server for the hed-task project.

## 🚀 **What `uv run uvicorn hed_task.api:app --reload` Does**

This command starts a **development web server** for your FastAPI application:

- **`uv run`** - Runs the command in your project's virtual environment
- **`uvicorn`** - A fast ASGI server (like a web server for Python)
- **`hed_task.api:app`** - Points to the `app` object in your `src/hed_task/api.py` file
- **`--reload`** - Automatically restarts the server when you change code files

## 🌐 **How to Use the API Server**

### 1. **Start the Server**
```bash
uv run uvicorn hed_task.api:app --reload
```

You'll see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using WatchFiles
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
```

### 2. **Access the API**

Once running, you can access these endpoints:

| URL | Purpose |
|-----|---------|
| `http://localhost:8000/` | Welcome message |
| `http://localhost:8000/health` | Health check |
| `http://localhost:8000/version` | Version info |
| `http://localhost:8000/docs` | **Interactive API documentation** |
| `http://localhost:8000/redoc` | Alternative documentation |

### 3. **Interactive Documentation**

The most useful feature is **`http://localhost:8000/docs`** - this gives you:
- ✨ **Interactive API explorer** - test endpoints directly in your browser
- 📋 **Automatic documentation** - generated from your code
- 🧪 **Built-in testing** - send real requests and see responses

### 4. **Testing the API**

#### Using curl (Command Line)
```bash
# Test the welcome endpoint
curl http://localhost:8000/

# Test health check
curl http://localhost:8000/health

# Test version info
curl http://localhost:8000/version
```

#### Using Python requests
```python
import requests

# Test the API
response = requests.get("http://localhost:8000/")
print(response.json())  # {"message": "Welcome to HED Task API"}

# Health check
health = requests.get("http://localhost:8000/health")
print(health.json())  # {"status": "healthy"}
```

#### Using the Interactive Docs
1. Start the server: `uv run uvicorn hed_task.api:app --reload`
2. Open your browser to: `http://localhost:8000/docs`
3. Click on any endpoint to expand it
4. Click "Try it out" to test the endpoint
5. Click "Execute" to send the request and see the response

## 🛠️ **Development Tips**

### Auto-Reload Feature
The `--reload` flag means:
- ✅ **Automatic restarts** when you save changes to Python files
- ✅ **No need to manually restart** during development
- ⚠️ **Development only** - don't use `--reload` in production

### Adding New Endpoints
To add new API endpoints:

1. Edit `src/hed_task/api.py`
2. Add new route functions:
```python
@app.get("/my-endpoint")
async def my_function():
    return {"message": "Hello from new endpoint"}
```
3. Save the file - server automatically reloads
4. Visit `http://localhost:8000/docs` to see your new endpoint

### Configuration
The server uses settings from `src/hed_task/config.py`:
- **Host**: `0.0.0.0` (accessible from other machines)
- **Port**: `8000` (default)
- **Log level**: `INFO`

You can override these with environment variables or by editing the config file.

## 🚀 **Alternative Start Methods**

### Using the Startup Script
```bash
uv run python scripts/start_api.py
```

### Using Make
```bash
make api
```

### Using Docker
```bash
docker-compose up
```

## 🔍 **Troubleshooting**

### Port Already in Use
If you see "Address already in use" error:
```bash
# Use a different port
uv run uvicorn hed_task.api:app --reload --port 8001
```

### Module Not Found
If you see import errors:
```bash
# Make sure you're in the project directory
cd h:\Repos\hed-task

# Reinstall in development mode
uv sync --all-extras
```

### API Not Accessible
- Check the server is running: look for "Uvicorn running on..." message
- Verify the URL: `http://localhost:8000` or `http://127.0.0.1:8000`
- Check firewall settings if accessing from another machine

## 📚 **Next Steps**

Now that you understand how to run the API server, you can:

1. **Explore the interactive docs** at `/docs`
2. **Add your own endpoints** for HED task analysis
3. **Test your API** using the built-in tools
4. **Integrate with your CLI** for a complete application

Happy coding! 🎉
import sys
import os

# Add the current directory to sys.path so 'main' can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from main import app
except Exception as e:
    import traceback
    print("CRITICAL: Failed to import 'app' from 'main.py'")
    traceback.print_exc()
    # On Vercel, this will show up in the Logs.
    # To make it visible in the browser (for debugging only):
    from fastapi import FastAPI
    app = FastAPI()
    @app.get("/")
    async def error_page():
        return {"error": str(e), "traceback": traceback.format_exc()}

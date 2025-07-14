# run_server.py
import uvicorn
import sys
import os

# Add userandorder/ to PYTHONPATH explicitly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "userandorder")))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # No more userandorder.main — we injected the path manually
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_dirs=["userandorder"]
    )

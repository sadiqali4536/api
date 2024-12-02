from fastapi import FastAPI
import os
import logging

# Create FastAPI instance
app = FastAPI()

# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)

# In-memory data store for workers
workers = {
    "1": {
        "name": "John Doe",
        "position": "Manager",
        "salary": 5000
    },
    "2": {
        "name": "John Smith",
        "position": "General Manager",
        "salary": 40000
    }
}

@app.get("/")
def read_root():
    return {"message": "Hello, Render!"}

@app.get("/workers")
def get_all_workers():
    logging.debug("Fetching all workers.")
    return {"workers": workers}

@app.get("/workers/{worker_id}")
def get_worker(worker_id: str):
    if worker_id in workers:
        logging.debug(f"Fetching worker with ID: {worker_id}")
        return {"worker": workers[worker_id]}
    logging.warning(f"Worker with ID {worker_id} not found.")
    return {"message": "Worker not found"}, 404

@app.post("/workers")
def add_worker(worker_id: str, name: str, position: str, salary: int = 0):
    if worker_id in workers:
        logging.warning(f"Worker ID {worker_id} already exists.")
        return {"message": "Worker ID already exists"}, 400

    workers[worker_id] = {
        "name": name,
        "position": position,
        "salary": salary,
    }
    logging.info(f"Worker with ID {worker_id} added successfully.")
    return {"message": "Worker added", "worker": workers[worker_id]}

@app.put("/workers/{worker_id}")
def update_worker(worker_id: str, name: str, position: str, salary: int = 0):
    if worker_id not in workers:
        return {"message": "Worker not found"}, 404

    workers[worker_id] = {
        "name": name,
        "position": position,
        "salary": salary,
    }
    logging.info(f"Worker with ID {worker_id} updated successfully.")
    return {"message": "Worker updated", "worker": workers[worker_id]}

@app.delete("/workers/{worker_id}")
def delete_worker(worker_id: str):
    if worker_id in workers:
        del workers[worker_id]
        logging.info(f"Worker with ID {worker_id} deleted.")
        return {"message": "Worker deleted"}
    logging.warning(f"Worker with ID {worker_id} not found for deletion.")
    return {"message": "Worker not found"}, 404

@app.get("/test")
def test():
    logging.debug("Test route accessed.")
    return {"message": "API is working!"}

if __name__ == "__main__":
    # Get the port from the environment variable or default to 8000
    port = int(os.environ.get("PORT", 8000))
    # Run the app on 0.0.0.0 to allow external access
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)

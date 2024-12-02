


# from flask import Flask, request, jsonify
# from flask_restful import Resource, Api
# import logging

# # Initialize Flask application
# app = Flask(__name__)
# api = Api(app)

# # Enable logging for debugging
# logging.basicConfig(level=logging.DEBUG)

# # In-memory data store for workers
# workers = {
#     "1": {
#         "name": "John Doe",
#         "position": "Manager",
#         "salary": 5000
#     },
#     "2": {
#         "name": "John Smith",
#         "position": "General Manager",
#         "salary": 40000
#     }
# }

# # Resource for a single worker
# class Worker(Resource):
#     def get(self, worker_id):
#         """
#         Get details of a specific worker by their ID.
#         """
#         if worker_id in workers:
#             logging.debug(f"Fetching worker with ID: {worker_id}")
#             return jsonify({"worker": workers[worker_id]})
#         logging.warning(f"Worker with ID {worker_id} not found.")
#         return jsonify({"message": "Worker not found"}), 404

#     def put(self, worker_id):
#         """
#         Update details of a specific worker.
#         """
#         data = request.get_json()
#         logging.debug(f"PUT data received for worker ID {worker_id}: {data}")
#         if not data or 'name' not in data or 'position' not in data:
#             return jsonify({"message": "Invalid data. 'name' and 'position' are required."}), 400

#         workers[worker_id] = {
#             "name": data["name"],
#             "position": data["position"],
#             "salary": data.get("salary", 0),  # Default salary to 0 if not provided
#         }
#         logging.info(f"Worker with ID {worker_id} updated successfully.")
#         return jsonify({"message": "Worker updated", "worker": workers[worker_id]})

#     def delete(self, worker_id):
#         """
#         Delete a worker by their ID.
#         """
#         if worker_id in workers:
#             del workers[worker_id]
#             logging.info(f"Worker with ID {worker_id} deleted.")
#             return jsonify({"message": "Worker deleted"})
#         logging.warning(f"Worker with ID {worker_id} not found for deletion.")
#         return jsonify({"message": "Worker not found"}), 404


# # Resource for all workers
# class WorkerList(Resource):
#     def get(self):
#         """
#         Get a list of all workers.
#         """
#         logging.debug("Fetching all workers.")
#         return jsonify({"workers": workers})

#     def post(self):
#         """
#         Add a new worker.
#         """
#         data = request.get_json()
#         logging.debug(f"POST data received: {data}")
#         if not data or 'id' not in data or 'name' not in data or 'position' not in data:
#             return jsonify({"message": "Invalid data. 'id', 'name', and 'position' are required."}), 400

#         worker_id = data["id"]
#         if worker_id in workers:
#             logging.warning(f"Worker ID {worker_id} already exists.")
#             return jsonify({"message": "Worker ID already exists"}), 400

#         workers[worker_id] = {
#             "name": data["name"],
#             "position": data["position"],
#             "salary": data.get("salary", 0),
#         }
#         logging.info(f"Worker with ID {worker_id} added successfully.")
#         return jsonify({"message": "Worker added", "worker": workers[worker_id]})


# # API Endpoints
# api.add_resource(WorkerList, '/workers')  # List all workers, Add a new worker
# api.add_resource(Worker, '/workers/<string:worker_id>')  # Get, Update, Delete worker by ID

# # Simple test route
# @app.route('/test', methods=['GET'])
# def test():
#     """
#     Simple test route to ensure the server is running.
#     """
#     logging.debug("Test route accessed.")
#     return "API is working!"


# # Run the Flask application
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import logging

# Initialize Flask application
app = Flask(__name__)
api = Api(app)

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

# Resource for a single worker
class Worker(Resource):
    def get(self, worker_id):
        if worker_id in workers:
            logging.debug(f"Fetching worker with ID: {worker_id}")
            return jsonify({"worker": workers[worker_id]})
        logging.warning(f"Worker with ID {worker_id} not found.")
        return jsonify({"message": "Worker not found"}), 404

    def put(self, worker_id):
        data = request.get_json()
        logging.debug(f"PUT data received for worker ID {worker_id}: {data}")
        if not data or 'name' not in data or 'position' not in data:
            return jsonify({"message": "Invalid data. 'name' and 'position' are required."}), 400

        workers[worker_id] = {
            "name": data["name"],
            "position": data["position"],
            "salary": data.get("salary", 0),
        }
        logging.info(f"Worker with ID {worker_id} updated successfully.")
        return jsonify({"message": "Worker updated", "worker": workers[worker_id]})

    def delete(self, worker_id):
        if worker_id in workers:
            del workers[worker_id]
            logging.info(f"Worker with ID {worker_id} deleted.")
            return jsonify({"message": "Worker deleted"})
        logging.warning(f"Worker with ID {worker_id} not found for deletion.")
        return jsonify({"message": "Worker not found"}), 404

# Resource for all workers
class WorkerList(Resource):
    def get(self):
        logging.debug("Fetching all workers.")
        return jsonify({"workers": workers})

    def post(self):
        data = request.get_json()
        logging.debug(f"POST data received: {data}")
        if not data or 'id' not in data or 'name' not in data or 'position' not in data:
            return jsonify({"message": "Invalid data. 'id', 'name', and 'position' are required."}), 400

        worker_id = data["id"]
        if worker_id in workers:
            logging.warning(f"Worker ID {worker_id} already exists.")
            return jsonify({"message": "Worker ID already exists"}), 400

        workers[worker_id] = {
            "name": data["name"],
            "position": data["position"],
            "salary": data.get("salary", 0),
        }
        logging.info(f"Worker with ID {worker_id} added successfully.")
        return jsonify({"message": "Worker added", "worker": workers[worker_id]})

# API Endpoints
api.add_resource(WorkerList, '/workers')  # List all workers, Add a new worker
api.add_resource(Worker, '/workers/<string:worker_id>')  # Get, Update, Delete worker by ID

# Simple test route
@app.route('/test', methods=['GET'])
def test():
    logging.debug("Test route accessed.")
    return "API is working!"

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

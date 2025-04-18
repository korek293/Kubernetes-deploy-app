# Kubernetes-deploy-app

This project is a Flask web application that interfaces with a MongoDB database, offering user interaction through a form and exposing several diagnostic API endpoints.

The app features a simple front-end rendered using Jinja templates, where users can submit messages stored in a MongoDB collection; this interaction is managed through a /test_db route with form validation.

It utilizes environment variables for key configurations such as background color, MongoDB connection details, and error flags—making it highly adaptable and suitable for different deployment environments.

The entire setup is deployed on Kubernetes using a combination of a Deployment for the application and a StatefulSet for MongoDB, backed by persistent storage to retain data across pod restarts.

Robust health check endpoints (/healthz and /healthx) are implemented to ensure Kubernetes can perform proper liveness and readiness probing, while ConfigMap and Secret resources provide secure and flexible runtime configuration.

![image](https://github.com/user-attachments/assets/b378bcf7-ff27-4e71-bd79-8eb01c47b3b7)

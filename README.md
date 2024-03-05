# Flask Hello World App

This application serves a simple webpage that alternates between displaying "Hello" and "World" each time it is accessed.

## Getting Started

These instructions will cover usage information for building and deploying the Flask application locally and on Kubernetes.

### Prerequisites

- Docker
- Kubernetes cluster (optional)
- kubectl configured (for Kubernetes deployment)

### Building the Application

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <your-repository-directory>
```

2. Build the Docker image:
```docker build -t flask-hello-world .
```

### Running Locally
```
docker run -d -p 5000:5000 flask-hello-world
```

###  Deploying to Kubernetes

1. Push the Docker image to your container registry.

2. Update the deployment.yaml file with the image path.

3. Apply the Kubernetes deployment:
    ```
    kubectl apply -f deployment.yaml

    ```






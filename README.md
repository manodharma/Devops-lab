# Devops trainee Practical Assessment
This repository contains the code and configuration for Practical Assessment, which is deployed locally in a Kubernetes cluster using Kind (Kubernetes IN Docker) and exposed via Ingress

## Prerequisites

Before you begin, ensure you have the following installed:

*Kind: A tool to run Kubernetes clusters in Docker.
*kubectl: The Kubernetes command-line tool.
*Docker: Required for building images and running Kind.
*Ingress Controller: For exposing services via HTTP(S).

## Setup

### Install Kind and kubectl
[Kind Installation](https://kind.sigs.k8s.io/docs/user/quick-start/#installation),[kubectl Installation](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)


### Create a Kind Cluster

Create a Kind cluster using the config file:

```kind create cluster --config kind-config.yaml```

### Install Ingress Controller

Deploy the NGINX Ingress Controller to your Kind cluster:
```kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml```

### Build the Docker image
```docker build -t mano7kumarasamy:latest```

### Deploy the Application

```kubectl apply -f deployment.yaml```
```kubectl apply -f ingress.yaml```

### Access the Application
```kubectl get services -o wide -w --namespace ingress-nginx```

## Update your local /etc/hosts file

Update your local /etc/hosts file to map the Ingress hostname to the IP address of the Ingress controller.

```echo "<nodeport IP> wisecow.local" | sudo tee -a /etc/hosts```

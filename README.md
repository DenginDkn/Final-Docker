# Final-Docker
 
This project is developed using Azure, Python 3.10, and Docker.

## Getting Started

This guide will help you get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have the following software installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [GitActions](https://docs.github.com/en/actions)

### Installation

Clone the project locally:

```bash
git clone https://github.com/username/project-name.git cd project-name 
````

### Creating a Virtual Environment and Installing Dependencies
Create and activate the Python virtual environment:
```bash
python3.10 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
````

### Install dependencies from the requirements file:
```bash
pip install -r requirements.txt
````

### Using Docker
Follow these steps to build and run the Docker image:

Build the Docker image:

````bash
docker build -t project-name:latest .
````

Run the Docker container:

````bash
docker run -d -p 8000:8000 project-name:latest
````

Deployment on Azure
Log in to Azure CLI
````bash
az login
````

### Create Azure Container Registry (ACR) and Web App
Use the following commands to create the necessary Azure resources:

````bash
az group create --name myResourceGroup --location eastus
az acr create --resource-group myResourceGroup --name myContainerRegistry --sku Basic
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1 --is-linux
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name myWebApp --deployment-container-image-name myContainerRegistry.azurecr.io/project-name:latest
````
### Push Docker Image to ACR
Log in to ACR using Docker CLI:

````bash
az acr login --name myContainerRegistry
````
Tag and push the Docker image:

````bash
docker tag project-name:latest myContainerRegistry.azurecr.io/project-name:latest
docker push myContainerRegistry.azurecr.io/project-name:latest
````
### Update Azure Web App
Use the following command to update the Azure Web App to use the Docker image:

````bash
az webapp config container set --name myWebApp --resource-group myResourceGroup --docker-custom-image-name myContainerRegistry.azurecr.io/project-name:latest
````
### CI/CD with GitHub Actions
This project uses GitHub Actions to build the Docker image and push it to Azure Container Registry (ACR) and Azure Web App. The .github/workflows/main.yml file manages the CI/CD processes.

Set up GitHub Secrets:

AZURE_CREDENTIALS: Azure service principal credentials
REGISTRY_USERNAME: ACR username
REGISTRY_PASSWORD: ACR password

Contributing
If you would like to contribute, please open a pull request. All contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.




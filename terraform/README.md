# Terraform Deployment for GitHub Gists API

This folder contains Terraform configuration to build and deploy the GitHub Gists API Docker container on Docker Desktop (Windows 11).

## Prerequisites

- Docker Desktop installed and running on Windows 11
- Terraform installed (version 1.x)
- PowerShell or Command Prompt
- Terraform state must be stored in S3 or any database for persistence and collaboration

## Usage

1. Navigate to this directory:
   ```powershell
   cd terraform
   ```

2. Initialize Terraform:
   ```powershell
   terraform init
   ```

3. Plan the deployment:
   ```powershell
   terraform plan
   ```

4. Apply the configuration:
   ```powershell
   terraform apply
   ```

5. Access the API at: `http://localhost:8080/<username>`

## Cleanup

To destroy the container and image:
```powershell
terraform destroy
```
variable "image_name" {
  description = "Name of the Kubernetes container image"
  type        = string
  default     = "mantragya/githubapi:latest"
}

variable "deployment_name" {
  description = "Name of the Kubernetes deployment"
  type        = string
  default     = "github-gists-api"
}

variable "service_name" {
  description = "Name of the Kubernetes service"
  type        = string
  default     = "github-gists-api-service"
}

variable "external_port" {
  description = "Port exposed by the Kubernetes service"
  type        = number
  default     = 8080
}

variable "internal_port" {
  description = "Port the container listens on"
  type        = number
  default     = 8080
}

variable "replicas" {
  description = "Number of deployment replicas"
  type        = number
  default     = 1
}
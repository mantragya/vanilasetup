output "service_name" {
  description = "Kubernetes service name"
  value       = kubernetes_service.github_gists_api.metadata[0].name
}

output "service_node_port" {
  description = "NodePort assigned to the Kubernetes service"
  value       = kubernetes_service.github_gists_api.spec[0].port[0].node_port
}

output "service_type" {
  description = "Type of Kubernetes service"
  value       = kubernetes_service.github_gists_api.spec[0].type
}
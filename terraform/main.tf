resource "kubernetes_deployment" "github_gists_api" {
  metadata {
    name = var.deployment_name
    labels = {
      app = "github-gists-api"
    }
  }

  spec {
    replicas = var.replicas

    selector {
      match_labels = {
        app = "github-gists-api"
      }
    }

    template {
      metadata {
        labels = {
          app = "github-gists-api"
        }
      }

      spec {
        container {
          name  = "github-gists-api"
          image = var.image_name

          port {
            container_port = var.internal_port
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "github_gists_api" {
  metadata {
    name = var.service_name
  }

  spec {
    selector = {
      app = "github-gists-api"
    }

    port {
      port        = var.external_port
      target_port = var.internal_port
      protocol    = "TCP"
    }

    type = "NodePort"
  }
}
resource "docker_container" "frontend" {
  name     = "${local.project_name}-frontend-${var.environment}"
  image    = docker_image.frontend.name
  hostname = "frontend.admetricks"

  attach   = false
  must_run = true
  logs     = true
  restart  = "unless-stopped"

  env = [
    "ENVIRONMENT=${var.environment}",
  ]

  ports {
    external = 3000
    internal = 80
  }

  networks_advanced {
    name = docker_network.admetricks.name
    aliases = [
      "frontend"
    ]
  }
}

resource "docker_image" "frontend" {
  name = "${local.project_name}/frontend"

  build {
    path       = abspath(path.cwd)
    dockerfile = "./infrastructure/docker/frontend.dockerfile"

    tag = [
      "${var.environment}"
    ]

    label = {
      author : "ixmael"
    }
  }
}

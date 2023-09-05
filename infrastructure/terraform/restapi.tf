resource "docker_container" "api" {
  name     = "${local.project_name}-api-${var.environment}"
  image    = docker_image.api.name
  hostname = "api.admetricks"

  attach   = false
  must_run = true
  logs     = true
  restart  = "unless-stopped"

  env = [
    "ENVIRONMENT=${var.environment}",
  ]

  ports {
    external = 9000
    internal = 80
  }

  networks_advanced {
    name = docker_network.admetricks.name
    aliases = [
      "api"
    ]
  }
}

resource "docker_image" "api" {
  name = "${local.project_name}/api"

  build {
    path       = abspath(path.cwd)
    dockerfile = "./infrastructure/docker/restapi.dockerfile"

    tag = [
      "${var.environment}"
    ]

    label = {
      author : "ixmael"
    }
  }
}

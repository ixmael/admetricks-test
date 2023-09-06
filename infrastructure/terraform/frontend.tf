resource "docker_container" "frontend" {
  name     = "${local.project_name}-frontend-${var.environment}"
  image    = var.frontendOnlyBuild ? docker_image.frontendBuild.name : docker_image.frontend.name
  hostname = "frontend.admetricks"

  attach   = false
  must_run = true
  logs     = true

  ports {
    external = 3000
    internal = 80
  }

  env = [
    "ENVIRONMENT=${var.environment}",
  ]

  volumes {
    volume_name    = docker_volume.frontend.name
    container_path = "/packages/frontend"
  }
}

resource "docker_image" "frontendBuild" {
  name = "${local.project_name}/frontendbuilder"

  build {
    path       = abspath(path.cwd)
    dockerfile = "./infrastructure/docker/frontend.build.dockerfile"

    tag = [
      "${var.environment}"
    ]

    label = {
      author : "ixmael"
    }
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

resource "docker_volume" "frontend" {
  name = "${local.project_name}-frontend-${var.environment}"
  driver_opts = {
    type   = "none"
    device = local.frontend_path
    o      = "bind"
  }
}


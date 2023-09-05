resource "docker_network" "admetricks" {
  name   = "${local.project_name}-network-${var.environment}"
  driver = "bridge"
}

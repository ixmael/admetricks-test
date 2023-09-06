variable "environment" {
  type        = string
  description = "The environment"
  default     = "production"
}

variable "frontendOnlyBuild" {
  type = bool
  description = "Only build the frontend"
  default = false
}

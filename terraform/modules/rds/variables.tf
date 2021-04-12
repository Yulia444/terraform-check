variable "region" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "rds_subnet1" {
  type = string
}

variable "rds_subnet2" {
  type = string
}

variable "instance_class" {
  type = string
  default = "db.t2.micro"
}

variable "allocated_storage" {
  type = number
}

variable "engine" {
  type = string
}

variable "engine_version" {
  type = string
}

variable "name" {
  type = string
}

variable "identifier" {
  type = string
}

variable "username" {
  type = string
}
variable "vpc_name" {
    type = string
    default = "vpc"
}

variable "public_subnets" {
    type = list(string)
    default = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
}

variable "private_subnets" {
    type = list(string)
    default = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "instance_count" {
  type = number
  default = 1
}

variable "instance_type" {
  type = string
  default = "t2.micro"
}

variable "cluster_name" {
  type = string
  default = "demo"
}

variable "cidr" {
  type = string
  default = "10.0.0.0/16"
}

variable "region" {
  type = "string"
  default = "us-east-2"
}

variable "allocated_storage" {
  default = 20
}

variable "engine" {
  default = "postgres"
}

variable "engine_version" {
  default = "11.10"
}

variable "name" {
  // RDS database name
  default = "mydb1"
}

variable "identifier" {
  // RDS database identifier
  default = "mydb1"
}

variable "username" {
  // RDS database username
  default = "mydb1"
}
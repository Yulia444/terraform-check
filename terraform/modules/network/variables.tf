variable "vpc_name" {
    type = string
}

variable "instance_count" {
    type = number
}

variable "cidr" {
    type = string
}

variable "public_subnets" {
    type = list(string)
}

variable "private_subnets" {
    type = list(string)
}

variable "cluster_name" {
    type = string
}
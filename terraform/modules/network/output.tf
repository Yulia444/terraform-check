output "vpc_id" {
  value = module.network.vpc_id
}

output "subnet_1" {
    value = element(module.network.public_subnets, 0)
}

output "subnet_2" {
  value = element(module.network.public_subnets, 1)
}

output "public_subnets" {
  value = module.network.public_subnets
}

output "private_subnets" {
  value = module.network.private_subnets
}
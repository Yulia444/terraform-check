module "network" {
    source = "./modules/network"
    vpc_name = var.vpc_name
    cidr = var.cidr
    public_subnets = var.public_subnets
    private_subnets = var.private_subnets
    cluster_name = var.cluster_name
    instance_count = var.instance_count
}

module "eks" {
    source = "./modules/eks"
    vpc_id = module.network.vpc_id
    public_subnets = module.network.public_subnets
    private_subnets = module.network.private_subnets
    cluster_name = var.cluster_name
    instance_type = var.instance_type
}


module "rds" {
    source = "./modules/rds"
    vpc_id = module.network.vpc_id
    region = var.region
    rds_subnet1 = module.network.subnet_1
    rds_subnet2 = module.network.subnet_2
    allocated_storage = var.allocated_storage
    engine = var.engine
    engine_version = var.engine_version
    name = var.name
    identifier = var.identifier
    username = var.username
}

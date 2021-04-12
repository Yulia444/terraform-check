provider "aws" {
  region  = var.region
  profile = "terraform"
}

terraform {
  required_version = "> 0.14.0"
}

data "aws_vpc" "selected" {
  id = var.vpc_id
}

resource "aws_db_subnet_group" "rds-private-subnet" {
  name       = "rds-private-subnet-group"
  subnet_ids = [ var.rds_subnet1, var.rds_subnet2 ]
}

resource "random_string" "demo_postgres_password" {
  length  = 12
  upper   = true
  number  = true
  special = false
}

resource "aws_security_group" "postgres" {
  name        = "mydb1"
  description = "RDS postgres servers"
  vpc_id      = data.aws_vpc.selected.id
  
  # Only postgres in
  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
}

resource "aws_db_instance" "postgres" {
  allocated_storage      = var.allocated_storage
  engine                 = var.engine
  engine_version         = var.engine_version
  identifier             = var.identifier
  instance_class         = var.instance_class
  multi_az               = false
  name                   = var.name
  password               = random_string.demo_postgres_password.result
  port                   = 5432
  skip_final_snapshot    = true
  publicly_accessible    = true
  username               = var.username
  vpc_security_group_ids = [aws_security_group.postgres.id]
  db_subnet_group_name = aws_db_subnet_group.rds-private-subnet.name

  maintenance_window      = "Mon:00:00-Mon:03:00"
  backup_window           = "03:00-06:00"
  backup_retention_period = 1
}
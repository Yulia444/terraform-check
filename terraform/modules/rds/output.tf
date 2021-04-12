output "rds_host" {
  value = aws_db_instance.postgres.endpoint
}

output "rds_username" {
  value = aws_db_instance.postgres.username
}

output "rds_db_name" {
  value = aws_db_instance.postgres.name
}

output "rds_password" {
  value = aws_db_instance.postgres.password
}


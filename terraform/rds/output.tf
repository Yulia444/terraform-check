output "RDS_HOST" {
  value = aws_db_instance.postgres.endpoint
  sensitive = true
}

output "RDS_USERNAME" {
  value = aws_db_instance.postgres.username
}

output "RDS_DB_NAME" {
  value = aws_db_instance.postgres.name
}

output "RDS_PASSWORD" {
  value = aws_db_instance.postgres.password
}

output "RDS_PORT" {
  value = aws_db_instance.postgres.port
}
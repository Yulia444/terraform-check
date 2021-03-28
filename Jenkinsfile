pipeline {
    tools {
        terraform 'terraform'
    }
    agent any
    stages {
        stage('Terraform Init For EKS') {
            steps {
                dir('terraform/eks') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2'){
                    sh 'terraform init'
                    }
                }

            }
        }
        stage('Terraform Plan For EKS') {
            steps {
                dir('terraform/eks') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        sh 'terraform plan -out=tfplan -input=false'
                    }
                }
            }
        }

        stage('User Approval For Applying Terraform For EKS') {
            steps {
                echo "Proceed applying terraform for EKS?:"
                input(message: 'Proceed applying terraform for EKS?', ok: 'Yes', 
                parameters: [booleanParam(defaultValue: true, 
                description: 'This will apply changes in EKS terraform',name: 'Yes?')])
            }
        }

        stage('Terraform Apply For EKS') {
            steps {
                dir('terraform/eks') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        sh "terraform apply -input=false  -auto-approve"
                    }
                }
            }
        }

        stage('Terraform Init For RDS') {
            steps {
                dir('terraform/rds') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2'){
                    sh 'terraform init'
                    }
                }

            }
        }

        stage('Terraform Plan For RDS') {
            steps {
                dir('terraform/eks') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2'){
                        sh 'export VPC_ID $(terraform output vpc-id)'
                    }
                }
                dir('terraform/rds') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        sh 'terraform plan -out=tfplan -input=false'
                    }
                }
            }
        }

        stage('User Approval For Applying Terraform For RDS') {
            steps {
                echo "Proceed applying terraform for RDS?:"
                input(message: 'Proceed applying terraform for RDS?', ok: 'Yes', 
                parameters: [booleanParam(defaultValue: true, 
                description: 'This will apply changes in RDS terraform',name: 'Yes?')])
            }
        }

        stage('Terraform Apply For RDS') {
            steps {
                dir('terraform/rds') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        sh "terraform apply -input=false  -auto-approve"
                    }
                }
            }
        }

        stage('User Approval For Destroying Terraform For EKS') {
            steps {
                echo "Proceed destroying terraform for EKS?:"
                input(message: 'Proceed destroying terraform for EKS?', ok: 'Yes', 
                parameters: [booleanParam(defaultValue: false, 
                description: 'This will destroy changes in EKS terraform',name: 'Yes?')])
            }
        }

        stage('Terraform Destroy EKS') {
            steps {
                dir('terraform/eks') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        sh "terraform destoy -input=false -auto-approve"
                    }
                }
            }
        }

        stage('User Approval For Destroying Terraform For RDS') {
            steps {
                echo "Proceed destroying terraform for RDS?:"
                input(message: 'Proceed destroying terraform for RDS?', ok: 'Yes', 
                parameters: [booleanParam(defaultValue: false, 
                description: 'This will destroy changes in RDS terraform',name: 'Yes?')])
            }
        }

        stage('Terraform Destroy RDS') {
            steps {
                dir('terraform/rds') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        sh "terraform destoy -input=false -auto-approve"
                    }
                }
            }
        }
    }
}
def RDS_DB_NAME
def RDS_HOST
def RDS_PASSWORD
def RDS_USERNAME
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
        stage('Install helm') {
            steps {
                script {
                    sh (
                        label: "Installing Helm and tiller",
                        script: """#!/usr/bin/env bash
                        wget https://get.helm.sh/helm-v3.1.0-linux-amd64.tar.gz
                        tar -xvzf helm-v3.1.0-linux-amd64.tar.gz
                        mv linux-amd64/helm helm
                        """
                    )
                }
            }
        }
        stage('Export env variables for RDS instance') {
            steps {
                dir('/terraform/rds') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        script {
                            sh "export AWS_DEFAULT_OUTPUT=text"
                            RDS_DB_NAME = sh(script: """export RDS_DB_NAME=\$(echo \$(terraform output RDS_DB_NAME) | tr -d '"')""",
                                             returnStdout: true).trim()
                            RDS_HOST = sh(script: """export RDS_HOST=\$(echo \$(terraform output RDS_HOST) | tr -d '"')""",
                                          returnStdout: true).trim()
                            RDS_USERNAME = sh(script: """export RDS_USERNAME=\$(echo \$(terraform output RDS_USERNAME) | tr -d '"')""",
                                              returnStdout: true).trim()
                            RDS_PASSWORD = sh(script: """export RDS_PASSWORD=\$(echo \$(terraform output RDS_PASSWORD) | tr -d '"')""",
                                              returnStdout: true).trim()
                        }
                    }
                }
            }
        }

        stage('Install demo through helm') {
            steps {
                dir('/helm') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        script {
                            sh (
                                script: """export KUBECONFIG=../terraform/eks/kubeconfig_demo && \
                                helm install demo-chart ./demo \
                                --set RDS_USERNAME=$RDS_USERNAME --set RDS_DB_NAME=$RDS_DB_NAME \
                                --set RDS_HOST=$RDS_HOST --set RDS_PASSWORD=$RDS_PASSWORD
                                """
                            )
                        }
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

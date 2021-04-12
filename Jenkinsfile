pipeline {
    tools {
        terraform 'terraform'
    }
    environment {
        RDS_DB_NAME = ""
        RDS_HOST = ""
        RDS_PASSWORD = ""
        RDS_USERNAME = ""
        name = "demo"
        RELEASE_NAME = "datadogagentdemo"
    }
    agent any
    stages {
        stage('Terraform Init') {
            steps {
                dir('terraform') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2'){
                    sh 'terraform init'
                    }
                }

            }
        }
        stage('Terraform Plan') {
            steps {
                dir('terraform') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        sh 'terraform plan -out=tfplan -input=false'
                    }
                }
            }
        }

        stage('User Approval For Applying Infrastructure') {
            steps {
                echo "Proceed applying terraform options?:"
                input(message: 'Proceed applying terraform options?', ok: 'Yes', 
                parameters: [booleanParam(defaultValue: true, 
                description: 'This will apply changes in terraform',name: 'Yes?')])
            }
        }

        stage('Terraform Apply For EKS') {
            steps {
                dir('terraform') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        sh "terraform apply -input=false  -auto-approve"
                    }
                }
            }
        }

        stage('Update kubeconfig') {
            steps {
                withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                    sh "aws eks update-kubeconfig --name $name}"
                }
            }
        }
        stage('Download Helm') {
            steps {
                script {
                    sh (
                        label: "Installing Helm",
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
                dir('terraform') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        script {
                            sh "export AWS_DEFAULT_OUTPUT=text"
                            RDS_DB_NAME = sh(script: """echo \$(terraform output RDS_DB_NAME) | tr -d '"'""", returnStdout: true).trim()
                            RDS_HOST = sh(script: """echo \$(terraform output RDS_HOST) | tr -d '"'""", returnStdout: true).trim()
                            RDS_USERNAME = sh(script: """echo \$(terraform output RDS_USERNAME) | tr -d '"'""", returnStdout: true).trim()
                            RDS_PASSWORD = sh(script: """echo \$(terraform output RDS_PASSWORD) | tr -d '"'""", returnStdout: true).trim()
                            sh "echo $RDS_PASSWORD"
                            sh "echo $RDS_HOST"
                            sh "echo $RDS_USERNAME"
                            sh "echo $RDS_DB_NAME"
                        }
                    }
                }
            }
        }
        stage('Deploy project through helm') {
            steps {
                dir('helm') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        script {
                            sh (
                                script: """helm install demo-chart ./demo \
                                --set RDS_USERNAME=$RDS_USERNAME --set RDS_DB_NAME=$RDS_DB_NAME \
                                --set RDS_HOST=$RDS_HOST --set RDS_PASSWORD=$RDS_PASSWORD
                                """
                            )
                        }
                    }
                }
            }
        }
        stage('Deploy datadog agent for Kubernetes') {
            steps {
                dir('helm/datadog'){
                    script {
                        sh (
                            script :"""helm repo add datadog https://helm.datadoghq.com && \
                            helm repo add stable https://charts.helm.sh/stable && \
                            helm repo update && \
                            helm install $RELEASE_NAME -f datadog-values.yaml \
                            --set datadog.site='datadoghq.com' \
                            --set datadog.apiKey=29de05566ae7878b1ffe846247a76b5b datadog/datadog 
                            """
                        )
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

        stage('Terraform Destroy AWS Infrastructure') {
            steps {
                dir('terraform') {
                    withAWS(credentials: 'aws_credentials_terraform_user', region: 'us-east-2') {
                        sh "terraform destroy -input=false -auto-approve"
                    }
                }
            }
        }

    }
}
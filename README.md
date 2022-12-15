# Clickr Project
The purpose of the Clickr project is to create a simple web app, but implement all the important components that go into running a production system. We will focus more on the supportive elements that make a system run, moreso than the application itself. 

The premise of the base application is simple: you increment a counter. All Clickr front ends will have a button which can be used to increment a single atomic value. 

The backend of clickr will have two routes: one to serve the front-end application and another than will be used to increment the counter. 

## Roadmap

- [ ] CI
  - [ ] linting
  - [ ] testing
  - [ ] tagging
  - [ ] building artifacts
- [ ] CD 
  - [ ] staging environment
  - [ ] production environment
  - [ ] kubernetes? 
- [ ] Monitoring
  - [ ] logging
  - [ ] dashboards
- [ ] Security
  - [ ] key managment
  - [ ] key rotation

## Tools Used
- Application
  - Language: Python & Poetry
  - Backend: Flask
  - Database: DynamoDB
- CI
  - Pipeline: Github Actions
  - Container Service: Podman
  - Artifact Registry: AWS ECR
  - Monitoring: Prometheus & Grafana
- CD
  - Deployment: Kubernetes
- Security
  - Key Management: AWS KMS
    

# AWS Serverless Web Scraper

This project demonstrates how to deploy a serverless web scraper application on AWS using Lambda, API Gateway, S3, CloudWatch, and CodePipeline.

## Overview

The project consists of several components:

- **Lambda Function**: A Python Flask application deployed as an AWS Lambda function to scrape job listings from a website and store them in an S3 bucket.
- **API Gateway**: Exposes the Lambda function as a RESTful API for external access.
- **S3 Bucket**: Stores the scraped job listings data.
- **CloudWatch Event**: Triggers the Lambda function on a scheduled basis to update job listings regularly.
- **CodePipeline**: Implements a CI/CD pipeline to automate the deployment of the application.

## Deployment Steps

### 1. Deploy Lambda Function

- Upload the `lambda_function/app.py`, `lambda_function/job_scraper.py`, and `lambda_function/storage_manager.py` files to your Lambda function's code.
- Use the CloudFormation template `cloudformation/lambda_function.yaml` to create the Lambda function.

### 2. Create API Gateway

- Use the CloudFormation template `cloudformation/api_gateway.yaml` to create an API Gateway.

### 3. Set Up S3 Bucket

- Use the CloudFormation template `cloudformation/s3_bucket.yaml` to create an S3 bucket.

### 4. Configure CloudWatch Event

- Use the CloudFormation template `cloudformation/cloudwatch_event.yaml` to create a CloudWatch Event.

### 5. Implement CodePipeline

- Use the CloudFormation template `cloudformation/codepipeline.yaml` to create a CodePipeline.
- Configure your GitHub repository as the source for the pipeline.
- Set up the build and deployment stages to deploy changes automatically.

## Usage

Once deployed, you can use the API Gateway endpoint to access the application. Here are some sample API endpoints:

- `GET /job_listings`: Retrieve the latest job listings.
- `POST /scrape_jobs?search_query=keyword`: Scrape new job listings based on the provided search query.

## Requirements

- Python 3.x
- Flask
- BeautifulSoup
- Boto3
- AWS CLI
- AWS Account with appropriate IAM permissions

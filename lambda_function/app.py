# This file contains the main Flask application code for the AWS Lambda function.

from flask import Flask, request, jsonify
from job_scraper import scrape_job_listings
from storage_manager import save_job_listings, load_job_listings

app = Flask(__name__)

def lambda_handler(event, context):
    """
    Lambda function handler. Handles incoming HTTP requests.
    """
    if event['httpMethod'] == 'GET':
        # Handle GET request to retrieve job listings
        job_listings = load_job_listings()
        return {
            'statusCode': 200,
            'body': jsonify(job_listings).data
        }
    elif event['httpMethod'] == 'POST':
        # Handle POST request to scrape and save new job listings
        search_query = event['queryStringParameters']['search_query']
        job_listings = scrape_job_listings(search_query)
        save_job_listings(job_listings)
        return {
            'statusCode': 200,
            'body': jsonify({'message': 'Job listings saved successfully'}).data
        }
    else:
        # Handle other HTTP methods
        return {
            'statusCode': 405,
            'body': jsonify({'error': 'Method not allowed'}).data
        }

if __name__ == '__main__':
    app.run()

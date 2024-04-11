# This file contains functions to scrape job listings from a website.

import requests
from bs4 import BeautifulSoup

def scrape_job_listings(search_query):
    """
    Scrapes job listings from a website based on the given search query.
    """
    # Example: Scraping job listings from a website
    url = f"https://example.com/jobs?q={search_query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse HTML content and extract job listings
        soup = BeautifulSoup(response.content, 'html.parser')
        job_listings = []
        for listing in soup.find_all('div', class_='job-listing'):
            job_title = listing.find('h2').text.strip()
            company = listing.find('p', class_='company').text.strip()
            location = listing.find('p', class_='location').text.strip()
            job_listings.append({
                'title': job_title,
                'company': company,
                'location': location
            })
        return job_listings
    else:
        print(f"Failed to fetch job listings. Status code: {response.status_code}")
        return []

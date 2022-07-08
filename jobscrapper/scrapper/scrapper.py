# scrapper.py
from typing import Any, Dict, List
import mechanicalsoup as soup

from jobscrapper.scrapper.defaults import DEFAULT_JOB_LOCATION
from .config import get_config
from .utils import data_sanitizer


def linkedin_scrapper(
    job_position, job_location=DEFAULT_JOB_LOCATION
) -> List[Dict[str, Any]]:
    """
    linkedin_scrapper makes a scrapping request into linkedin jobs site
    then return a list of dictionaries with the received data:
    Parameters:
        - job_position: str | 'work_name'
        - job_location: str | 'country/city' defaults: DEFAULT_JOB_LOCATION
    Returns:
        - 'works': {
            'position': 'work_name',
            'company': 'company_name',
            'location: 'country/city',
        }
    """
    browser = soup.StatefulBrowser()
    user_agent, url = get_config(
        work_keyword=job_position, location_keyword=job_location
    )
    browser.set_user_agent(user_agent)
    browser.open(url)
    page = browser.page
    positions = page.find_all("h3", {"class": "base-search-card__title"})
    companies = page.find_all("h4", {"class": "base-search-card__subtitle"})
    locations = page.find_all("span", {"class": "job-search-card__location"})
    urls = a = page.find_all(
        "a",
        {
            "class": "base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]"
        },
    )
    urls = [url["href"] for url in urls]
    positions = data_sanitizer(positions)
    companies = data_sanitizer(companies)
    locations = data_sanitizer(locations)

    job_list = [
        {"position": position, "company": company, "location": location, "url": url}
        for position, company, location, url in zip(
            positions, companies, locations, urls
        )
    ]

    return job_list

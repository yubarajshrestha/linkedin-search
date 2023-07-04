import os
import requests
from utils.clean_util import cleaned_data


def remove_people_also_viewed(data):
    """remove people also viewed"""
    if not isinstance(data, (dict, list)):
        return data

    if isinstance(data, list):
        return [v for v in (remove_people_also_viewed(v) for v in data) if v]

    return {k: v for k, v in ((k, remove_people_also_viewed(v)) for k, v in data.items()) if v and k != "people_also_viewed"}


def scrape_linkedin_profile(linked_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile page"""

    api_endpoint = "https://nubela.co/api/v2/linkedin"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {os.environ.get("PROXYURL_API_KEY")}',
    }
    response = requests.get(api_endpoint, params={"url": linked_profile_url}, headers=headers)

    data = cleaned_data(response.json())
    return remove_people_also_viewed(data)

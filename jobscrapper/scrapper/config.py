# config.py
from typing import Tuple

from jobscrapper.scrapper.defaults import DEFAULT_JOB_LOCATION


def get_config(
    work_keyword: str, location_keyword: str = DEFAULT_JOB_LOCATION
) -> Tuple[str, str]:
    """
    get_config setups the necessary settings for mechaniclasoup actions
    Parameters:
        - work_keyword: str | this is the work name and query parameter for the request
        - location_keyword: str | this is the work location ad query parameter for the request
            defaults: DEFAULT_JOB_LOCATION
    Returns:
        - user_agent: str | for allow linkedin scrapper requests
        - url: str | the url of the requests
    """
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    url = f"https://www.linkedin.com/jobs/search?keywords={work_keyword}&location={location_keyword}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    return user_agent, url

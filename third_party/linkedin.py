import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    if mock:
        linkedin_profile_url= "https://gist.githubusercontent.com/Korkevados/0af3498a896f45d976c3769756961db5/raw/cce1e8c4df49389d4e93d66098dfadcf2cac6d51/eden_marco_linkedin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        print(os.environ["SCRAPIN_API_KEY"])
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        # params = {
        #     "apikey": os.environ["SCRAPIN_API_KEY"],
        #     "linkedInUrl": linkedin_profile_url,
        # }
        params = {"apikey": os.environ["SCRAPIN_API_KEY"],
                       "linkedInUrl": linkedin_profile_url}

        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )
    data = response.json().get("person")
    if data is not None:
        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None) and k not in ["certifications"]
        }
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco/"
        ),
    )
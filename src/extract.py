import requests

from config.settings import (
    ADZUNA_BASE_URL,
    ADZUNA_APP_ID,
    ADZUNA_API_KEY,
)


class AdzunaClient:
    """
    Client responsible for communicating with the Adzuna API.
    """

    def __init__(self, timeout: int = 15):
        self.base_url = ADZUNA_BASE_URL
        self.app_id = ADZUNA_APP_ID
        self.api_key = ADZUNA_API_KEY
        self.timeout = timeout

        # Reuse the same HTTP connection for better performance.
        self.session = requests.Session()

    def fetch_jobs(self, page: int = 1):
        """Fetch job listings from the Adzuna API.

        Returns:
            dict: Parsed JSON response from the Adzuna API.

        Raises:
            requests.exceptions.Timeout: If the request times out.
            requests.exceptions.ConnectionError: If a network connection cannot be established.
            requests.exceptions.HTTPError: If the API returns an HTTP error.
            requests.exceptions.RequestException: For any other request-related error.
        """

        url = (
            f"{self.base_url}/jobs/in/search/{page}"
            f"?app_id={self.app_id}"
            f"&app_key={self.api_key}"
        )

        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            raise requests.exceptions.Timeout("The request to the Adzuna API timed out.")

        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError("Unable to connect to the Adzuna API.")

        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError(f"Adzuna API returned HTTP {response.status_code}.")

        except requests.exceptions.RequestException as error:
            raise requests.exceptions.RequestException(f"Unexpected request error: {error}")
        
    def fetch_multiple_pages(self, pages: int = 10):
        """
    Fetch multiple pages of job listings from the Adzuna API.

    Args:
        pages (int): Number of pages to fetch.

    Returns:
        dict: A single dictionary containing all jobs under the
              "results" key.
        """

        all_jobs = []

        for page in range(1, pages + 1):

            page_data = self.fetch_jobs(page=page)

            all_jobs.extend(page_data["results"])

        return {
        "results": all_jobs
        }

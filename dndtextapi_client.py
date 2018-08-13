import requests, logging


class DNDTextAPIClient:
    """REST API client for DND Text API."""

    def __init__(self, host):
        self.base = host
        self.logger = logging.getLogger(__name__)

    def ping(self):
        """Returns True if it can reach the API, False otherwise."""
        url = f"{self.base}/public/channels"

        try:
            r = requests.get(url)
            if r.status_code != 200:
                self.logger.warn("Received unexpected status code `{r.status_code}` from api.")
            return r.status_code == 200
        except requests.exceptions.ConnectionError:
            self.logger.warn("Failed to ping API.")
            return False

    def check_auth(self):
        raise NotImplementedError

    def get_bot(self):
        raise NotImplementedError

    def get_character(self):
        raise NotImplementedError

    def send_message_obo_character(self):
        raise NotImplementedError

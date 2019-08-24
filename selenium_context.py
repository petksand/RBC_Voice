from selenium_client import SeleniumClient


class SeleniumContext:
    @staticmethod
    def get_instance() -> SeleniumClient:
        if not hasattr(SeleniumContext, '_instance'):
            SeleniumContext._instance = SeleniumClient()
        return SeleniumContext._instance

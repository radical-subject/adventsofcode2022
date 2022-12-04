import requests, json
# url = 'https://adventofcode.com/2020/day/8/input' -- example
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from secret_cookie_extractor import *


class PuzzleInput:
    """
    gets the puzzle input from provided link to daily task in adventofcode.com
    """
    def __init__(self, link, timeout=5.0):

        self.old_cookies = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": secret_cookie,
            "dnt": "1",
            "referer": "https://adventofcode.com/",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "cross-site",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }

        self.cookies ={
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "cookie": secret_cookie,
            "referer": "https://adventofcode.com/",
            # "sec-ch-ua": '"Not;A=Brand";v="99", "Chromium";v="106"',
            # "sec-ch-ua-mobile": "?0",
            # "sec-ch-ua-platform": "Linux",
            # "sec-fetch-dest": "document",
            # "sec-fetch-mode": "navigate",
            # "sec-fetch-site": "same-origin",
            # "sec-fetch-user": "?1",
            # "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }

        self.timeout = timeout
        self.sess = requests.Session()
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }

        self.link = link

    def get_puzzle_input(self, **kwargs):
      """
      function that retrieves puzzle input
      """

      r = self.sess.get(
                        self.link,
                        headers=self.headers,
                        timeout=self.timeout,
                        cookies=self.cookies
                        )
      soup = r.text.split("\n\n")
      return soup[:-1]



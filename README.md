# #adventofcode2020
pythonic solutions to adventofcode 2020 puzzles
<!-- export env to yml -->
conda env export --name advents > advents.yml
<!-- create env from yml file  -->
conda env create -f advents.yml

credentials to login and automatically retrieve inputs from adventofcode puzzles are secret, be careful if you use them do not put on the internet. 
i used login by github, and stored cookies for session, to use them in html_requests automatic session. smth like this:

        cookies = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                    "cookie": "_ga=xxxxxxxxxxx; _gid=xxxxxxxxxxx; _gat=x; session=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "dnt": "1",
                    "referer": "https://adventofcode.com/",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "cross-site",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
                }

the class to login is slightly modified from day to day, so it is stored in each_day_folder/modules/PazzlesAPI.py but the general idea is the same - you just need your own session id in cookies.


docker-compose up --build 
then go to jupyter-notebook and look for notebook.
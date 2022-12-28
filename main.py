# Import Files 
from collections import namedtuple
import time
import os
import sys
import requests
from typing import List
from github.InputFileContent import InputFileContent
from github import Github

# Variables
ENV_GIST_TITLE = "🟥 TETRA LEAGUE STATS 🟧"
ENV_GH_TOKEN = "GH_TOKEN"
ENV_GIST_ID = "GIST_ID"
TETR_IO_USERNAME = "TETR_IO_USERNAME"
REQUIRED_ENVS = [
    ENV_GH_TOKEN, 
    ENV_GIST_ID, 
    TETR_IO_USERNAME
]
WIDTH_JUSTIFICATION_SEPARATOR = "·"
STATS_URL = "https://ch.tetr.io/api/users/{user}"
TITLE_AND_VALUE = namedtuple("TitleAndValue", "title value")

# Methods
# Method that validates the needed ENV for the project
def validate_github_req() -> bool:
    REQUIRED_ENVS_ABSENT = [
        env for env in REQUIRED_ENVS if env not in os.environ or len(os.environ[env]) == 0
    ]

    if REQUIRED_ENVS_ABSENT:
        print(f"Please define {REQUIRED_ENVS_ABSENT} in your github actions ")
        return False
    
    return True


# Method that gets the stat from tetr.io
def get_tetr_io_stats(user: str = "hello") -> dict:
    return requests.get(STATS_URL.format(user=user)).json()


# Method on how the data will format inside the gist
def get_adjusted_line(title_and_value: TITLE_AND_VALUE, max_line_length: int) -> str:
    separation = max_line_length - (
        len(title_and_value.title) + len(title_and_value.value) + 2
    )
    separator = f"{WIDTH_JUSTIFICATION_SEPARATOR * separation}"
    return title_and_value.title + separator + title_and_value.value


# Method that checks if the string is a float
def is_float_try(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


# Method that gets the stats line and store inside the TITLE AND VALUE named tuple
def get_stats_line(stats_key: str, emoji: str, name_format: str, tetr_io_stats: dict ) -> TITLE_AND_VALUE:
    try:
        stats = str(tetr_io_stats.get("data").get("user").get("league").get(stats_key))
        
        if(is_float_try(stats)):
            stats = str(round(float(stats), 2))
            
    except Exception as e:
        stats = "N/A"

    return TITLE_AND_VALUE(emoji + " " + name_format, stats)


# Method that update the gist
def update_gist(title: str, content: str) -> bool:
    access_token = os.environ[ENV_GH_TOKEN]
    gist_id = os.environ[ENV_GIST_ID]
    gist = Github(access_token).get_gist(gist_id)
    old_title = list(gist.files.keys())[0]
    gist.edit(title, {old_title: InputFileContent(content, title)})
    print(f"{title}\n{content}")


def main():

    if not validate_github_req(): return

    tetr_io_user_name = os.environ[TETR_IO_USERNAME]
    tetr_io_stats = get_tetr_io_stats(tetr_io_user_name)

    rating_stat = get_stats_line("rating", "📈", "Ratings", tetr_io_stats)
    apm_stat = get_stats_line("apm", "🕹️", "APM", tetr_io_stats)
    pps_stat = get_stats_line("pps", "🧩", "PPS", tetr_io_stats)
    vs_stat = get_stats_line("vs", "🧱", "VS", tetr_io_stats)

    lines = [ 
        get_adjusted_line(rating_stat, 52),
        get_adjusted_line(apm_stat, 54),
        get_adjusted_line(pps_stat, 52),
        get_adjusted_line(vs_stat, 52),
    ]

    content = "\n".join(lines)
    update_gist(ENV_GIST_TITLE, content)


if __name__ == "__main__":
    s = time.perf_counter()
    if len(sys.argv) > 1:
        os.environ[ENV_GIST_ID] = sys.argv[2]
        os.environ[ENV_GH_TOKEN] = sys.argv[3]
        os.environ[TETR_IO_USERNAME] = sys.argv[4]
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


import requests
import os
import schedule
import time


def job():
    link = os.environ['APILINK']
    try:
        requests.get(link)
    except:
        None


if __name__ == "__main__":
    schedule.every(20).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(60)

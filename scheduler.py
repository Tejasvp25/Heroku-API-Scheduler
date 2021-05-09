import requests
import os
if __name__ == "__main__":
    link = os.environ['APILINK']
    requests.get(link)

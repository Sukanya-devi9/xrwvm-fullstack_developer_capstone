# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5000/"
)


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"
    request_url = backend_url + endpoint + "?" + params
    print("GET from {}".format(request_url))
    try:
        response = requests.get(request_url)
        return response.json()
    except:
        print("Network Exception occurred")


# Add code for get requests to back end


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    # Add code for retrieving sentiments
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Sentiment service returned {response.status_code}")
            return {"sentiment": "unknown"}
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return {"sentiment": "unknown"}


# def post_review(data_dict):
# Add code for posting review
def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")

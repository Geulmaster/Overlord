import requests
from Kingfish.Core import logger

connection_timeout = 4
headers = {"Content-Type": "application/json"}

def get(url, route: str, prms: dict = None):
    try:
        res = requests.get(url + route, params=prms, headers=headers, timeout=connection_timeout)
    except Exception as e:
        logger.fatal("Error getting " + route)
        logger.info(str(e))
    if res.status_code != 200:
        logger.fatal(f"Error getting {route} from server {str(res.status_code)}")
    else:
        logger.info("Got a response")
        logger.info(f"Successfully got {route} params: " + str(prms) if prms else "No params were sent")
        return res.content

def post(url, route: str, json: dict = None):
    try:
        res = requests.post(url + route, json, timeout=connection_timeout)
    except Exception as e:
        logger.fatal("Error getting " + route)
        logger.info(str(e))
    if res.status_code >= 400:
        logger.fatal(f"Error getting {route} from server {str(res.status_code)}")
    else:
        logger.info(f"post {route} - {res.status_code}")
        return res.content
import requests
from Kingfish.Core import logger

connection_timeout = 4

def get(url, route: str, prms: dict = None):
    try:
        res = requests.get(url + route, params=prms, timeout=connection_timeout)
    except Exception as e:
        logger.fatal("Error getting " + route)
        logger.info(str(e))
    if res.status_code != 200:
        logger.fatal(f"Error getting {route} from server {str(res.status_code)}")
    else:
        logger.info(f"Successfully got {route} params: " + str(prms) if prms else '')
        return res.content

def post(url, route: str, expected_status=201):
    try:
        res = requests.post(url + route, timeout=connection_timeout)
    except Exception as e:
        logger.fatal("Error getting " + route)
        logger.info(str(e))
    if res.status_code != expected_status:
        logger.fatal(f"Error getting {route} from server {str(res.status_code)}")
    else:
        logger.info(f"post {route} - {res.status_code}")
        return res.content
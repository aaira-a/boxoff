import requests

QUERY_URI = ("https://www.mbocinemas.com/GetMboData.ashx?js="
             "{%27Command%27:%27GETSESSIONTIMES%27,"
             "%27MovieName%27:%22VENOM%22,"
             "%27CinemaID%27:%271030%27,"
             "%27Time%27:%27%27}")


def query_endpoint(endpoint=QUERY_URI):
    try:
        response = requests.get(endpoint)
        return response.json()
    except:
        return "error"


def parse_response(response_json):
    match = False
    for date in response_json["Data"]:
        for session in date["Times"]:
            if session["SessionAttributes"].lower() == "KECIL".lower():
                match = True
    return match

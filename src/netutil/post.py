import urllib.request
import json
from builtins import print


def post(url: str, req_json: dict):
    json_dump = json.dumps(req_json, sort_keys=True, ensure_ascii=False, indent=2).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    request = urllib.request.Request(url, data=json_dump, headers=headers, method="POST")
    with urllib.request.urlopen(request) as response:
        response_body: str = response.read().decode("utf-8")
        result_dict: dict = json.loads(response_body)
        return result_dict
    pass


def generateTestJson() -> dict:
    reqJson: dict = {
        "nid": "xxxyycc",
        "userid": "uname",
        "seat": "101",
        "crid": "99366",
        "url": "https://yahoo.co.jp",
        "title": "sample   title",
        "media": "sample media",
        "image": "http//hogefuga.example.com/image/aaa.jpg",
        "domain": [
            "ab.bbb.com",
            "cd.bbb.com"
        ],
        "w": 300,
        "h": 400,
        "campaign": "5e33888",
        "country_id": "jp",
        "createdtime": "2020/07/10 01:37:32",
        "last_updated_time": "2020/07/10 01:37:32"
    }
    return reqJson


if __name__ == '__main__':
    req_json: dict = generateTestJson()
    url = 'http://localhost:8000/test?aaa=bbb&ccc=ddd'
    res_json = post(url=url, req_json=req_json)
    print(res_json)
    pass

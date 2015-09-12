import json
import urllib.request
from builtins import print
from typing import Dict


def post(url: str, req_json: dict) -> dict:
    json_dump = json.dumps(req_json, sort_keys=True, ensure_ascii=False, indent=2).encode("utf-8")
    headers: Dict[str, str] = {"Content-Type": "application/json"}
    request = urllib.request.Request(url, data=json_dump, headers=headers, method="POST")
    with urllib.request.urlopen(request) as response:
        response_body: str = response.read().decode("utf-8")
        result_dict: dict = json.loads(response_body)
        return result_dict


def get(url: str) -> dict:
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        response_body: str = response.read().decode("utf-8")
        result_dict: dict = json.loads(response_body)
        return result_dict


def generateTestJson() -> Dict[str, object]:
    reqJson: Dict[str, object] = {
        "name": "xxxyycc",
        "w": 300,
        "h": 400,
        "image": "http//hogefuga.example.com/image/aaa.jpg",
        "domain": [
            "ab.bbb.com",
            "cd.bbb.com"
        ],
        "obj": {
            "w": 9,
            "obj2": {
                "id": 3,
                "data": "hoge"
            },
            "array": [2, 9, 3]
        },
        "campaign": "5e33888",
        "country_id": "jp",
        "createdtime": "2020/07/10 01:37:32",
        "last_updated_time": "2020/07/10 01:37:32"
    }
    return reqJson


if __name__ == '__main__':
    url = 'http://localhost:8000/test?aaa=bbb&ccc=ddd'
    # post
    req_json: dict = generateTestJson()
    post_res_json = post(url=url, req_json=req_json)
    print(post_res_json)
    # get
    get_res_json = get(url)
    print(get_res_json)
    pass

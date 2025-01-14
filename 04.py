import requests
from pprint import pprint

BASE_URL = "https://api.themoviedb.org/3"
path = "/search/movie" 
params = {
    "api_key": "e89f1ac075fe652da53b26e8466adbac",
    "language": "ko-KR",
    "region": "KR",
    "query": "",
}

def search_movie(title):
    pass
    # 여기에 코드를 작성합니다.
    params["query"] = title
    response = requests.get(BASE_URL+path, params=params).json()
    responseList = response.get("results")
    if len(responseList) > 0:
        firstResponse = response.get("results")[0]
        return firstResponse.get("id")
    else:
        return("None")

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None

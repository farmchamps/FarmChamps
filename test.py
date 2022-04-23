import requests

url = "https://bing-news-search1.p.rapidapi.com/news/search"

querystring = {"q":"<REQUIRED>","freshness":"Day","textFormat":"Raw","safeSearch":"Off"}

headers = {
	"X-BingApis-SDK": "true",
	"X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com",
	"X-RapidAPI-Key": "f3b51317dbmshcb52d8d10c1c68cp144165jsnca4611583565"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
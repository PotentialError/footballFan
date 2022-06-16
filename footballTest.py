#Included in .gitignore so it will not be seen in repository
import privateVariables
import requests

url = "https://v3.football.api-sports.io/status"

headers = {
	"X-RapidAPI-Key": privateVariables.APIKey,
	"X-RapidAPI-Host": privateVariables.URL
}

response = requests.request("GET", url, headers=headers)

print(response.text)

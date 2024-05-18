import requests


header={
'shared_secret':'zTOhPP4N+u$$2Wtoazv2d-p$cO}Od0@MyDF1{E7F',


}


url="https://sandbox.api.visa.com/vdp/helloworld?apikey=<0S8T25YWNJWUN6CD27QH2190kfLtXwhpbnGFdkGuHK7mmX-ms>" 

response=requests.get(
    url=url
)

print(response.json)
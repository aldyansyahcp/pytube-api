# pytube-api
```
https://pytube-api.herokuapp.com/ytvideo-sound?url=link youtube
https://pytube-api.herokuapp.com/ytvideo-no-sound?url=link youtube
https://pytube-api.herokuapp.com/ytaudio-only?url=link youtube
```
## python requests
```
$from requests import get,post
$params = {"url":"youtube link"}
$get("https://pytube-api.herokuapp.com/ytvideo-sound", params=params).text
```

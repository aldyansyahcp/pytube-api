from pytube import YouTube as yt
import random, json
from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def hom():
    return render_template("index.html")

@app.route("/ytvideo-sound", methods=["GET", "POST"])
def yts():
        try:
            url = request.args.get("url")
            yu = yt(url)
            res=[]
            name = yu.title.replace(" ", "").replace(",","").replace("'","")
            [res.append(i) for i in yu.streams.filter(progressive=True)]
            print(len(res))
            if len(res) == 2:
                result = {
                    "status":True,
                    "title":name,
                    "msg":"berhasil",
                    "video-sound": {
                                    "144p":res[0].url+"&title="+name,
                                    "360p":res[1].url+"&title="+name
                                    }
                            }
            else:
                result = {
                    "status":True,
                    "title":name,
                    "msg":"berhasil",
                    "video-sound":{
                        "114p":res[0].url+"&title="+name,
                        "360p":res[1].url+"&title="+name,
                        "720p":res[2].url+"&title="+name
                    }
                }
        except Exception as e:
            result = {
                "status":False,
                "msg":"link-undefined",
                "error":str(e),
                "inLine":e.__traceback__.tb_lineno
                }
        return json.dumps(result, indent=4)
        

@app.route("/ytvideo-no-sound", methods=["GET", "POST"])
def ytnse():
        try:
            url = request.args.get("url")
            yu = yt(url)
            res= []
            name = yu.title.replace(" ","").replace(",","").replace("''","")
            [res.append(yu.streams.get_by_itag(130+i)) for i in range(3,8)]
            if None in res:
                result = {
                    "status":True,
                    "title":name,
                    "msg":"berhasil",
                    "video-no-sound": {
                        "240p":res[0].url+"&title="+name,
                        "360p":res[1].url+"&title="+name
                    }
                }
            else:
                result = {
                    "status":True,
                    "title":name,
                    "msg":"berhasil",
                    "video-no-sound":{
                        "144p":res[0].url+"&title="+name,
                        "240p":res[1].url+"&title="+name,
                        "480p":res[2].url+"&title="+name,
                        "720p":res[3].url+"&title"+name,
                        "1080p":res[4].url+"&title="+name
                    }
                }
        except Exception as e:
            #err = _except(line=sys.exc_info()[-1].tb_lineno, error=e, function_name=ytns(), script_name=__file__)
            result = {
                "status":False,
                "msg":"link-undefined",
                "error":str(e),
                "inLine":e.__traceback__.tb_lineno
            }
        return json.dumps(result, indent=4)
        
@app.route("/ytaudio-only", methods=["GET", "POST"])
def youtubevidnos():
    try:
        url = request.args.get("url")
        yu = yt(url)
        name = "&title="+yu.title.replace(" ","").replace(",","").replace("''","")
        res = []
        [res.append(i) for i in yu.streams.filter(only_audio=True)]
        if None in res:
            result ={
                "status":True,
                "title":yu.tilte,
                "msg":"Berhasil",
                "audio-only":{
                    "m4A":res[3].url+name,
                    "mp3":res[4].url+name
                }
            }
        else:
            result ={
                "status":True,
                "title":yu.title,
                "msg":"berhasil",
                "audio-only":{
                    "m4A":res[2].url,
                    "m4B":res[3].url+name,
                    "mp3":res[4].url+name
                }
            }
    except Exception as e:
        result ={
            "status":False,
            "msg":"link-undefined",
            "error":str(e),
            "inLine":e.__traceback__.tb_lineno
        }
    return json.dumps(result, indent=4)

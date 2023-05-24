import json
import logging
import os
import sys
import pyttsx3

import youtube_dl
from core import coreIo, titleSong
from flask import Flask, request, send_file, render_template
from include import randomPass as Pass
from include import AlfredRead as AR
from datetime import date, datetime

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)

os.system('python3 core/startIA.py')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/accueil")
def alfredAccueil():
    return render_template('accueil/accueil.html')


@app.route("/convert-youyoute")
def convertyouyoute():
    delet = coreIo.verif()
    print(delet)
    return render_template('convert/convert.html')


@app.route("/frame", methods=["GET", "POST"])
def frame():
    url = request.form['URL']
    if not coreIo.verifUrl(url):
        return render_template('convert/convert.html', div="choisir un lien youtube")

    return render_template('convert/download.html', div=str(url))


@app.route('/download_video', methods=["GET", "POST"])
def download_video():
    global verison, name
    path = ""
    youtube_url = request.form['URL']
    try:
        
        verison = request.form[
            'choix']  # je renomme la musique au nom de la musique et de l'app car un peu de pub ca mange pas de pain
        name = titleSong.titleDownload(youtube_url)  # je declare les options de telechargement
        ydl_opts = coreIo.choiseVerison(verison,
                                        name)  # je declare le lien de telechargement afin de retourner le fichier à l'utilisateur
        path = verison + "/" + name + '.' + verison
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
    except:
        return render_template('convert/convert.html', div="une erreur est survenue")
    # declaration pour telecharger le lien youtube avec la configuration desiré

    finally:
        return render_template('convert/complet.html', progress="Merci votre fichier " + verison, download=path,
                               name=name)


@app.route('/uploads', methods=['GET', 'POST'])
def download():
    path = request.form['path']
    return send_file(path, as_attachment=True)


@app.route('/translate', methods=['GET', 'POST'])
def translate():
    data = [{'idioma': 'es'}, {'idioma': 'en'}, {'idioma': 'it'}, {'idioma': 'de'}, {'idioma': 'fr'}, {'idioma': 'pt'}]

    return render_template('translate/translate.html', data=data)


@app.route('/translate_text', methods=['GET', 'POST'])
def traducir():
    data = [{'idioma': 'es'}, {'idioma': 'en'}, {'idioma': 'it'}, {'idioma': 'de'}, {'idioma': 'fr'}, {'idioma': 'pt'}]
    lenguaEn = request.form['idiomaIn']
    lenguaAfuera = request.form['idiomaOut']
    textoEn = request.form['TextATraduire']
    print("textoEn     " + str(textoEn))
    print("lenguaAfuera     " + str(lenguaAfuera))
    sResult = AR.traducirtexto(lenguaEn, lenguaAfuera, textoEn)

    return render_template('translate/translate.html', result=str(sResult), textoEn=str(textoEn), data=data)


@app.route("/generatorkey", methods=['GET', 'POST'])
def generatorkey():
    return render_template('keygenerator/randomPassword.html')


@app.route("/generator", methods=['GET', 'POST'])
def generator():
    identifiant = request.form['Identifiant']
    site = request.form['site']
    newKey = Pass.generateKey(site, identifiant)
    return render_template('keygenerator/randomConfirme.html', result=str(newKey['key']), id=str(identifiant), site=str(site))



@app.route("/saveKey", methods=['GET', 'POST'])
def toto():
    identifiant = request.form['Identifiant']
    site = request.form['site']
    randomKey = request.form['password']
    newKey = {"name": "site", "identifiant": "identifiant", "key": "randomKey", "datecreate": str(datetime.now())}

    if not Pass.saveKey(json.dumps(newKey)):
        return render_template('keygenerator/randomConfirme.html', message='Erreur password non enregisté' )
    return render_template('keygenerator/randomConfirme.html', message='nouveau password enregisté', result=str(newKey['key']), id=str(identifiant), site=str(site))

# result=str(newKey)
#os.system("flask run")

# set FLASK_APP=app.py
# set FLASK_ENV=development
app.run(host="0.0.0.0", port=5000, debug=True)

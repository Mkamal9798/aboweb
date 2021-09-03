import os
import requests
from requests.models import Response
from bottle import route, run, template, request, response, static_file, get, post
from datetime import datetime, timezone
import json
import pytz

@route('/sidebar')
def send_iframe_html():
    qs = request.query_string
    response.set_cookie('my_app_params', qs)
    return template('start', qs=qs)

@route('/js/<filename>')
def send_js(filename):
    return static_file(filename, root='static/js')

@get('/incident')
def show_tasks():
    return  '''
        <form action="/incident" method="post">
            <div>
                <label for="fname">ref Editeur:</label><br>
                <input name="refEditeur" type="text" value=808 size="25" /> <br>
                <label for="lname">ref Abonnement:</label><br>
                <input name="refAbonnements" type="text" size="25" /> <br>
                <label for="lname">date de début:</label><br>
                <input name="dateDebut" type="text" size="25" /> <br>
                <input type="submit">
            <div>
        </form> 
    '''

@post('/incident')
def show_tasks():
    header = {'Authorization': "Basic YWJvd2ViOg=='",'Connection':'keep-alive'}
    url_auth='https://portal.mahalo-app.io/oauth/token?username=help@tbsblue.com&password=2020&grant_type=password'
    r = requests.post(url_auth, headers=header)
    if r.status_code == 200:
        token = r.json()
        header2 = {'Authorization': 'Bearer {}'.format(token['access_token'])}
        refEditeur=request.forms.get('refEditeur')
        refAbonnements=request.forms.get('refAbonnements')
        dateDebut=request.forms.get('dateDebut') 
        url_post='https://api.mahalo-app.io/aboweb/editeur/808/incident?refEditeur='+ refEditeur +'&dateDebut='+ dateDebut +'&refAbonnements='+refAbonnements

        req = requests.post(url_post, headers=header2)
        if req.status_code == 200:
            incidents = req.json()
            nb=incidents["value"]["nombreCreation"]
            if nb == 0:
                msg="L'incident existe déjà"
            else :
                msg="L'incident est bien créé"
            print(incidents)
            return  template('list_incidents', list=[msg])
        else :
            print(req.status_code)

    else:
        msg = 'Problem with the request: {} {}'.format(r.status_code, r.reason)
        qs = request.get_cookie('my_app_params')
        return template('start', qs=qs, error_msg=msg)






@get('/action')
def show_tasks():
    return  '''
        <form action="/action" method="post">
            <div>
                <label for="fname">ref Editeur:</label><br>
                <input name="refEditeur" type="text" value=808 size="25" /> <br>
                <label for="lname">date de début:</label><br>
                <input name="dateDebut" type="text" size="25" /> <br>
                <input type="submit">
            <div>
        </form> 
    '''

@post('/action')
def show_tasks():
    header = {'Authorization': "Basic YWJvd2ViOg=='",'Connection':'keep-alive'}
    url_auth='https://portal.mahalo-app.io/oauth/token?username=help@tbsblue.com&password=2020&grant_type=password'
    r = requests.post(url_auth, headers=header)
    if r.status_code == 200:
        token = r.json()
        header2 = {'Authorization': 'Bearer {}'.format("87cfa004-69d2-4888-8af6-10635fc96129")}
        refEditeur=request.forms.get('refEditeur')
        url_post='https://api.mahalo-app.io/aboweb/editeur/68/action?refEditeur='+ refEditeur

        
        codeClient = 14449
        newAction = []
        newAction["codeClient"] = codeClient

        #Valeur possible : Courrier / Email / Tel / SMS / Notes / Ticket / Pige
        newAction["type"] = "Email" 
        newAction["object"] = "RELANCE EMAIL"
            
        date_time = datetime.utcnow().isoformat(timespec='seconds')
        date_time=date_time+".000"

        newAction["date"] = date_time


        heure = datetime.now(pytz.timezone('Europe/Paris'))
        heure=heure.isoformat()
        heure=heure[11:16]

        newAction["refEtat"] = 1 
        newAction["etatAction"] = "false" 
            
        newAction["rappel"] = "true"
        heure_rappel = datetime("2021-12-12 15:40",pytz.timezone('Europe/Paris'))
        heure_rappel=heure_rappel.isoformat()
        newAction["heureRappel"] = heure_rappel[11:16]


        date_rappel = datetime.utcnow().isoformat(timespec='seconds')
        date_rappel=date_rappel+".000"

        newAction["dateRappel"] = date_rappel
        newAction["utilRappel"] = "SandBox Trias " 
        newAction["rappelEmailAddress"] = "guillaume@trias.fr"
            
        newAction["etatRappel"] = 0 
        newAction["rappelEmail"] = 0 


        newAction["texte"] = "Texte du mail pour Tester l'action"


        req = requests.post(url_post, headers=header2,data=json.dumps(newAction))
        if req.status_code == 200:
            print("GOOD WORK")
        else :
            print(req.status_code)
            print(Response)

    else:
        msg = 'Problem with the request: {} {}'.format(r.status_code, r.reason)
        qs = request.get_cookie('my_app_params')
        return template('start', qs=qs, error_msg=msg)








    



@route('/suspension')
def show_tasks():
    header = {'Authorization': "Basic YWJvd2ViOg=='",'Connection':'keep-alive'}
    url_auth='https://portal.mahalo-app.io/oauth/token?username=help@tbsblue.com&password=2020&grant_type=password'
    r = requests.post(url_auth, headers=header)
    if r.status_code == 200:
        token = r.json()

        header2 = {'Authorization': 'Bearer {}'.format(token['access_token'])}
        url = 'https://api.mahalo-app.io/aboweb/editeur/808/suspension?refEditeur=808&maxResults=10'
        
        r = requests.get(url, headers=header2)
        if r.status_code == 200:
            incidents = r.json()
            return template('list_suspensions', list=incidents['value'])
        else:
            msg = 'Problem with the request: {} {}'.format(r.status_code, r.reason)
            qs = request.get_cookie('my_app_params')
            return template('start', qs=qs, error_msg=msg)
    else:
        print("Shit")
        msg = 'Problem with the request: {} {}'.format(r.status_code, r.reason)
        qs = request.get_cookie('my_app_params')
        return template('start', qs=qs, error_msg=msg)
if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
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
                <input name="dateDebut" type="date" size="25" /> <br>
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
                <input name="refEditeur" type="text" value=68 size="25" /> <br>

                <label for="fname">codeClient:</label><br>
                <input name="codeClient" type="text" value=14449 size="25" /> <br>
                
                <label for="fname">type:</label><br>
                <SELECT name="type0" size="1">
                    <OPTION>Email
                    <OPTION>Courrier
                    <OPTION>Tel
                    <OPTION>SMS
                    <OPTION>Notes
                    <OPTION>Ticket
                    <OPTION>Pige
                </SELECT> <br>


                <label for="lname">object:</label><br>
                <input name="object" type="text" value="RELANCE_EMAIL" size="25" /> <br>

                <label for="lname">dateRappel:</label><br>
                <input name="dateRappel" type="date" size="25" /> <br>
                
                <label for="lname">heureRappel:</label><br>
                <input name="heureRappel" type="time" size="25" /> <br>


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
        header2= {'Authorization': 'Bearer {}'.format(token['access_token']), 'Content-Type': 'application/json'}
        refEditeur=request.forms.get('refEditeur')
        codeClient=request.forms.get('codeClient')
        type0=request.forms.get('type0')
        object=request.forms.get('object')
        dateRappel=request.forms.get('dateRappel')
        heureRappel=request.forms.get('heureRappel')

        url_post='https://api.mahalo-app.io/aboweb/editeur/68/action?refEditeur='+ refEditeur
            
        date_time = datetime.utcnow().isoformat(timespec='seconds')
        date_time=date_time+".000"
        date_date = date_time


        heure = datetime.now(pytz.timezone('Europe/Paris'))
        heure=heure.isoformat()
        heure=heure[11:16]

        refEtat = 1 
        etatAction = False
            
        rappel = True
        utilRappel = "Test test " 
        rappelEmailAddress = "help@tbsblue.com"
            
        etatRappel = 0 
        rappelEmail = 0 


        texte = "Texte du mail pour Tester l'action"

        
        #dateRappel = datetime.strptime(dateRappel)
        #dateRappel.isoformat()
        #dateRappel=dateRappel+".000"
        #print(dateRappel)
        action_json={
                    "codeClient":codeClient,
                    "type":type0,
                    "object":object,
                    "date":date_date,
                    "heure":heure,
                    "refEtat":refEtat,
                    "etatAction":etatAction,
                    "rappel":rappel,
                    "dateRappel":dateRappel,
                    "heureRappel":heureRappel,
                    "utilRappel":utilRappel,
                    "rappelEmailAddress":rappelEmailAddress,
                    "etatRappel":etatRappel,
                    "rappelEmail":rappelEmail,
                    "texte":texte
                    }
        #print(action_json)
        req = requests.post(url_post, headers=header2,data=json.dumps(action_json))

        if req.status_code == 200 or 201:
            #response=req.json()
            #res=response["value"]
            #print(res)
            return '''
                    <div>
                        <label for="fname">Action bien Créé</label><br>
                    <div>
                '''

        else :
            print(req.status_code)

    else:
        msg = 'Problem with the request: {} {}'.format(r.status_code, r.reason)
        qs = request.get_cookie('my_app_params')
        return template('start', qs=qs, error_msg=msg)









@get('/suspension')
def show_tasks():
    return  '''
        <form action="/suspension" method="post">
            <div>
                <label for="fname">ref Abonnement:</label><br>
                <input name="refAbonnement" type="text" value=68 size="25" /> <br>
                                
                <label for="fname">ref Editeur:</label><br>
                <input name="refEditeur" type="text" value=68 size="25" /> <br>
                
                <label for="lname">date de début:</label><br>
                <input name="dateDebut" type="date" size="25" /> <br>

                <label for="lname">date de fin:</label><br>
                <input name="dateFin" type="date" size="25" /> <br>

                <label for="lname">refMotifSuspension :</label><br>
                <input name="refMotifSuspension " type="text" size="25" value=11 /> <br>

                <input type="submit">
            <div>
        </form> 
    '''
                   

@post('/suspension')
def show_tasks():
    header = {'Authorization': "Basic YWJvd2ViOg=='",'Connection':'keep-alive'}
    url_auth='https://portal.mahalo-app.io/oauth/token?username=help@tbsblue.com&password=2020&grant_type=password'
    r = requests.post(url_auth, headers=header)
    if r.status_code == 200:
        token = r.json()
        header2= {'Authorization': 'Bearer {}'.format(token['access_token']), 'Content-Type': 'application/json'}
        refAbonnement=request.forms.get('refAbonnement')
        refEditeur=request.forms.get('refEditeur')
        dateDebut=request.forms.get('dateDebut')
        dateFin=request.forms.get('dateFin')
        refMotifSuspension=request.forms.get('refMotifSuspension')

        url_post='https://api.mahalo-app.io/aboweb/editeur/68/suspension?refEditeur='+ refEditeur

        
            
        date_time = datetime.utcnow().isoformat(timespec='seconds')
        date_time=date_time+".000"
        date_date = date_time


        heure = datetime.now(pytz.timezone('Europe/Paris'))
        heure=heure.isoformat()
        heure=heure[11:16]


        suspension_json={
            "abonnements":[refAbonnement],
            "suspension":
                {
                "refMotifSuspension": refMotifSuspension,
                "dateDebut":dateDebut,
                "dateFin":dateFin
                }
            }
    
        
        #print(suspension_json)
        req = requests.post(url_post, headers=header2,data=json.dumps(suspension_json))
        response=req.json()
        print(response)
        if req.status_code == 200 or 201:
            print("Suspension bien créé")
            return '''
                    <div>
                        <label for="fname">Suspension bien Créé</label><br>
                    <div>
                '''

        else:
            msg = 'Problem with the request: {} {}'.format(r.status_code, r.reason)
            qs = request.get_cookie('my_app_params')
            return template('start', qs=qs, error_msg=msg)

    else:
        msg = 'Problem with the request: {} {}'.format(r.status_code, r.reason)
        qs = request.get_cookie('my_app_params')
        return template('start', qs=qs, error_msg=msg)







if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
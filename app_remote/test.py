from datetime import datetime, timezone
import json
import pytz

refAbonnement = 12905 

date_time = datetime.utcnow().isoformat(timespec='seconds')
date_time=date_time+".000"


dateDebut = datetime.utcnow().isoformat(timespec='seconds')
dateDebut = dateDebut+".000"

dateFin = datetime.utcnow().isoformat(timespec='seconds')
dateFin = dateFin+".000"


refMotifSuspension = 11 
	
	
listAbos = []
listAbos[] = refAbonnement
	

suspension = [
	"codeMotifSuspension" => refMotifSuspension,
	"dateDebut" => dateDebut->format('Y-m-d\TH:i:s.\0\0\0'),
	"dateFin" => dateFin->format('Y-m-d\TH:i:s.\0\0\0')
]
	
params = [
		"abonnements" = listAbos
		"suspension" = suspension
	]
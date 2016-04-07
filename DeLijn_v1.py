#http://docs.delijn.apiary.io/
#http://data.irail.be/DeLijn/Stations.about?name=ramsel

import ast
from urllib2 import Request, urlopen

#Stel hier de juiste halte in en het aantal vertrekkende verbindingen dat je wilt zien
HALTE = 109044
AANTAL_RESULTATEN = 10

halte_info_request = Request('https://www.delijn.be/rise-api-core/haltes/titel/{halte}'.format(halte=HALTE))
halte_info_response_body = urlopen(halte_info_request).read()
halte_info = ast.literal_eval(halte_info_response_body.replace("null", "None")) #halte_info is een dict die alle informatie bevat over HALTE

doorkomsten_info_request = Request('https://www.delijn.be/rise-api-core/haltes/vertrekken/{halte}/{aantal_resultaten}'.format(halte=HALTE, aantal_resultaten=AANTAL_RESULTATEN))
doorkomsten_info_response_body = urlopen(doorkomsten_info_request).read()
doorkomsten_info = ast.literal_eval(doorkomsten_info_response_body.replace("null","None")) #doorkomsten_info is een dict die  alle informatie ivm doorkomsten HALTE bevat

Lijnen = doorkomsten_info['lijnen'] #Lijnen is een list die dictionaries bevat met de info over vertrekkende verbindingen in HALTE

print '\033[91mDoorkomsten voor ', halte_info['omschrijvingLang'], ' - Huidige tijd: ',doorkomsten_info['huidigeTijd'],'\033[0m'
for i in range(0, len(Lijnen)):
        print '\033[1m',Lijnen[i]['vertrekTijd'], '\033[0m - ', Lijnen[i]['lijnNummerPubliek'], ' - ', Lijnen[i]['bestemming']

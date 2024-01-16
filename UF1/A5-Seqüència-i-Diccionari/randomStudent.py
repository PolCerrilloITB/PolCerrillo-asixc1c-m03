"""
Pol Cerrillo
16/01/2024
ASIXc1C M03 UF1
Descripció: Aleatòriament, el programa ha de triar un dels correus de
l'alumnat de classe. Que prèviament estaran emmagatzemats "hard code".
NO FER SERVIR la funció choice() del random: random.choice(...)
"""
import random
hard_core = (
    "juan.acosta.7e6@itb.cat",
    "hugo.arijon.7e7@itb.cat",
    "guim.ballve.7e7@itb.cat",
    "jan.cabaces.7e5@itb.cat",
    "sergio.cabello.7e5@itb.cat",
    "amritpal.singh.7e5@itb.cat",
    "roma.carbonell.7e7@itb.cat",
    "bernat.carol.7e5@itb.cat",
    "sandro.casanova.7e5@itb.cat",
    "pol.cerrillo.7e7@itb.cat",
    "franco.chavez.7e7@itb.cat",
    "jordi.chuquimarca.7e7@itb.cat",
    "oscar.cordoba.7e7@itb.cat",
    "engel.encarnacion.7e5@itb.cat",
    "gabriel.ghiorghita.7e7@itb.cat",
    "guillem.gonzalez.7e7@itb.cat",
    "alexey.lonskiy.7e7@itb.cat",
    "carlos.perez.7e7@itb.cat",
    "angela.plana.7e7@itb.cat",
    "victoria.ramos.7e7@itb.cat",
    "joel.reis.7e5@itb.cat",
    "gerard.ros.7e7@itb.cat",
    "teresa.rovira.7e7@itb.cat",
    "adriana.sanchez.7e7@itb.cat",
    "joel.sola.7e7@itb.cat",
    "cristian.taran.7e7@itb.cat",
    "albert.torres.7e7@itb.cat",
    "matteo.vilchez.7e6@itb.cat",
    "shawaiz.zahid.7e7@itb.cat",
    "adrian.zamora.7e7@itb.cat",
    "arnau.fernandez.7e4@itb.cat"
)
eleccio = random.randint(0, len(hard_core)-1)
print(hard_core[eleccio])
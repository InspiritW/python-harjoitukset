# Codebreaker

jonatan

tekstiseikkailu terminaaliin. käynnistys `python3 peli.py` tässä kansiossa

## idea

oot koodinmurtaja joka löytää arvoitustornin. arvoituksista saa kolikoita ja niillä voi ostaa juomia kaupasta. tornia voi myös tutkia ja löytää romua jonka voi kierrättää kolikoiksi

tavoite on avata tornin ovi. sen voi tehä kolmella tavalla

## kestävä kehitys

kierrätys, eli YK:n tavoite 12 (vastuullinen kuluttaminen). tornista löytyy romua (lasipullo, peltipurkki ja sanomalehti) ja ne kierrätetään eikä heitetä pois. juomapullotkin voi kierrättää. kierrätys on myös yks kolmesta reitistä niin se on oikeesti osa peliä

sopii myös lapsille, ei oo väkivaltaa tai muuta

## mitä peli osaa

- kysyy nimen ja iän alussa
- päävalikko (1-8): arvoitus, edistyminen, lopetus, kauppa, reppu, oven avaus, kierrätys ja tutkiminen
- arvoituksesta 3 kolikkoa ja jos käytät vihjeen niin 1
- juomat toimii oikeesti: kirjota `hint` niin hint potion antaa vihjeen ilman kolikkojen menetystä, `answer` näyttää vastauksen. juoma kuluu
- tallentuu tiedostoon `savegame.json` kun lopetat ja jatkuu siitä. voitettaessa tallennus poistuu
- jos tallennus on rikki niin alkaa vaan uus peli
- ruutu tyhjenee valikoiden välillä ettei terminaali täyty

## reitit

| reitti | mitä pitää tehä |
| --- | --- |
| riddle master | ratkaise kaikki 3 arvoitusta |
| merchant | osta hint potion ja answer potion eikä käytä niitä |
| recycler | löydä 3 romua tornista (ullakko, kellari, puutarha) ja kierrätä ne, ei tarvii arvoituksia |

## tiedostot

- `peli.py` pääohjelma ja funktiot
- `player.py` Player luokka
- `room.py` Room luokka
- `item.py` Item, Potion ja Scrap
- `intro.txt` ja `instructions.txt` tekstit jotka luetaan tiedostosta
- `savegame.json` tallennus, syntyy pelatessa

## muuta

arvoitukset on listassa `RIDDLES` ja yks funktio hoitaa kaikki. tiedostopolut toimii mistä vaan käynnistettynä

# Arkkitehtuurikuvaus

## Rakenne

Ohjelmassa on varsinainen koodi src tiedoston sisällä. Sprites sisältää erilaisten hahmojen kuten alustojen ja robot-hahmon toiminnallisuudet. Näiden hahmojen grafiikka haetaan assets tiedostosta. Nämä tiedostot sisältävät pelin toiminnalle tärkeitä luokkia, kuten GameLoop, Robot ja Level.

![65828A4C-57D4-48FA-82B2-E14F0F9D752D](https://user-images.githubusercontent.com/86207135/204646226-468fda0b-a99f-4e93-b3af-852ed7226077.JPEG)

## Käyttöliittymä

Ohjelmistossa on tällähetkellä vain yksi näkymä:

* Pelikenttä


## Sovelluslogiikka

Sovelluslogiikka sisältää useita luokkia. Näistä tärkeimmät tällähetkellä ovat renderer sekä game_loop. Luokat pyörittävät peliä.
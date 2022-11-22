# Ohjelmistotekniikka

## Tasohyppelypeli

Pygamella toteutetussa tasohyppelypelissä pelaaja hyppii liikkuvia tasoja/alustoja pitkin ylöspäin. Tarkoituksena on päästä mahdollisimman korkealle. Peli vaikeutuu mitä korkeammalle pelaaja pääsee. Hyppiessä pelaaja kohtaa esteitä, joihin voi kuolla tai pudota alemmas. Pelaaja voi myös saada lisäpisteitä ja korkeampia hyppyjä tietyiltä alustoilta.

## Dokumentaatiot

[vaatimusmäärittely](https://github.com/nicolaskivimaki/ot-harjoitustyo22/blob/master/tasohyppelypeli/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/nicolaskivimaki/ot-harjoitustyo22/blob/master/tasohyppelypeli/dokumentaatio/tuntikirjanpito.md)

[changelog](https://github.com/nicolaskivimaki/ot-harjoitustyo22/blob/master/tasohyppelypeli/dokumentaatio/changelog.md)


## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```


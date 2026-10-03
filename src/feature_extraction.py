
from src.mappings import (MUSICAL_FORMS, MUSICAL_GENRES, MUSICAL_INSTRUMENTS,
                          MUSICAL_GENRES_INSTRUMENTS, MODES, TEMPO_MARKINGS)
import numpy as np


def extract_form(text):
    for form in MUSICAL_FORMS:
        if form.lower() in text.lower():
            return MUSICAL_FORMS[form]
    return np.nan

def extract_extended_genre(row):
    text = row['title_subtitle']
    genre = row['genre']
    for extended_genre in MUSICAL_GENRES:
        if extended_genre.lower() in text.lower():
            return extended_genre

    return genre.capitalize()

def extract_instruments(row):
    text, genre, form = row.values
    instruments = ''
    for instrument in MUSICAL_INSTRUMENTS:
        if instrument.lower() in text.lower():
            if instruments == '':
                instruments = instrument.capitalize()

            else:
                instruments = instruments + ', ' + instrument.capitalize()

    if instruments != '':
        if form == 'Concerto':
            instruments = instruments + ', ' + 'Orchestra'

        return instruments
    else:
        return MUSICAL_GENRES_INSTRUMENTS[genre]


def extract_mode(text):
    for mode in MODES:
        if mode.lower() in text.lower():
            return mode

    return np.nan


def extract_tempo(text):
    for tempo in TEMPO_MARKINGS:
        if tempo.lower() in text.lower():
            return tempo

    return np.nan

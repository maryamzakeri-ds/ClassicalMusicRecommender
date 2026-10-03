import numpy as np

MUSICAL_FORMS = {
    'Symphony': 'Symphony',
    'Sinfonia': 'Symphony',
    'Symphonia': 'Symphony',
    'Symphonie': 'Symphony',
    'Symphonic': 'Symphony',
    'Sinfonietta': 'Symphony',

    'Concerto': 'Concerto',

    'Sonata': 'Sonata',
    'Sonatina': 'Sonata',
    'Sonatine': 'Sonata',

    'Fugue': 'Fugue',
    'Fuga': 'Fugue',
    'Fughetta': 'Fugue',

    'Toccata': 'Toccata',

    'Prelude': 'Prelude',
    'Prélude': 'Prelude',
    'Preludium': 'Prelude',
    'Preambulum': 'Prelude',
    'Praeambulum': 'Prelude',

    'Interlude': 'Interlude',

    'Invention': 'Invention',

    'Overture': 'Overture',
    'Ouverture': 'Overture',

    'Minuet': 'Minuet',
    'Menuet': 'Minuet',

    'Rondo': 'Rondo',
    'Rondeau': 'Rondo',

    'Suite': 'Suite',
    'Variation': 'Variations',
    'Partita': 'Partita',

    'Berceuse': 'Lullaby',
    'Lullaby': 'Lullaby',

    'Polka' : 'Polka',
    'Polonaise': 'Polonaise',
    'Étude': 'Etude',
    'Impromptu': 'Impromptu',
    'Ballade': 'Ballade',
    'Rhapsody': 'Rhapsody',
    'Scherzo': 'Scherzo',
    'Mazurka': 'Mazurka',
    'Nocturne': 'Nocturne',

    'Passacaglia': 'Passacaglia',
    'Passacaille' : 'Passacaglia',

    'Canon': 'Canon',
    'Canone': 'Canon',

    'Chaconne': 'Chaconne',
    'Chacony' : 'Chaconne',

    'Intermezzo': 'Intermezzo',
    'Intermezzi': 'Intermezzo',

    'Arabesque': 'Arabesque',

    'Sarabande': 'Sarabande',
    'Saraband': 'Sarabande',

    'Waltz': 'Waltz',
    'Valsa': 'Waltz',
    'Valse': 'Waltz',
    'Walzer': 'Waltz',

    'Serenade' : 'Serenade',
    'Serenata': 'Serenade',
    'Sérénade': 'Serenade',
    'Ständchen': 'Serenade',
    'Serenate': 'Serenade',

    'Romance': 'Romance',
    'Romances': 'Romance',
    'Romanze': 'Romance',
    'Romanzen': 'Romance',

    'Capriccio': 'Capriccio',
    'Caprice': 'Capriccio',
    'Caprizzio': 'Capriccio',

    'Fantasy': 'Fantasy',
    'Fantasia': 'Fantasy',
    'Fantasie': 'Fantasy',

    'Ordre': 'Ordre',

    'Quartet': 'Quartet',
    'Quintet': 'Quintet',
    'Trio': 'Trio',
    'Duo': 'Duet',
    'Duet': 'Duet'
 }

MUSICAL_GENRES = {
    'Passion': 'Voice',
    'Mass': 'Voice',
    'Oratorio': 'Voice',
    'Cantata': 'Voice',
    'Song' : 'Voice',
    'Salve Regina': 'Voice',
    'Stabat Mater': 'Voice',
    'Choral': 'Voice',
    'Musical': 'Voice, Orchestra',
    'Opera': 'Voice, Orchestra',
    'Operetta': 'Voice, Orchestra',
    'Lieder': 'Voice, Piano',
    'Lied': 'Voice, Piano',
    'Aria': 'Voice',
    'Ballet': 'Orchestra',
    'Incidental Music': np.nan,
}

MUSICAL_GENRES_INSTRUMENTS = {
    'Passion': 'Voice, Chorus, Orchestra',
    'Mass': 'Voice, Chorus, Orchestra',
    'Oratorio': 'Voice, Chorus, Orchestra',
    'Cantata': 'Voice, Chorus, Orchestra',
    'Song' : 'Voice, Piano',
    'Salve Regina': 'Voice, Chorus, Orchestra',
    'Stabat Mater': 'Voice, Chorus, Orchestra',
    'Choral': 'Chorus',
    'Musical': 'Voice, Chorus, Orchestra',
    'Opera': 'Voice, Chorus, Orchestra',
    'Operetta': 'Voice, Orchestra',
    'Lieder': 'Voice, Piano',
    'Lied': 'Voice, Piano',
    'Aria': 'Voice',
    'Ballet': 'Orchestra',
    'Incidental Music': np.nan,
    'Chamber': 'ChamberEnsemble',
    'Orchestral': 'Orchestra',
    'Vocal': 'Voice',
    'Keyboard': 'Piano',
    'Stage': np.nan
}

MUSICAL_INSTRUMENTS = ['Piano', 'Violin', 'Viola', 'Oboe', 'Flute', 'Clarinet', 'Strings', 'Winds', 'Brass',
                       'Percussion', 'Orchestra', 'Chorus', 'Guitar', 'Contrabass', 'Harpsichord', 'Cello',
]


MODES = ['Major', 'Minor', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Locrian']


TEMPO_MARKINGS = ['Largo', 'Lento', 'Adagio', 'Andante', 'Moderato', 'Allegretto', 'Allegro', 'Vivace',
                  'Presto', 'Prestissimo']
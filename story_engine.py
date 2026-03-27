import random
from data import genres, characters, settings, conflicts, plot_twists


def generate_story():

    genre = random.choice(genres)
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    twist = random.choice(plot_twists)

    story = f"""
Genre: {genre}

Story:

One day, {character} {setting}. Soon they {conflict}.

Everything seems impossible to solve {twist}

The journey changes them forever.
"""

    return story
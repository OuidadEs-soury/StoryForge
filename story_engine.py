import random
from data import characters, settings, conflicts, plot_twists, poem_lines


def generate_story(selected_genre):

    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    twist = random.choice(plot_twists)

    story = f"""
============================

Genre: {selected_genre}

One day, {character} {setting}.

Soon they {conflict}.

Nothing seems easy, every step feels uncertain.

In the end, everything changes {twist}

Their journey will be remembered forever.

============================
"""

    return story


def generate_poem():

    lines = random.sample(poem_lines, 4)

    poem = f"""
============================

A Generated Poem

{lines[0]}
{lines[1]}
{lines[2]}
{lines[3]}

============================
"""

    return poem
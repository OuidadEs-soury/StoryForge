import random
from data import characters, settings, conflicts, plot_twists, poem_lines


def generate_story(genre):

    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    twist = random.choice(plot_twists)

    story = f"""
==============================

Genre: {genre}

One day, {character} {setting}.

Soon they {conflict}.

Nothing seems easy and every decision has consequences.

In the end everything changes {twist}

==============================
"""

    return story


def generate_poem():

    lines = random.sample(poem_lines, 4)

    poem = f"""
==============================

Generated Poem

{lines[0]}
{lines[1]}
{lines[2]}
{lines[3]}

==============================
"""

    return poem
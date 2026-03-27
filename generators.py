import random
from data import character_roles, traits, world_types, world_events


def generate_character():

    role = random.choice(character_roles)
    trait1 = random.choice(traits)
    trait2 = random.choice(traits)

    character = f"""
==============================

Generated Character

Role: {role}
Traits: {trait1}, {trait2}

A {trait1} {role} known for being {trait2}.
Their story is still waiting to be written.

==============================
"""

    return character


def generate_world():

    world = random.choice(world_types)
    event = random.choice(world_events)

    description = f"""
==============================

Generated World

This world is {world}.

Currently it faces a major event:
{event}

Heroes and villains are rising.

==============================
"""

    return description
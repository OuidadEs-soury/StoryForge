from story_engine import generate_story, generate_poem
from generators import generate_character, generate_world
from file_manager import save_to_file
from data import genres
import random


def banner():

    print("""
========================================
            STORYFORGE PRO
      Story & Fantasy Generator
========================================
Author: Ouidad Es-Soury
----------------------------------------
""")


def choose_genre():

    print("\nChoose a genre:\n")

    for i, g in enumerate(genres):
        print(f"{i+1} - {g}")

    choice = input("\nSelect genre number: ")

    try:
        return genres[int(choice)-1]
    except:
        print("Invalid choice. Random genre selected.")
        return random.choice(genres)


def menu():

    while True:

        print("""

Choose an option

1 - Generate Story
2 - Generate Poem
3 - Generate Character
4 - Generate Fantasy World
5 - Exit

""")

        option = input("Select option: ")

        if option == "1":

            genre = choose_genre()
            result = generate_story(genre)

        elif option == "2":

            result = generate_poem()

        elif option == "3":

            result = generate_character()

        elif option == "4":

            result = generate_world()

        elif option == "5":

            print("Goodbye writer.")
            break

        else:

            print("Invalid option.")
            continue

        print(result)

        save = input("Save this result? (y/n): ")

        if save.lower() == "y":
            save_to_file(result)


def main():

    banner()
    menu()


if __name__ == "__main__":
    main()
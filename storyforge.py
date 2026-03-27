from story_engine import generate_story, generate_poem
from file_manager import save_to_file
from data import genres


def show_banner():

    print("""
====================================
            STORYFORGE
      Story & Poetry Generator
====================================
Author: Ouidad Es-Soury
------------------------------------
""")


def choose_genre():

    print("\nChoose a genre:\n")

    for index, genre in enumerate(genres):
        print(f"{index + 1} - {genre}")

    choice = input("\nSelect genre number: ")

    try:
        return genres[int(choice) - 1]
    except:
        print("Invalid choice. Using random genre.")
        import random
        return random.choice(genres)


def menu():

    while True:

        print("""

Choose an option:

1 - Generate Story
2 - Generate Poem
3 - Exit

""")

        choice = input("Select option: ")

        if choice == "1":

            genre = choose_genre()
            story = generate_story(genre)

            print(story)

            save = input("Save this story? (y/n): ")

            if save.lower() == "y":
                save_to_file(story)

        elif choice == "2":

            poem = generate_poem()

            print(poem)

            save = input("Save this poem? (y/n): ")

            if save.lower() == "y":
                save_to_file(poem)

        elif choice == "3":

            print("Goodbye writer.")
            break

        else:

            print("Invalid option.")


def main():

    show_banner()
    menu()


if __name__ == "__main__":
    main()
from story_engine import generate_story


def main():

    print("""
================================
        STORYFORGE
     Random Story Generator
================================
""")

    while True:

        input("Press ENTER to generate a story...")

        story = generate_story()

        print(story)

        again = input("\nGenerate another story? (y/n): ")

        if again.lower() != "y":
            print("Goodbye writer.")
            break


if __name__ == "__main__":
    main()
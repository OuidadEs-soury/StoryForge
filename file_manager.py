def save_to_file(text):

    with open("generated_texts.txt", "a") as file:
        file.write(text)
        file.write("\n\n")

    print("Saved to generated_texts.txt")
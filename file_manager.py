def save_to_file(text):

    with open("generated_content.txt", "a") as file:
        file.write(text)
        file.write("\n\n")

    print("Saved to generated_content.txt")
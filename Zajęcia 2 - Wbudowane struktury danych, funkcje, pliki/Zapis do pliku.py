file = open("text.txt", "wt")

print("Wprowadz tresc ktora chcesz zapisac do pliku\nWprowadz pusta wartosc, aby zakonczyc\n")

text_input = input(" > ")
while text_input != "":
    file.write(text_input + "\n")
    text_input = input(" > ")

print("\nPlik zapisany")

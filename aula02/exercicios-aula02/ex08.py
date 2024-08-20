letra = input("Digite uma letra: ").strip().lower()

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("Essa letra é uma vogal")
    case "b" | "c" | "d" | "f" | "g" | "h" | "j" | "k" | "l" | "m" | "n" | "p" | "q" | "r" | "s" | "t" | "v" | "w" | "x" | "y" | "z":
        print("Essa letra é uma consoante")
    case _:
        print("Resposta inválida, isso não é uma letra.")

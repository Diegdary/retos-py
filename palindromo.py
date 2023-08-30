frase = input("ingrese la frase a evaluar como palindromo\n").replace(" ","")
print("es palindromo" if frase==frase[::-1] else "no es palindromo")
import wikipedia

def buscar(tema):
    resultado = wikipedia.search(tema)
    return resultado


tema = input('What you want learn?')

print(buscar(tema))

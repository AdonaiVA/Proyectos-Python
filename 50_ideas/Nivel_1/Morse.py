

código_morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",".": ".-.-.-", ",": "-.-.--", "?": "..--..", "\"": ".-..-."}

texto_codificado = ""

mensaje = input("Cual es su mensaje?\n******:")

for i in mensaje:
    if i != "" and i.lower() in código_morse:
        texto_codificado += código_morse[i.lower()]
    else:
        texto_codificado += i

print("Texto codificado: {}".format(texto_codificado))

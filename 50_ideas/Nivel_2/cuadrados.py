class Cuadrados:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def hacer(self):
        primer_num = self.num_1
        segundo_num = self.num_2 + 1
        
        for i in range (primer_num, segundo_num):
            print(i, "--------------", i**2)   



ejercicio = Cuadrados(1,100)
print("Number ---------- Square")
ejercicio.hacer()
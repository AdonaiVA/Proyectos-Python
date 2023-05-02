class City:
    def __init__(self,name,country,population,landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

xalapa = City('Xalapa','México',443063,'Catedral del Centro')
nyc = City('New York City', 'EEUU',24000000,'The Empire State')
t = City('Tokio','Japón', 13095000, 'Sensoji-Temple')
deli = City('Delhi','India',13850507,'Templo del loto')

print(vars(xalapa))
print(vars(nyc))
print(vars(t))
print(vars(deli))
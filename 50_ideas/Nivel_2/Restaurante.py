class Restaurant:
    def __init__(self, name, type, rating, delivery):
      self.name = name
      self.type = type
      self.rating = rating
      self.delivery = delivery

tonys = Restaurant('Tonys Mariscos','mariscos',9.5,False)
bobs_burguers = Restaurant('Bob\'s Burguers','American Diner',4.7,False)

print(vars(tonys))
print(vars(bobs_burguers))
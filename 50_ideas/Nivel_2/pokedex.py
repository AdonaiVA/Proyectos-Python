class Pokemon:
    def __init__(self, entry, name, type, description, is_caught, sound, level, region, height, weight):
        self.entry = entry
        self.name = name
        self.type = type
        self.description = description
        self.is_caught = is_caught
        self.sound = sound
        self.level = level
        self.region = region
        self.height = height
        self.weight = weight

    def speak(self):
        print(self.sound)

bulbasaur = Pokemon(3, 'Venusaur','Grass & Posion','It uses the nutrients that are stored in the seed on its back in order to grow. The reception of Bulbasaur has been largely positive and it often appears in "top Pokémon lists"','Caught','SAAAAUURR', 'lvl 52','Kanto','2.0 m','200 kg')

magneton = Pokemon(82, 'Magenton','Electric & Steel','Formed when several Magnemites fuse together, it tends to raise the temperature up by 3.6°F within 3,600 ft. It generates strange radio signals and they tend to gather where sun flares happen. Earaches can occur if you get close to one. Its magnetism is so powerful it dries up moisture in its vicinity, and its fatal to devices if it were to go near one as devices like TVs will stop playing correctly. When many Magneton gather, it disrupts radio signals. As a result, large cities have sirens to warn their citizens of this occurrence and some even warn people to keep it inside their Pokeballs. When it evolves, their brains link up too, though they dont become three times smarter. When rain clouds form, they like to gather in high spots where lightning could strike. It seems that Sandy Shocks is a futuristic relative of it. It evolves into Magnezone while in range of a special magnetic field or a Thunder Stone in later games.','Caught','TTSSSSSS','lvl 41','Kanto','1.0 m', '60.0 kg')

Clefable = Pokemon(36,'Clefable','Fairy','It is rarely seen by people. Clefable walks around on moonlit nights, skipping lightly as if in flight, allowing it to walk on water. It has an extremely sharp sense of hearing; its sensitive ears allow it to detect a pin drop from a mile away.','Caught','I-I','lvl 50','Kanto','1.3 m', '40.0 kg')

print('-'*50)
print(vars(bulbasaur))
print('-'*50)
print(vars(Clefable))
print('-'*50)
print(vars(magneton))
print('-'*50)
bulbasaur.speak()
print('-'*50)
Clefable.speak()
print('-'*50)
magneton.speak()
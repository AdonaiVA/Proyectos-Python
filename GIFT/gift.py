
import imageio

filenames = ['team-pic1.png', 'team-pic2.png']
images = [ ]

for filename in filenames:
  images.append(imageio.imread(filename))

imageio.mimsave('team2.gif', images, duration = 0.5)
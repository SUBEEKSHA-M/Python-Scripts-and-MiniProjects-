#PIP Library
#PIP= PILLOW
#It is used to store, close, and work on that file

from PIL import Image

images = []
for filename in ["costume1.gif", "costume2.gif"]:
    image = Image.open(filename)
    images.append(image)

images[0].save(
    "costumes.gif",
    save_all=True,
    append_images=[images[1]],
    duration=20,
    loop=0
)

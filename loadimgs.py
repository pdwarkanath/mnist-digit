from mnist import MNIST
import random

mndata = MNIST()

images, labels = mndata.load_training()

index = random.randrange(0, len(images))
print(mndata.display(images[3]))
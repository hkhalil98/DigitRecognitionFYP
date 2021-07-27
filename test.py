import sys
import torch
import torchvision
import torchvision.datasets as datasets


# print(f"PyTorch Version: {torch.__version__}")

# mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)

mnist_testset = datasets.MNIST(root='./data', train=False, download=True, transform=None)

# print (len(mnist_trainset))
print (len(mnist_testset))
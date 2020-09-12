import torchvision
DATA_DIR = "/products/cifardata"
train_set_raw = torchvision.datasets.CIFAR10(root=DATA_DIR, train=True, download=True)
test_set_raw = torchvision.datasets.CIFAR10(root=DATA_DIR, train=False, download=True)

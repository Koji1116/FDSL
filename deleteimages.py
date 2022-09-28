import os
import shutil


for i in range(1000, 5000):
    os.remove(f'path_to_cifar10_1000/train/airplane/img{i}.jpeg')
    os.remove(f'path_to_cifar10_1000/train/automobile/img{i}.jpeg')
    os.remove(f'path_to_cifar10_1000/train/cat/img{i}.jpeg')
    os.remove(f'path_to_cifar10_1000/train/deer/img{i}.jpeg')
    os.remove(f'path_to_cifar10_1000/train/dog/img{i}.jpeg')
    os.remove(f'path_to_cifar10_1000/train/frog/img{i}.jpeg')
    os.remove(f'path_to_cifar10_1000/train/horse/img{i}.jpeg')
    os.remove(f'path_to_cifar10_1000/train/ship/img{i}.jpeg')
    os.remove(f'path_to_cifar10_1000/train/truck/img{i}.jpeg')
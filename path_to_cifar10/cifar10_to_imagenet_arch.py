from torchvision.datasets import CIFAR10
import cv2
from tqdm import tqdm
import os
from collections import defaultdict


class C10(CIFAR10):
    def __getitem__(self, index):
        img, target = self.data[index][:, :, ::-1], self.classes[self.targets[index]]
        return img, target


for tv in [True, False]:
    ds = C10("../training/datasets", train=tv)
    tv_name = {True: 'train', False: 'val'}[tv]
    count = defaultdict(int)
    for i in tqdm(range(len(ds))):
        d, t = ds[i]
        root = f"{tv_name}/{t}"
        file = f"img{count[t]}.jpeg"
        if not os.path.isdir(root):
            os.makedirs(root, exist_ok=True)
        cv2.imwrite(f"{root}/{file}", d)
        count[t] += 1

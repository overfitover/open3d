import os 
import time
import random
import numpy as np  
import torch
import torchvision.models
import torch.nn as nn
from torchvision import datasets, transforms
import hiddenlayer as hl 


history1 = hl.History()
canvas1 = hl.Canvas()

loss = 1
accuracy = 0

for step in range(800):
    loss -= loss*np.random.uniform(-0.09, 0.1)
    accuracy = max(0, accuracy+(1-accuracy) * np.random.uniform(-0.09, 0.1))

    if step % 10 == 0:
        history1.log(step, loss=loss, accuracy=accuracy)

        canvas1.draw_plot([history1["loss"], history1["accuracy"]])

        time.sleep(0.1)













































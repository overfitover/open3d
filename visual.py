import keras
from keras.applications.vgg19 import VGG19
from keras.preprocessing import image
from keras.applications.vgg19 import preprocess_input
from keras.models import Model
import numpy as np
import matplotlib.pyplot as plt


img_path = 'timg.jpeg'
img = image.load_img(img_path, target_size=(1026, 640))
plt.imshow(img)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
# plt.show()
print(x.shape)


base_model = VGG19(weights='imagenet',include_top=False)
# 获取各层的输出：
layer_outputs = [layer.output for layer in base_model.layers[2:20]]
# 获取各层的名称：
layer_names = []
for layer in base_model.layers[2:20]:
    layer_names.append(layer.name)
print(layer_names)


# 组装模型：
model = Model(inputs=base_model.input, outputs=layer_outputs)
# 将前面的图片数据x，输入到model中，得到各层的激活值activations：
activations = model.predict(x)
print(activations[0].shape)

import math
for activation,layer_name in zip(activations,layer_names):
    h = activation.shape[2]
    w = activation.shape[3]
    num_channels = activation.shape[1]
    cols = 16
    rows = math.ceil(num_channels/cols)
    img_grid = np.zeros((h*rows,w*cols))

    for c in range(num_channels):
        f_r = math.ceil((c+1)/cols)
        f_c = (c+1)if f_r==1 else (c+1-(f_r-1)*cols)
        img_grid[(f_r-1)*h:f_r*h,(f_c-1)*w:f_c*w ] = activation[0,:,:,c]


    plt.figure(figsize=(25,25))
    plt.imshow(img_grid, aspect='equal',cmap='viridis')
    plt.grid(False)
    plt.title(layer_name,fontsize=16)
plt.show()












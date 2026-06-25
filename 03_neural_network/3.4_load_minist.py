#sys：和 Python 解释器、导入路径有关；os：和操作系统、文件路径有关
import sys, os

#os.pardir, 上一级目录
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True)

print(x_train.shape) #(60000, 784)
print(t_train.shape) #(60000,)
print(x_test.shape) #(10000, 784)
print(t_test.shape) #(10000,)
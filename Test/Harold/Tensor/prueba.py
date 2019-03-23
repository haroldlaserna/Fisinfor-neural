import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#random_normal donde crea una matriz 2x20 la cual general numeros aleatorios de la funcion normal
a = tf.random_normal([2,20])
#Session crea una sesion que es un ambiente el cual hace los calculos
sess = tf.Session()
#run corre la operaccion dentro de la sesion creada
out =sess.run(a)
#se separan los datos para crearlo
x, y = out
# se grafican y vs x
plt.scatter(x, y)

plt.show()

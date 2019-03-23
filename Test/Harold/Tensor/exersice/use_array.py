import tensorflow as tf
import numpy as np

#iniciar algunos tensores usados en computacion
a = np.array([2, 3], dtype=np.int32)
b = np.array([4, 5], dtype=np.int32)

#usar tf.add para uniciar la operacion suma del tensor de rango 1
c = tf.multiply(a,b, name="my_add_op")
sess = tf.Session()
print(sess.run(c))

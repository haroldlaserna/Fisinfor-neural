import tensorflow as tf
import numpy as np

#crear un marcador de posicion:
#tal que los parametros que se le definen son:
# -tipo de valor=tf.int32
# -dimension y longitud de cada dimension=shape=[2]
# -el nombre a colocar= name="my_input"
a =tf.placeholder(tf.int32, shape=[2], name="my_input")

#usar el marcador de posicion en cualquier objeto tensor tal que
b = tf.reduce_prod(a,name="prod_b")
c = tf.reduce_sum(a,name="prod_b")

d = tf.add(b, c,name="add_d")

#generamos una sesion
sess = tf.Session()

#creamos un diccionario que este en "feed_dict"
#la clave: 'a', es el placeholder que queremos cambiar

#valor puesto al diccionario luego de la clave [5,3] de tipo int32
input_dict = {a: np.array([5,3], dtype=np.int32)}

#ahora obtenemos el valor de de introducioendo el placeholder con el diccionario antes definido
output = sess.run(d, feed_dict=input_dict)
print(output)

import tensorflow as tf

#se crea una variable que su valor inicial sea igual a 3
my_var = tf.Variable(3, name="my_variable")

#las variables pueden ser usadas en funciones y/o operaciones
add = tf.add(5,my_var)
mul = tf.multiply(3, my_var)

#para generar valores iniciales existen operadores de ayuda que se nombrara en las sigueintes lineas

# matriz de ceros donde el arreglo dentro de dicha operacion define el rango del tensor
#y la longitud de cada dimension
zeros = tf.zeros([2,2])

#vector con una longitud de 6 ceros
ones = tf.ones([6])

#un tensor de rango 3, cada dimension tiene una longitud de 3
#el cual se define por valores aleatorio uniformes entre el 0 y el 10
uniform = tf.random_uniform([3,3,3], minval=0, maxval=10)

#tensor de rengo 3 cada dimension tiene una longitud de 3
#el cual se define por valores aleatorias desde una distribucion normal
#con media = 0 y desviacion estandar de 2
normal = tf.random_normal([3,3,3], mean=0.0, stddev=2.0)

#tambien se puede definir una distribucion normal truncada
#esta distribucion no tomara valores debajo de 3.0 o superiores a 7.0
trunc = tr.truncated_normal([2, 2], mean=5.0, stddev=1.0)

#puedes introducion operaciones como valores iniciales de la siguiente manera
#dicha distribucion es tomada predeterminadamente como la media = 0.0 y sd=1.0
random_var = tf.Variable(tf.truncated_normal([2, 2]))

import tensorflow as tf
#SINTAXIS CORRECTA PARA AÑADIR OPERACIONES A GRAFICAS
#incluyendo la grafica predeterminada
g1 = tf.get_default_graph
g2 = tf.Graph

with g1.as_default():
    #insertar operaciones
    a = tf.add(2,3,name="add_1")

with g2.as_default():
    #insertar operacion
    b = tf.multiply(3,4; name="mult_2"):

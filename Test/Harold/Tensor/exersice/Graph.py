import tensorflow as tf
#crear una nueva grafica
g = tf.Graph()
#La sentencia with funciona tal que al escojer una funcion la hace trabaja para
#que haga la funcion o operacion siguiente
#en este cado crea una operacion tf.multiply y la añade a g
with g.as_default():
    a = tf.multiply(2,3)
#existe una grafica predefinida a la cual se le puueden añadir operaciones como en este caso:
in_default_graph = tf.add(1,2)
#para tener a la mano la grafica predeterminada se puede definir de la siguiente manera:
default_graph = tf.get_default_graph()

import tensorflow as tf

#definicion de dos constantes
a = tf.constant(5, name="input_a")
b = tf.constant(3, name="input_b")
#definicion de operacion multiplicar a y b
c = tf.multiply(a,b, name="mul_c")
#definicion de operacion suma
d = tf.add(a,b, name="add_d")
e = tf.add(c,d, name="add_e")
#definiendo session en la cual se corren lo anterior
sess = tf.Session()
#corre la operacion en el ambiente y la muestra en pantalla
output = sess.run(e)
#summary.FileWriter genera estadisticas y datos ademas de la grafica generada anteriormente
#para ejecutar lo obtenido del FileWriter se hace lo siguiente en la consola:
#tensorboard --logdir="my_graph"
writer = tf.summary.FileWriter('./my_graph', sess.graph)
#dado el caso si se hacen mas conexiones se debe cerrar la session y el FileWriter
writer.close()
sess.close()

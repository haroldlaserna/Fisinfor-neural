import tensorflow as tf

#para el caso de las variables necesita una funcion de activacion
#en este caso para activar todas las variables se define:
a = tf.Variable(3)
b = tf.Variable(4)

#activa variables
init = tf.initialize_all_variables()
sess = tf.Session()

#activar variables dentro session
sess.run(init)

#mostrar mostrar variables
output = sess.run([a, b])
sess.close()
#si se quiere iniciar solo ciertas variables se hace lo siguiente:
var1 = tf.Variable(0, name="initialize_me")
var2 = tf.Variable(1, name="no_initialize")
init = tf.initialize_variables([var1], name="init_var1")
sess1 =tf.Session()
sess1.run(init)
output1 = sess1.run(var1)
print(output1)
#si no se inicia una variable con el metodo anterior en la consola aparece un error
#de no uso de activacion de la variable

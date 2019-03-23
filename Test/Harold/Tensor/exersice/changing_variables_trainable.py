import tensorflow as tf
#para el cambio de variables se hace uso de la operacion Variable.assign() tal que:
my_var = tf.Variable(1)

#cuando se usan optimizadores tal que cambian los valores de las variables hay ciertas variables
#que no se quieren cambiar tal que se define una variable que no sea afectada por el
#optimizador de la siguiente manera:
not_trainable = ft.Variable(0, trainable=False)

#se crea ima operacion que multiplica la variable por 2 cada cierto tiempo cuando se corre en la session
my_var_times_two = my_var.assign(my_var * 2)

#se crea a operacion de iniciacion
init = tf.initialize_all_variables()

#se empieza una session
sess = tf.Session()

#se inicia la variables
sess.run(init)

#se multiplica la variable por 2 y se retorna
output = sess.run(my_var_times_two)
print(output)

#se multiplica de nuevo
output = sess.run(my_var_times_two)
print(output)

#se multiplica otra vez
output = sess.run(my_var_times_two)
print(output)

#para incrementar variables se usa los siguientes metodos
#incrementar mas 1
output = sess.run(my_var.assign_add(1))
print(output)

#decrementar menos 1
output = sess.run(my_var.assign_sub(1))
print(output)
sess.close()
#este metodo funcion para generar distintas variables con una variable para cada session tal que

my_var = tf.Variable(0)
init = tf.initialize_all_variables()

sess1 = tf.Session()
sess2 = tf.Session()

#Iniciar variables e incremetar 5 a la sesion 1
sess1.run(init)
output1 = sess1.run(my_var.assign_add(5))
print(output1)

#inicial variables e incrementar 2 a la sesion 3
sess2.run(init)
output2 = sess2.run(my_var.assign_add(2))
print(output2)

#tal que puedes incrementar las variables en sessiones difewrentes teniendo valores dinstintos
output1 = sess1.run(my_var.assign_add(5))
output2 = sess2.run(my_var.assign_add(2))
print("sesion1=",output1," sesion2=",output2)
#para reinicial las variables al valor inicial solo se vuelve a introducir en el codigo
sess1.run(init)

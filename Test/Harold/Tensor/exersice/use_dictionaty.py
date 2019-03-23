import tensorflow as tf

#crea operaciones
a = tf.add(2, 5)
b = tf.multiply(a,3)

#se crea una sesion
sess = tf.Session()

#se genera un diccionario del valor a remplazar
replace_dict = {a: 15}

#se corre la sesion con la operacion a generar, ademas remplaza el valor dentro de la operacion con el diccionario
#esto se hace con la el parametro feed_dict y luego igualandolo con el diccionario
output = sess.run(b, feed_dict=replace_dict)
print(output)
sess.close()
#es posible cerrar sesion de manera alternativa unicamente con la sentencia with
with tf.Session() as sess:
    output = sess.run(b)
    print(output)

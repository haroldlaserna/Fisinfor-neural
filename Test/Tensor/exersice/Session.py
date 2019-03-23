import tensorflow as tf

#se crean operaciones
a = tf.add(2,5)
b = tf.multiply(a,3)

#se genera una sesion con la grafica predeterminada
#los siguientes lineas de codigo son iguales
sess = tf.Session()
sess = tf.Session(graph=tf.get_default_graph())

#se hace la operacion dentro de la session
output = sess.run(b)
print(output)

#tambien es posible correr varias operaciones o tensores en una sesion tal que genera una matriz de numpy

output2 = sess.run([a,b])
print(output2)

#es posible cerrar sesion de manera alternativa unicamente con la sentencia with
with tf.Session() as sess:
    output = sess.run(b)
    print(output)

#tambien es posibnle correr directamente a una operacion o tensor de la siguiente manera

a = tf.constant(5)
b = tf.add(a,5)
sess = tf.Session()

with sess.as_default():
    const = a.eval()
    out = b.eval()
    print(const,out)

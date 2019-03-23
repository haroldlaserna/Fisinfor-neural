import tensorflow as tf
#definicion de constate

a = tf.constant([5,3],name="input")

#funcion reduce_prod para tensores de rango 1 [a,b,...,n]

b = tf.reduce_prod(a, name="product")
#funcion reduce_sum para tensores de rango 1 [a,b,...,n]
c = tf.reduce_sum(a, name="add_0")
#funcion add para tensores de rango 0, escalar
d = tf.add(b,c, name="add_1")

sess = tf.Session()
output = sess.run(d)
print("tu valor es ",output)

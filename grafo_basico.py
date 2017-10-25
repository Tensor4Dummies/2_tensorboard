#IMPORTACIÓN DE LIBRERIAS
import tensorflow as tf
import os

#QUITAR LOS MENSAJES DE AVISO
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#CREAR EL MODELO
#Entradas
x = tf.constant(5, dtype=tf.float32, name="x")
y = tf.Variable([3.5], dtype=tf.float32, name="y")
z = tf.placeholder(tf.float32, shape=(1), name="z")
#Operaciones (x*y+z)
mult = tf.multiply(x,y, name="mult")
suma = tf.add(mult,z, name="suma")

#INICIAR SESIÓN
with tf.Session() as sesion:

    #Iniciar variables
    init = tf.global_variables_initializer()
    sesion.run(init)

    #Ejecución operaciones
    for i in range(10):
        result_parcial =sesion.run(mult)
        resultado = sesion.run(suma, feed_dict={z:[i]})
        print("{}*{}+{}={}+{}={}".format(sesion.run(x), sesion.run(y), i, result_parcial,i,resultado))

    #Creación del grafo
    writer = tf.summary.FileWriter('/grafo_basico', sesion.graph)
    print("Guardados los datos para ver el grafo")
    writer.close()

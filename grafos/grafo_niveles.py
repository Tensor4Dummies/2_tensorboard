#IMPORTACIÓN DE LIBRERIAS
import tensorflow as tf
import os

#QUITAR LOS MENSAJES DE AVISO
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#CREAR EL MODELO
#Entradas
A = tf.constant([4], tf.int32, name='A')
B = tf.constant([5], tf.int32, name='B')
C = tf.constant([6], tf.int32, name='C')
x = tf.placeholder(tf.int32, name='x')

#CREAR OPERACIONES
#y1= Ax^2 + Bx + C
with tf.name_scope("Ecuacion_1"):
	Ax2 = tf.multiply(A, tf.pow(x, 2), name="Ax2")
	Bx = tf.multiply(B, x, name="Bx")
	y1 = tf.add_n([Ax2, Bx, C], name="suma1")

#y2 = A + Bx + Cx^2
with tf.name_scope("Ecuacion_2"):
    Bx = tf.multiply(B, x, name="Bx")
    Cx2 = tf.multiply(C, tf.pow(x, 2), name="Cx2")
    y2 = tf.add_n([A, Bx, Cx2], name="suma2")

#y = y1 + y2
with tf.name_scope("Suma_final"):
	y = y1 + y2

#INICIAR SESIÓN
with tf.Session() as sesion:

    #Ejecución operaciones
    for i in range(10):
        print ("Para x={} -->{}".format(i,sesion.run(y, feed_dict={x: [i]})))

    #Creación del grafo
    writer = tf.summary.FileWriter('/grafo_niveles', sesion.graph)
    print("Guardados los datos para ver el grafo")
    writer.close()

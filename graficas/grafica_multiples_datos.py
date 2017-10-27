#IMPORTACIÓN DE LIBRERIAS
import tensorflow as tf
import os

#QUITAR LOS MENSAJES DE AVISO
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#CREAR ENTRADAS
#Las variables inicializadas a 3
A = tf.Variable([3], dtype=tf.float32, name='A')
B = tf.Variable([-3], dtype=tf.float32, name='B')
#Los placeholders según la forma(shape) del tipo lista y largo desconocido(None)
x = tf.placeholder(tf.float32, shape=(None), name='x')
y = tf.placeholder(tf.float32, shape=(None), name='y')

#CREAR OPERACIONES
with tf.name_scope("y_calculada"):
    #y_calculada = A*x + B
    y_calculada = A * x + B
with tf.name_scope("Diferencia"):
    #Diferencia de cuadrados
    perdida =  tf.reduce_sum(tf.square(y_calculada - y))
with tf.name_scope("Optimizar"):
    #Optimización
    optimizador = tf.train.GradientDescentOptimizer(0.01)
    entrenamiento = optimizador.minimize(perdida)
with tf.name_scope("Grafica"):
    #Operaciones para la gráfica
    tf.summary.scalar('Diferencia', perdida)
    summary = tf.summary.merge_all()

#GENERAR LOS DATOS
x_entrenamiento = [1.01, 1.99, 3.02, 3.98]
y_entrenamiento = [0.02, -1.03, -1.99, -2.99]
x_test = [1.48, 1.75, 3.45, 3.59]
y_test = [0.36, -1.25, -1.42, -2.84]

#INICIAR SESIÓN
with tf.Session() as sesion:

    #Iniciar variables
    init = tf.global_variables_initializer()
    sesion.run(init)

    #Crear el escritor del log
    writer_entrenamiento = tf.summary.FileWriter('/grafica/entrenamiento', sesion.graph)
    writer_test = tf.summary.FileWriter('/grafica/test', sesion.graph)

    #Ejecución operaciones
    for i in range(200):
        sesion.run(entrenamiento, feed_dict={x: x_entrenamiento, y: y_entrenamiento})
        #Evaluar los datos
        summary_entrenamiento = sesion.run(summary,feed_dict={x: x_entrenamiento, y: y_entrenamiento})
        summary_test = sesion.run(summary,feed_dict={x: x_test, y: y_test})
        writer_entrenamiento.add_summary(summary_entrenamiento, i)
        writer_test.add_summary(summary_test, i)

    #Cerrar el escritor
    print("Guardados los datos para ver la gráfica")
    writer_entrenamiento.close()
    #writer_test.close()

    #Evaluar la precisión
    A_entren, B_entren, perd_entren = sesion.run([A,B,perdida], {x: x_entrenamiento, y: y_entrenamiento})
    print("Para los datos de entrenamiento - A: %s B: %s perdida: %s"%(A_entren, B_entren, perd_entren))
    A_test, B_test, perd_test = sesion.run([A,B,perdida], {x: x_test, y: y_test})
    print("Para los datos de test - A: %s B: %s perdida: %s"%(A_test, B_test, perd_test))

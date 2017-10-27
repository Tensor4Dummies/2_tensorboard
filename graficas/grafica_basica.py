#IMPORTACIÓN DE LIBRERIAS
import tensorflow as tf
import os

#QUITAR LOS MENSAJES DE AVISO
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#CREAR ENTRADAS
#Las variables inicializadas a 0
A = tf.Variable([0], dtype=tf.float32, name='A')
B = tf.Variable([0], dtype=tf.float32, name='B')
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
with tf.name_scope("grafica"):
    #Operaciones para la gráfica
    tf.summary.scalar('diferencia_actual', perdida)
    summary = tf.summary.merge_all()

#GENERAR LOS DATOS
x_entrenamiento = [1.01, 1.99, 3.02, 3.98]
y_entrenamiento = [0.02, -1.03, -1.99, -2.99]

#INICIAR SESIÓN
with tf.Session() as sesion:

    #Iniciar variables
    init = tf.global_variables_initializer()
    sesion.run(init)

    #Crear el escritor del log
    writer = tf.summary.FileWriter('/grafica_basica', sesion.graph)

    #Ejecución operaciones
    for i in range(200):
        sesion.run(entrenamiento, feed_dict={x: x_entrenamiento, y: y_entrenamiento})
        #diferencia_calculada = sesion.run(diferencia,feed_dict={x: x_entrenamiento, y: x_entrenamiento})
        perdida_calculada, summary_calculada = sesion.run([perdida,summary],feed_dict={x: x_entrenamiento, y: y_entrenamiento})
        writer.add_summary(summary_calculada, i)
        #print("Iteración {} diferencia {}".format(i,diferencia_calculada))

    #Cerrar el escritor
    print("Guardados los datos para ver la gráfica")
    writer.close()

    #Evaluar la precisión
    curr_A, curr_b, curr_loss = sesion.run([A,B,perdida], {x: x_entrenamiento, y: y_entrenamiento})
    print("A: %s B: %s perdida: %s"%(curr_A, curr_b, curr_loss))

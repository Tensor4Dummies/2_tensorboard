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
    leerA = tf.reduce_sum(A)
    leerB = tf.reduce_sum(B)
with tf.name_scope("Graficas"):
    #Operaciones para la gráfica
    tf.summary.scalar('diferencia_actual', perdida, collections=['diferencia'])
    tf.summary.scalar('a_actual', leerA, collections=['A'])
    tf.summary.scalar('b_actual', leerB, collections=['B'])
    summary_dif = tf.summary.merge_all('diferencia')
    summary_a = tf.summary.merge_all('A')
    summary_b = tf.summary.merge_all('B')

#GENERAR LOS DATOS
x_entrenamiento = [1.01, 1.99, 3.02, 3.98]
y_entrenamiento = [0.02, -1.03, -1.99, -2.99]

#INICIAR SESIÓN
with tf.Session() as sesion:

    #Iniciar variables
    init = tf.global_variables_initializer()
    sesion.run(init)

    #Crear el escritor del log
    writer_perdidas = tf.summary.FileWriter('/graficas/Perdidas', sesion.graph)
    writer_a = tf.summary.FileWriter('/graficas/A', sesion.graph)
    writer_b = tf.summary.FileWriter('/graficas/B', sesion.graph)

    #Ejecución operaciones
    for i in range(200):
        sesion.run(entrenamiento, feed_dict={x: x_entrenamiento, y: y_entrenamiento})
        #diferencia_calculada = sesion.run(diferencia,feed_dict={x: x_entrenamiento, y: x_entrenamiento})
        summary1,summary2,summary3 = sesion.run([summary_dif,summary_a,summary_b],feed_dict={x: x_entrenamiento, y: y_entrenamiento})
        #print(summary_calculada.get_summary_description(diferencia_actual))
        writer_perdidas.add_summary(summary1, i)
        writer_a.add_summary(summary2, i)
        writer_b.add_summary(summary3, i)
        #print("Iteración {} diferencia {}".format(i,diferencia_calculada))

    #Cerrar el escritor
    print("Guardados los datos para ver la gráfica")
    writer_perdidas.close()
    writer_a.close()
    writer_b.close()

    #Evaluar la precisión
    curr_A, curr_b, curr_loss = sesion.run([A,B,perdida], {x: x_entrenamiento, y: y_entrenamiento})
    print("A: %s B: %s perdida: %s"%(curr_A, curr_b, curr_loss))

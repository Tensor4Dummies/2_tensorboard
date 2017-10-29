#IMPORTACIÓN DE LIBRERIAS
import tensorflow as tf
import os

#QUITAR LOS MENSAJES DE AVISO
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#LEER IMAGENES
lista_img = ["snoopy1.jpg","snoopy2.jpg","snoopy3.jpg"]
cola_nombres = tf.train.string_input_producer(lista_img)
lector_img = tf.WholeFileReader()

#INICIAR SESIÓN
with tf.Session() as sesion:
    #Coordinar la carga de imágenes
    coordinador = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sesion, coord=coordinador)

    imagenes = []
    for i in range(len(lista_img)):
        nombre_fichero, fichero_imagen = lector_img.read(cola_nombres)
        #Generar el tensor de la imagen
        imagen = tf.image.decode_jpeg(fichero_imagen)
        imagen.set_shape((224, 224, 3))
        array_imagen = sesion.run(imagen)
        tensor_imagen = tf.stack(array_imagen)
        imagenes.append(tensor_imagen)

    #terminar el del coordinador
    coordinador.request_stop()
    coordinador.join(threads)

    #Convertir las imágenes en un tensor de dimensión 4
    tensor = tf.stack(imagenes)

    #Crear los datos para tensorboard
    writer = tf.summary.FileWriter('/imagenes', graph=sesion.graph)
    summary = sesion.run(tf.summary.image("imagenes", tensor))
    writer.add_summary(summary)
    writer.close()

<h1>Imágenes</h1>
<p>En esta parte no me voy a centrar en el tratamiento de imágenes ya que se habla de ello en el <a href="https://github.com/Tensor4Dummies/5_img_mnist">repositorio</a>, así que sólo quier destacar que a partir del tensor de la imagen, puedo visualizar los datos a partir de:</br>
<pre style='display:inline'><i>writer = tf.summary.FileWriter('/imagenes', graph=sesion.graph)</br>
summary = sesion.run(tf.summary.image("imagenes", tensor))</br>
writer.add_summary(summary)</br>
writer.close()</i></pre></p>
<p>Tras la ejecución del fichero <a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/imagenes/imagenes.py">imagenes.py</a> con las imágenes <a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/imagenes/snoopy1.jpg">snoopy1.jpg</a>, <a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/imagenes/snoopy2.jpg">snoopy2.jpg</a> y <a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/imagenes/snoopy3.jpg">snoopy3.jpg</a>; la visualización en tensorboard es:</br>
<img src="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/imagenes/imagenes.JPG" alt="Grafo básico"></p>

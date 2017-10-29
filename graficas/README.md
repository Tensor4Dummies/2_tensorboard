<h1>Gráficas</h1>

<h2>Gráfica básica</h2>
<p>Para general una gráfica que muestre un dato concreto, en este caso la diferencia en las distintas transiciones, se realiza añadiendo:</br>
<li>with tf.name_scope("grafica"):</br>
<pre style='display:inline'>& # 0 9 ;</pre>#Operaciones para la gráfica</br>
<pre style='display:inline'>& # 0 9 ;</pre> tf.summary.scalar('diferencia_actual', perdida)</br>
<pre style='display:inline'>& # 0 9 ;</pre> summary = tf.summary.merge_all()</br></li>
en la parte de operaciones.</p>
<p>Y después en la parte de ejecución de las operaciones:</br>
<i>summary_calculada = sesion.run(summary,feed_dict={x: x_entrenamiento, y: y_entrenamiento}) </br>
writer.add_summary(summary_calculada, i)</br></i>
ejecutamos las operaciones y se las añadimos al writer.</p>
<p>Al ejecutar el fichero <a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/graficas/grafica_basica.py">grafica_basica.py</a> obtenemos:</br>
<i>Guardados los datos para ver la gráfica</br>
A: [-0.96660411] B: [ 0.90242046] perdida: 0.0116561</i></p>
<p>Y al abrir tensorboard en el grafo que muestra las operaciones, encontraremos:</br>
<img src="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/graficas/grafica_basica_grafo.JPG"></br>
y en la gráfica (Scalar):
<img src="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/graficas/grafica_basica_grafica.JPG"></p>

<h2>Múltiples gráficas</h2>
<p>Si lo que queremos es mostrar varias gráficas, para el ejemplo anterior queremos que no sólo se muestre la diferencia, sino también como cambian las variables A y B.</p>
<p>En la parte de operaciones, para el valor de tf.name_scope("Graficas") tendremos:</br>
<i>tf.summary.scalar('diferencia_actual', perdida, collections=['diferencia'])</br>
tf.summary.scalar('a_actual', leerA, collections=['A'])</br>
tf.summary.scalar('b_actual', leerB, collections=['B'])</br>
summary_dif = tf.summary.merge_all('diferencia')</br>
summary_a = tf.summary.merge_all('A')</br>
summary_b = tf.summary.merge_all('B')</i></br>
que cómo queremos 3 gráfica, tenemos 3 funciones de summary, y al utilizar merge_all sólo nos referimos a la colección del scalar al que queremos hacer referencia.</p>
<p>Lo mismo nos ocurre con los escritores de los datos, tendremos 3:</br>
<i>writer_perdidas = tf.summary.FileWriter('/graficas/Perdidas', sesion.graph)</br>
writer_a = tf.summary.FileWriter('/graficas/A', sesion.graph)</br>
writer_b = tf.summary.FileWriter('/graficas/B', sesion.graph)</i></p>
<p>Y la misma situación en la ejecución de las operaciones:</br>
<i>summary1,summary2,summary3 = sesion.run([summary_dif,summary_a,summary_b],feed_dict={x: x_entrenamiento, y: y_entrenamiento})</br>
writer_perdidas.add_summary(summary1, i)</br>
writer_a.add_summary(summary2, i)</br>
writer_b.add_summary(summary3, i)</i></p>
<p>Al ejecutar el fichero <a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/graficas/multiples_graficas.py">multiples_graficas.py</a> obtenemos:</br>
<i>Guardados los datos para ver la gráfica</br>
A: [-0.8534987] B: [ 0.5704748] perdida: 0.133711</i></p>
<p>Y al abrir tensorboard en la parte de gráficas encontraremos:</br>
<img src="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/graficas/multiples_graficas.JPG"></p>

<h2>Gráfica con varios datos</h2>
<p>En esta ocasión queremos comparar la diferencia para los datos de entrenamiento y test viéndolo en una única gráfica. En las operaciones, sólo tendremos el caso básico para escribir un dato. Sin embargo, en los writer tenemos 2:</br>
<i>writer_entrenamiento = tf.summary.FileWriter('/grafica/entrenamiento', sesion.graph)</br>
writer_test = tf.summary.FileWriter('/grafica/test', sesion.graph)</i></br>
lo que haremos son subcarpetas, que proporcionan una visión de dos variables con nombres "entrenamiento" y "test".</p>
<A la hora de escribir los datos en estos writers tendremos que ejecutar la operación de summary para los datos de entrenamiento y luego para los de test, y añadirlos a su correspondiente writer.</p>
<p>Tras ejecutar el fichero <a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/graficas/grafica_multiples_datos.py">grafica_multiples_datos.py</a> obtenemos:</br>
<i>Guardados los datos para ver la gráfica</br>
Para los datos de entrenamiento - A: [-0.8534987] B: [ 0.5704748] perdida: 0.133711</br>
Para los datos de test - A: [-0.8534987] B: [ 0.5704748] perdida: 2.24532</i></p>
<p>Y al abrir tensorboard en la parte de gráficas encontraremos:</br>
<img src="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/graficas/grafica_multiples_datos.JPG"></p>

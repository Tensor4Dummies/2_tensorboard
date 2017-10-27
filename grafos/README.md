<h1><a name="grafo"></a>Grafos</h1>
<h2>Un grafo b�sico</h2>
En el ejemplo <a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/grafos/grafo_basico.py">grafo_basico.py</a> se realiza la operaci�n
<i>x * y +z</i>, siendo "x" una constante, "y" una variable y "z" un placeholder. Al visualizar el grafo m�s adelante veremos que no se representan
 igual, sobre todo destacar que todos los placeholder se indican en la esquina izquierda superior para inicializar.</p>
<p>Lo �nico que hemos a�adido en diferencia a un programa especial es:</br>
<i>writer = tf.summary.FileWriter('/grafo_basico', sesion.graph)</br>writer.close()</i></br>
que se encarga de escribir un fichero en la ruta "/grafo_basico" con los datos, y luego se cierra con close().</p>
<p>Para ver tensorboard, que se instala con tensorflow, s�lo tendremos que ejecutar el fichero de python, en este caso
<a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/grafos/grafo_basico.py">grafo_basico.py</a>, que devuelve:</br>
<i>5.0*[ 3.5]+0=[ 17.5]+0=[ 17.5]</br>
5.0*[ 3.5]+1=[ 17.5]+1=[ 18.5]</br>
5.0*[ 3.5]+2=[ 17.5]+2=[ 19.5]</br>
5.0*[ 3.5]+3=[ 17.5]+3=[ 20.5]</br>
5.0*[ 3.5]+4=[ 17.5]+4=[ 21.5]</br>
5.0*[ 3.5]+5=[ 17.5]+5=[ 22.5]</br>
5.0*[ 3.5]+6=[ 17.5]+6=[ 23.5]</br>
5.0*[ 3.5]+7=[ 17.5]+7=[ 24.5]</br>
5.0*[ 3.5]+8=[ 17.5]+8=[ 25.5]</br>
5.0*[ 3.5]+9=[ 17.5]+9=[ 26.5]</br>
Guardados los datos para ver el grafo</i></br>
y despu�s en la ruta que hayamos puesto, en mi caso en la memoria b�sica, ejecutar:</br>
<i>tensorboard --logdir="grafo_basico"</i></br>
donde "grafo_basico" se refiere a la carpeta donde hemos creado los ficheros y devolver� algo as�:</br>
<i>TensorBoard 0.1.8 at http://0.0.0.0:6006 (Press CTRL+C to quit)</i></br>
S�lo tendremos que abrir el navegador en la ruta indicada y se ver� algo as�:</br>
<img src="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/grafos/grafo_basico.JPG" alt="Grafo b�sico"></p>

<h2>Grafos con niveles</h2>
<p>Otra cosa muy interesante que nos permiten los grafos de Tensorboard es agrupar para la visualizaci�n y trabajo.
Como ejemplo tenemos <a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/grafos/grafo_niveles.py">grafo_niveles.py</a> en el que queremos realizar la operaci�n <i>(Ax^2 + Bx + C)+(A + Bx + Cx^2)</i>, en la que va variando la x. Pero para simplificar lo convertimos en <i>y1+y2</i>, donde <i>y1=(Ax^2 + Bx + C)</i> e <i>y2=(A + Bx + Cx^2)</i>.</p>
<p>�sto es conocido como name_scope y se realiza a�adiendo: </br>
<i>with tf.name_scope("Ecuacion_1"):</i></br>
previamente a las operaciones que queremos incluir dentro de ese nombre. Por lo tanto al abrir la visualizaci�n ser�a:</br>
<img src="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/grafos/grafo_niveles_inicial.JPG" alt="Grafo b�sico"></p>
<p>Podemos agrandar cada una de las funciones creadas para ver su interior, quedando as�:</br>
<img src="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/grafos/grafo_niveles_visible.JPG" alt="Grafo b�sico"></p>
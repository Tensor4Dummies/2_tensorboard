<h1>Tensorboard</h1>
<p>Herramienta de TensorFlow para la visualización y mejor entendimiento del funcionamiento del programa creado.
Entre todos los datos que nos permite mostrar, la más interesante son los <a href="#grafo">grafos</a> que muestra el curso del programa creado.
Pero tenemos otras como: <a href="#grafica">gráficas</a>, <a href="#imagen">imágenes</a> o <a href="#histograma">histogramas</a>.</p>

<h2><a name="grafo"></a>Grafos</h2>
En el ejemplo <a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/grafo_basico.py">grafo_basico.py</a> se realiza la operación
<i>x * y +z</i>, siendo "x" una constante, "y" una variable y "z" un placeholder. Al visualizar el grafo más adelante veremos que no se representan
 igual, sobre todo destacar que todos los placeholder se indican en la esquina izquierda superior para inicializar.</p>
<p>Lo único que hemos añadido en diferencia a un programa especial es:</p>
<p><i>writer = tf.summary.FileWriter('/grafo_basico', sesion.graph)</br>writer.close()</i></p>
<p>que se encarga de escribir un fichero en la ruta "/grafo_basico" con los datos, y luego se cierra con close().</p>
<p>Para ver tensorboard, que se instala con tensorflow, sólo tendremos que ejecutar el fichero de python, en este caso
<a href="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/grafo_basico.py">grafo_basico.py</a>, que devuelve:</p>
<p><i>5.0*[ 3.5]+0=[ 17.5]+0=[ 17.5]</br>
5.0*[ 3.5]+1=[ 17.5]+1=[ 18.5]</br>
5.0*[ 3.5]+2=[ 17.5]+2=[ 19.5]</br>
5.0*[ 3.5]+3=[ 17.5]+3=[ 20.5]</br>
5.0*[ 3.5]+4=[ 17.5]+4=[ 21.5]</br>
5.0*[ 3.5]+5=[ 17.5]+5=[ 22.5]</br>
5.0*[ 3.5]+6=[ 17.5]+6=[ 23.5]</br>
5.0*[ 3.5]+7=[ 17.5]+7=[ 24.5]</br>
5.0*[ 3.5]+8=[ 17.5]+8=[ 25.5]</br>
5.0*[ 3.5]+9=[ 17.5]+9=[ 26.5]</br>
Guardados los datos para ver el grafo</i></p>
<p>y después en la ruta que hayamos puesto, en mi caso en la memoria básica, ejecutar:</p>
<p><i>tensorboard --logdir="grafo_basico"</i></p>
<p>donde "grafo_basico" se refiere a la carpeta donde hemos creado los ficheros y devolverá algo así:</p>
<p><i>TensorBoard 0.1.8 at http://0.0.0.0:6006 (Press CTRL+C to quit)</i></p>
</p>Sólo tendremos que abrir el navegador en la ruta indicada y se verá algo así:</p>
<p><img src="https://github.com/Tensor4Dummies/2_tensorboard/blob/master/grafo_basico.jpg" alt="Grafo básico"></p>

<h2><a name="grafica"></a>Gráficas</h2>

<h2><a name="imagen"></a>Imágenes</h2>

<h2><a name="histograma"></a>Histogramas</h2>

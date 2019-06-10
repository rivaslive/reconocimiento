PASOS PARA INSTALACION


1- Tener instalado python 3.7.3 o la ultima version en la pagina oficial
2- desinstalar versiones anteriores de puthon, dejar solo la ultima
3- Ejecuta los siguientes comandos pip, tal y como se muestran en orden, si alguno da error no pasar al siguiente hasta solucionarlo:
    
 	ABRIR CMD COMO ADMINISTRADOR y EJECUTAR:
	
	pip install --upgrade pip
	pip install --upgrade setuptools
	pip install flask
	pip install flask-socketio
	pip install flask-cors
	pip install numpy
	pip install opencv-contrib-python


4- Entrena al programa con un rostro para poder reconocerlo

	python capture.py NOMBRE_DE_LA_PERSONA
	
5- verifica que esta registrada
	
	python sockets.py

6- Estpera que se inicie el server y accede a la url

	http://localhost:8585/

y disfruta
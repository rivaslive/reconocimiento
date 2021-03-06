#OpenCV module
import cv2
#Modulo para leer directorios y rutas de archivos
import os
#OpenCV trabaja con arreglos de numpy
import numpy
 
import threading

#from usuarios import reconocido, desconocido
#Se importa la lista de personas con acceso al laboratorio

def recorrer():
    # Parte 1: Creando el entrenamiento del modelo
    print('Formando...')

    #Directorio donde se encuentran las carpetas con las caras de entrenamiento
    dir_faces = 'att_faces/orl_faces'

    #Tamaño para reducir a miniaturas las fotografias
    size = 4

    # Crear una lista de imagenes y una lista de nombres correspondientes
    (images, lables, names, id) = ([], [], {}, 0)
    for (subdirs, dirs, files) in os.walk(dir_faces):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(dir_faces, subdir)
            for filename in os.listdir(subjectpath):
                path = subjectpath + '/' + filename
                lable = id
                images.append(cv2.imread(path, 0))
                lables.append(int(lable))
            id += 1
    (im_width, im_height) = (112, 92)

    # Crear una matriz Numpy de las dos listas anteriores
    (images, lables) = [numpy.array(lis) for lis in [images, lables]]
    # OpenCV entrena un modelo a partir de las imagenes
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(images, lables)


    # Parte 2: Utilizar el modelo entrenado en funcionamiento con la camara
    face_cascade = cv2.CascadeClassifier( 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)


    prediccion = 0
    error = 0
    for e in range(0, 30):
        #leemos un frame y lo guardamos
        rval, frame = cap.read()
        frame=cv2.flip(frame,1,0)

        #convertimos la imagen a blanco y negro    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #redimensionar la imagen
        mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

        """buscamos las coordenadas de los rostros (si los hay) y
        guardamos su posicion"""
        faces = face_cascade.detectMultiScale(mini)
        
        for i in range(len(faces)):
        #for i in  range(0, 30):
            face_i = faces[i]
            (x, y, w, h) = [v * size for v in face_i]
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (im_width, im_height))

            # Intentado reconocer la cara
            prediction = model.predict(face_resize)
                
            #Dibujamos un rectangulo en las coordenadas del rostro
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                
            # Escribiendo el nombre de la cara reconocida
            # La variable cara tendra el nombre de la persona reconocida
            cara = '%s' % (names[prediction[0]])

            #Si la prediccion tiene una exactitud menor a 100 se toma como prediccion valida
            if prediction[1]<90:
                #Ponemos el nombre de la persona que se reconoció
                cv2.putText(frame,'%s - %.0f' % (cara,prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
                prediccion += 1
                #En caso de que la cara sea de algun conocido se realizara determinadas accione          
                #Busca si los nombres de las personas reconocidas estan dentro de los que tienen acceso          
                #flabs.TuSiTuNo(cara)

            #Si la prediccion es mayor a 100 no es un reconomiento con la exactitud suficiente
            elif prediction[1]>90 and prediction[1]<500:    
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)       
                #Si la cara es desconocida, poner desconocido
                cv2.putText(frame, 'Desconocido',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 0, 255))  
                error += 1
                #desconocido()
            #Mostramos la imagen
            #cv2.imshow('OpenCV Reconocimiento facial', frame)

        #Si se presiona la tecla ESC se cierra el programa
        key = cv2.waitKey(10)
        if key == 27:
            cv2.destroyAllWindows()
            break

    if prediccion > error:
        #the = threading.Thread(target=reconocido)
        #the.start()
        print("RECONOCIDO")
        return "1"
    else:
        #the = threading.Thread(target=desconocido)
        #the.start()
        print("Desconocido")
        return "0"
if __name__ == '__main__':
    recorrer()
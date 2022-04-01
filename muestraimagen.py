# mostrar imagen de camara usando opencv y copilot
# importar librerias
import cv2
#leer camara
cap = cv2.VideoCapture(0)
#leer imagen
ret, frame = cap.read()
#mostrar imagen
cv2.imshow('frame', frame)
# quitamos el loop
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    cap.release()   
# fin pruebacopilot.py

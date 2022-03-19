import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write

#Formato de audio
frecuencia_muestreo=44100
canales=1
profundidad_bits='float64'

duracion=5.3

grabacion= sd.rec(int(duracion* frecuencia_muestreo), samplerate=frecuencia_muestreo, channels=1, dtype=profundidad_bits)

print("Comienza grabación")
sd.wait()
print("Grabación completa")

tiempos=np.linspace(0.0, duracion,len(grabacion))

plt.figure()
plt.plot(tiempos, grabacion)
plt.show()

print("Shape: "+ str(grabacion.shape))
print("dtype: "+ str(grabacion.dtype))

sd.play(grabacion, frecuencia_muestreo)
print("Comienza reproducción")
sd.wait()
print("Reproducción completa")
grabacion_formato=(grabacion*np.iinfo(np.int16).max).astype(np.int16)

write("grabacion.wav", frecuencia_muestreo, grabacion_formato)

transformada=np.fft.rfft(grabacion[:,0])
#frecuencias=np.fft.rfftfreq(len(transformada), 1.0/frecuencia_muestreo)

fig, ejes=plt.subplots(1,2)

ejes[0].plot(tiempos, grabacion)
ejes[1].plot(np.abs(transformada))


if frecuencia_fundamental >= 324  and frecuencia_fundamental <= 335:
    print("E4 Correcta")

elif frecuencia_fundamental >= 241  and frecuencia_fundamental <= 251:
    print("B3 Correcta")

elif frecuencia_fundamental >= 191  and frecuencia_fundamental <= 201:
    print("G3 Correcta")

elif frecuencia_fundamental >= 141  and frecuencia_fundamental <= 151:
    print("D3 Correcta")

elif frecuencia_fundamental >= 105  and frecuencia_fundamental <= 115:
    print("A2 Correcta")

elif frecuencia_fundamental >= 77  and frecuencia_fundamental <= 108:
    print("E2 Correcta")

else:
    print("Es recomendable ajustar la cuerda")
    
plt.show()
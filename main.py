from cProfile import label
from wave_file_manager import wave_file_read_sample
import matplotlib.pyplot as plt

wave_sample = wave_file_read_sample("test1.wav")


if wave_sample == None:
    print("ERREUR : Aucun sample a la lecture du fichier wave")

'''a = [5, 4, 12, 14, 3]
b = [4, 1, 2, 5 ,6, 7]
plt.plot(a, label='Graph A')
plt.plot(b, label="Graph B")
plt.legend()
plt.show()'''

plt.plot(wave_sample)
plt.show()
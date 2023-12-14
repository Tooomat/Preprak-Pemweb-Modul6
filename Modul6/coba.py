import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# Membaca dan menampilkan gambar
img = mpimg.imread('E:\Kuliah\Toomat\VSCodeWorkspace\PemogramanFungsional\Pre-Praktikum\Modul6\download.jpeg') #Sesuaikan dengan direktori

plt.imshow(img)
plt.title("Judul Gambar")
plt.show()
#2. Anotasi dan Teks
plt.annotate("Teks Anotasi", xy=(250, 230), xytext=('kiri', 'kanan'),
arrowprops=dict(arrowstyle="->"))
plt.text('l', 'j', "Teks Tertentu")
plt.hist(img.ravel(), bins=256, range=(0, 256), density=True,
color='gray', alpha=0.6)


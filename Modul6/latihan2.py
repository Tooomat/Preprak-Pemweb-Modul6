#Lengkapi kode dibawah ini untuk menjawab soal diatas ya
# TODO 0 : Import beberapa library lain yang dibutuhkan
from PIL import Image

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open('E:\Kuliah\Toomat\VSCodeWorkspace\PemogramanFungsional\Pre-Praktikum\Modul6\pemandangan.jpeg')
overlay_image = Image.open('E:\Kuliah\Toomat\VSCodeWorkspace\PemogramanFungsional\Pre-Praktikum\Modul6\ig.png')

# TODO 2 : Konversi overlay image ke mode RGB (menghilangkan alphachannel)
overlay_image = overlay_image.convert('RGB')

# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
overlay_image = overlay_image.resize((100, 100))

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center))
# TODO 5 : Simpan gambar hasil edit
result_image_path = 'E:\Kuliah\Toomat\VSCodeWorkspace\PemogramanFungsional\Pre-Praktikum\Modul6\hasil_overvlay.jpg'
background_image.save(result_image_path)
# TODO 6 : Tampilkan
background_image.show()
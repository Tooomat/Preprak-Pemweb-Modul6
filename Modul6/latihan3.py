from PIL import Image, ImageEnhance

# TODO 1: buka gambar dengan pillow
path_image = 'E:\Kuliah\Toomat\VSCodeWorkspace\PemogramanFungsional\Pre-Praktikum\Modul6\download.jpeg'
image = Image.open(path_image)

# TODO 2: tingkatkan kecerahan dan kontras
enhancer = ImageEnhance.Brightness(image)
bright_image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(bright_image)
contrast_img = enhancer.enhance(1.2)

# TODO 3: simpan gambar
result_image_path = 'E:\Kuliah\Toomat\VSCodeWorkspace\PemogramanFungsional\Pre-Praktikum\Modul6\contrant_bright.jpeg'
image.save(result_image_path)

image.show()





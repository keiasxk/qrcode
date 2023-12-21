import qrcode

data = 'https://github.com/keiasxk'

qr = qrcode.QRCode(version=10, box_size=10, border=10)

qr.add_data(data)

img = qr.make_image( fill_color='white', back_color='black')

img.save('test.png')
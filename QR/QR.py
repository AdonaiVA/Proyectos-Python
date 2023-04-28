import qrcode

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

qr = qrcode.QRCode(version=1, box_size=5, border=5)

qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'orange', back_color='black')
img.save('youtube_qr.png')
import qrcode

input_data = "https://www.williamthelee.com/"

# Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=8,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='', back_color='white')
img.save('qrcode01.png')
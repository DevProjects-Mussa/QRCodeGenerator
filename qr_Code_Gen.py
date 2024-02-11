import qrcode
import image

# Creating a QRCode object by specifying a version, box size, and border
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

# The data to be encoded in the QR code (in this case, it is a link to my GitHub profile)
data = "https://github.com/MusaIP12"    # Link to my github profile
# Adding the data to the QRCode object
qr.add_data(data)
qr.make(fit=True)
# Creating an image object for the QR code with black as the fill color and white as the background color
img = qr.make_image(fill="black", back_color="white")
# Saving the generated QR code image to a specified file path
img.save("C:/Users/patiphiri/PycharmProject/QR_Code/test.png")

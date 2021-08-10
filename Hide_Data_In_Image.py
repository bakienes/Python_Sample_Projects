from stegano import lsb
image = "file_path"
new_img = "flask_hidden.png"
msg = 'Your Secret Message Here'
# To Hide Message
lsb.hide(image, message=msg).save(new_img)
# To Revel Hidden Message
message = lsb.reveal(new_img)
print('Hidden message:', message)

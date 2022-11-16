import qrcode
#Generate QR Code
l=['aryan', 'charmi']
for i in range(len(l)):
    img=qrcode.make(l[i])
    name='C:/Users/CHARMI/Desktop/Sem7/QR_code/QR_' + str(l[i]) + '.jpg'
    img.save(name,'JPEG')
    # https://towardsdatascience.com/create-and-read-qr-code-using-python-9fc73376a8f9
# if __name__ == '__main__':
#     main()
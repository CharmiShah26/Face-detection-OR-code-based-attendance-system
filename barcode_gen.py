import qrcode
#Generate QR Code
l=['001', '002']


# Create your dictionary class
class my_dictionary(dict):
 
  # __init__ function
  def __init__(self):
    self = dict()
 
  # Function to add key:value
  def add(self, key, value):
    self[key] = value

# Declaring dictionary
dict_names=my_dictionary()

for i in range(len(l)):
    hash_generated=hash(l[i])
    # print(hash_generated)
    dict_names.add(l[i],hash_generated)

# print(dict_names)
# list_test = list(dict_names.items())
# print(list_test[1][1])

for i in range(len(l)):
    img=qrcode.make(list(dict_names.items())[i][1])
    name='C:/Users/CHARMI/Desktop/Sem7/Minor_project/QR_code/QR_' + str(l[i]) + '.jpg'
    img.save(name,'JPEG')

    # https://towardsdatascience.com/create-and-read-qr-code-using-python-9fc73376a8f9
# if __name__ == '__main__':
#     main()
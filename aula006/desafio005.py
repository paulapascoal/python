msg = input("Digite algo: ");
print ("Segue as informações sobre o que você digitou:");
print('Tipo primitivo: ', type(msg));
print('Alfanúmerico: ',msg.isalnum());
print('Alfabético: ', msg.isalpha());
print('Númerico',msg.isnumeric());

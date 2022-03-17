import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160') #Define qual algoritimo sera utilizado para hash

hash1.update(open(arquivo1,'rb').read()) #Define qual arquivi sera aberto pelo hash

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2,'rb').read())

if hash1.digest() != hash2.digest(): #.digest resume os dados passados passado para o metodo update
    print(f'O arquivo {arquivo1} é diferente do arquivo {arquivo2}')
    print('O hash do arquivo', arquivo1, 'é: ', hash1.hexdigest()) #.hexdigest resume o h em exdecimal e nos mostra o hash
    print('O hash do arquivo', arquivo2, 'é: ', hash2.hexdigest())
else:
    print(f'O arquivo {arquivo1} é igual ao arquivo {arquivo2}')
    print('O hash do arquivo', arquivo1, 'é: ', hash1.hexdigest())
    print('O hash do arquivo', arquivo2, 'é: ', hash2.hexdigest())
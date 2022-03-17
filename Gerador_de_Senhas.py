import random, string

tamanho = int(input("Digite o tamanho de senha que você deseja gerar: ")) #Tamanho de caracteres que deve conter a senha

chars = string.ascii_letters + string.digits + '!@ç#$%&*()-=+' #estrutura da senha gerada string.ascii_letters {letras maísculas e minusculas}, string.digits {digitos de 0 a 9}

rnd = random.SystemRandom #chama  biblioteca os a classe urandom essa classe gera númeroa aleatórios a partir de fontes fornecidas pelo SO

print(''.join(rnd.choice(chars) for i in range(tamanho))) #rnd.choice retorna uma lista com os caracteres randonidos no caso puxando da variável char.

#rnd.choice não está aceitando o argumento for.
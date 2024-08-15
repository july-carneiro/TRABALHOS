#CONSTRUA UMA PÁGINA ONDE O USUÁRIO DIGITARÁ 3 NÚMEROS E O PROGRAMA EXIBIRÁ, NA TELA O MAIOR ENTRE ELES.

Numero01=int(input('Digite um número:'))
Numero02=int(input('Digite um segundo número:'))
Numero03=int(input('Digite um terceiro número:'))

if ((Numero01>=Numero02) and (Numero01>Numero03)):
 print ('O maior número é'[Numero01])
elif ((Numero02>=Numero03) and (Numero02>Numero01)):
 print('O maior número é'[Numero02])
else:
 print ('O maior número é'[Numero03])






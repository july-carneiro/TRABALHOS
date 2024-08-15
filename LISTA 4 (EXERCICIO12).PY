#CONSTRUA UM PROGRAMA ONDE O USUÁRIO DIGITARÁ SUA IDADE E CASO A SUA IDADE SEJA MAIOR OU IGUAL A 18 ANOS
# TERÁ COMO RESPOSTA "MAIOR DE IDADE" CASO CONTRÁRIO "MENOR DE IDADE"

maioridade=18
idade=int(input('Digite sua idade'))

if (idade>=maioridade):
   print('Maior de idade')
else:
   print('Menor de idade')
   
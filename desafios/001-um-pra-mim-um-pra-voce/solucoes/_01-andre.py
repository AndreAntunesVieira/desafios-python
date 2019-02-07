quantidade_de_balas = int(input("Quantas balas temos para dividir? "))

if quantidade_de_balas < 0:
  print 'Ah, nao vou contar balas negativas, sai fora!'

elif quantidade_de_balas == 0:
  print 'Voce nao tem balas :('

elif quantidade_de_balas > 100:
  print 'Ah nao, tem muitas balas, nao vou contar!'

else:
  metade_das_balas = int(quantidade_de_balas/2)
  for numero_de_um_ate_metade_das_balas in range(1, metade_das_balas+1):
    print '{} pra mim, {} pra voce'.format(numero_de_um_ate_metade_das_balas, numero_de_um_ate_metade_das_balas)

  resto_das_balas = quantidade_de_balas % 2
  if resto_das_balas == 1:
    print 'Ah sobrou uma, vou pegar pra mim'

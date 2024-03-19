#apresentação e entrada dos valores
print('Bem-Vindo a loja do Luis Fernando Duarte 4660126')
valor = float(input('Entre com o valor unitário do produto:R$'))
quantia = int(input('Entre com a quantidade do produto:'))
#calculo do total e condições de desconto
total = valor * quantia
if 0< total < 2500:
   print('O valor total foi de:R$ {:.2f}'.format(total))
elif 2500 <= total < 6000:
  desconto = valor * 0.04
  valor_com_desconto = total - desconto
  print('O valor sem desconto foi:R$ {:.2f}'.format(total))  
  print('O valor com desconto foi:R$ {:.2f} (desconto 4%)'.format(valor_com_desconto))
elif 6000 <= total < 10000:
  desconto = valor * 0.07
  valor_com_desconto = total - desconto
  print('O valor sem desconto foi:R$ {:.2f}'.format(total))  
  print('O valor com desconto foi:R$ {:.2f} (desconto 7%)'.format(valor_com_desconto))
elif 10000 <= total:
  desconto = valor * 0.11
  valor_com_desconto = total - desconto
  print('O valor sem desconto foi:R$ {:.2f}'.format(total))  
  print('O valor com desconto foi:R$ {:.2f} (desconto 11%)'.format(valor_com_desconto))
#em caso dos valores serem a baixo de 0
else:
    print('Desculpe, não foi possível determinar o calculo da compra,certifique-se que o preço e quatidade foram digitados corretamente ')


 

 
 
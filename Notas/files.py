#Nesta sessão iremos entender as noções de arquivos e dados persistentes


with open('accounts.txt', mode = 'w') as accounts:
   accounts.write('100 Jones 24.98\n')
   accounts.write('200 Doe 345.67\n')
   accounts.write('300 White 0.00\n')
   accounts.write('400 Stone -42.16\n')
   accounts.write('500 Rich 224.62\n')
#with implicitamente chama o objeto 'close'

with open('accounts.txt', mode = 'r') as accounts:
   print(f'{"Conta":<10}{"Nome":<10}{"Saldo":>10}')
   for record in accounts:
      conta, nome, saldo = record.split()
      print(f'{conta:<10}{nome:<10}{saldo:>10}')
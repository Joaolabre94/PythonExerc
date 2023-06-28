from Conta import Conta
conta1 = Conta(1, 123, 'Joao',0)
conta2 = Conta(3, 456, 'Maria',0)

if conta1 != conta2:
    print('Endereços diferentes de memoria')

conta1 = conta2
if conta1 == conta2:
    print('Endereços iguais de memoria')
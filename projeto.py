class IngressoCinema:
    def __init__(self, data, sala, valor):
        self.data = data
        self.sala = sala
        self.valor = valor
    
    def get_data(self):
        return self.data
        
    def set_data(self, data):
        self.data = data
    
    def get_sala(self):
        return self.sala
        
    def set_sala(self, sala):
        self.sala = sala
    
    def get_valor(self):
        return self.valor
        
    def set_valor(self, valor):
        self.valor = valor

    def calcularDesconto(self, idade):
        if 12 <= idade <= 15:
            desconto = self.valor * 0.4
        elif 16 <= idade <= 20:
            desconto = self.valor * 0.3
        elif idade > 20:
            desconto = self.valor * 0.2
        else:
            desconto = 0
        print(f'\nO valor do seu desconto é R${desconto:.2f}')
        return desconto

    def recibo(self, desconto):
        valor_final = self.valor - desconto
        print('='*30)
        print('         RECIBO')
        print('='*30)
        print(f'Data  : {self.data}')
        print(f'Sala  : {self.sala}')
        print(f'Valor : R${self.valor:.2f}')
        print(f'Desc. : -R${desconto:.2f}')
        print('-'*30)
        print(f'TOTAL : R${valor_final:.2f}')
        print('='*30 + '\n')


class TestarIngresso:
    def main():
        print('='*30)
        print('SISTEMA DE INGRESSO DE CINEMA')
        print('='*30)
        data = input('\nInsira a data do ingresso: (DD/MM/AAAA) \n')
        
        print('\nSalas')
        print('='*30)
        for c in range(1,7):
            print(f'{c}. SALA {c}')
        print('='*30)
        escolha = int(input('\nDigite o número da sala escolhida: \n'))
        if escolha not in [1, 2, 3, 4, 5, 6]:
            print('Sala inválida.')
        else:
            sala = escolha

        print('\nINGRESSOS')
        print('='*40)
        print('1. Ingresso comum   :   R$20,00')
        print('2. Ingresso VIP     :   R$30,00')
        print('='*40, '\n')
        ingresso = input('\nDigite o número do ingresso escolhido: \n')
        if ingresso == '1':
            valor = 20
        elif ingresso == '2':
            valor = 30 
        else:
            print('Escolha inválida')

        ingresso = IngressoCinema(data, sala, valor)

        idade = int(input('\nDigite sua idade: \n'))
        desconto = ingresso.calcularDesconto(idade)
        
        ingresso.recibo(desconto)
        ingresso.set_sala(5)
        print(f'Nova sala: {ingresso.get_sala()}')
TestarIngresso.main()
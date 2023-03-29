class Pessoas: 
  def __init__(self,nome1,nome2,idade1,idade2):  
    self.nome1 = nome1
    self.nome2 = nome2 
    self.idade1 = idade1 
    self.idade2 = idade2 
  
  def Maior (self):

    if idade1 > idade2 : 
      print('{} tem a idade maior'.format(nome1)) 

    if idade2 > idade1: 
      print('{} tem a idade maior'.format(nome2))  
    return 

if __name__ == '__main__': 
   nome1 = input("Digite o primeiro nome:")
   idade1 = int(input("Digite a idade:"))          
   nome2 = input("Digite o proximo nome:") 
   idade2 = int(input("Digite a idade:")) 

   pessoa = Pessoas(nome1,nome2,idade1,idade2) 
   pessoa.Maior() 



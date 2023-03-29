class funcionario: 
  def __init__(self):  
    self.nome = ""
    self.salarioBruto = 1500.00 
    self.imposto = 1000.00  

  def informacao(self):
      print("O nome do Foncionario é {} salario R${} e imposto e {}".format(self.nome,self.salarioBruto,self.imposto))  
     
  def aumentosalarial(self):
      aumento = int(input("Digite a porcentagem do aumento do salario:"))  
 
      aumentosalario = ((aumento * self.salarioBruto)/100) + self.salarioBruto 
      print(" O salario de {} aumentou para {} ".format(self.salarioBruto,aumentosalario))  

if __name__ == '__main__': 
   Funcionario = funcionario()  
   Funcionario.informacao()  
   Funcionario.aumentosalarial()
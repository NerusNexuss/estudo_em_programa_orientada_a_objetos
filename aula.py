class Aluno:   
   def __init__(self,nome,nota1,nota2,nota3): 
      self.Nome = nome 
      self.Nota1 = float(nota1)
      self.Nota2 = float(nota2)
      self.Nota3 = float(nota3) 

   def mediafinal(self): 
    media = ((self.Nota1+self.Nota2+self.Nota3)/3) 

    if media >= 60 : 
      print("NOTA FINAL = {:.2f}".format(media)) 
      print("APROVADO") 

    if media <60 :    
      faltam = (60 - media)
      print("NOTA FINAL = {:.2f}".format(media))
      print("REPROVADO ") 
      print("FALTAM {:.2f} PONTOS".format(faltam)) 

if __name__ == '__main__':    
  nome = (input("Nome do Aluno:"))
  nota1 = (input("Digite a primeira nota:"))   
  nota2 = (input("Digite a segunda nota:"))  
  nota3 = (input("Digite a Terceita nota:")) 

  aluno = Aluno(nome,nota1,nota2,nota3) 
  aluno.mediafinal()

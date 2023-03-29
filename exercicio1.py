import math
class Retangulo: 
  def __init__(self): 
    self.largura = 3.00 
    self.altura = 4.00 

  def calculos(self): 
    area = self.largura*self.altura  
    print("A area é {}".format(area))

    perimetro =  (2*(self.altura+self.largura)) 
    print("O perimetro é {}".format(perimetro))

    diagonal = math.sqrt(pow(self.largura , 2) + pow(self.altura,2))  
    print("A diagonal é {}".format(diagonal))  



if __name__ == '__main__': 
  retangulo = Retangulo()
  retangulo.calculos()
  
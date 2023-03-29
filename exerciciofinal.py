
class Triangulo: 
   def __init__(self,xa,xb,xc,ya,yb,yc):
    self.xa = xa
    self.xb = xb
    self.xc = xc 
    self.ya = ya
    self.yb = yb
    self.yc = yc 

   def Calculo(self):   
      mx = (self.xa + self.xb + self.xc)/2 
      my = (self.ya + self.yb + self.yc)/2   
      ax = (self.xa * self.xb * self.xc)/2
      ay = (self.ya * self.yb * self.yc)/2  

      if ax > ay: 
         print('Triangulo x tem a area maior') 

      if(ay > xa): 
         print('Triangulo y tem a area maior')   
       
      

      

if __name__ == '__main__':
    print('Entre com os lados para o triangulo x:')
    xa = float(input('Xa = ')) 
    xb = float(input('Xb = '))
    xc = float(input('Xc = ')) 
    print('Entre com os lados para o triangulo y:')
    ya = float(input('Ya = ')) 
    yb = float(input('Yb = ')) 
    yc = float(input('Yc = '))  

    triangulo = Triangulo(xa,xb,xc,ya,yb,yc)
    triangulo.Calculo()

    
using System; 

namespace School 
{
  class Program 
  {    
    static void Main(string[] args)   
    { 
      double totalArrecadado;

      Course courseMath = new Course();
       
      courseMath.nome = "Matemática Avançada"; 
      courseMath.value = 100.00; 
      courseMath.qtdeAlunos = 40; 

      totalArrecadado = courseMath.value * courseMath.qtdeAlunos;  
       
      Console.WriteLine("O valor Arrecadado é: " + totalArrecadado);
    }
  }
}
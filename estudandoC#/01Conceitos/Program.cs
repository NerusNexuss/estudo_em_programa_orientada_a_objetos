using System; 

namespace _01Conceitos
{
    class Program 
    {
        static void Main(string[] args)
        {
          Pessoa obj = new Pessoa();
          obj.nome = "Marcos";
          obj.idade = 23; 
          obj.mensagem();
        }
    }
}

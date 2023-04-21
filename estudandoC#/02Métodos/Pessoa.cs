using System; 

class Pessoa
{
 
 // Métados 01 
public void apresentar()
{
    Console.WriteLine("Ola!!");
}
 // Métados 02
  public void apresentar(string nome)
{
 Console.WriteLine("Olá "+nome);
}
 // Métados 03
public void apresentar(string nome, int idade)
{
  Console.Write("Ola "+nome+" Você tem "+idade+" anos");
}

}
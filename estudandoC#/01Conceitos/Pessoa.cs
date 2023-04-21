using System; 

class Pessoa
{
    //Atributos 
    public string nome;

    public int idade; 

    public void mensagem()
    {
        Console.WriteLine("Olá "+nome+" Você tem "+idade+" anos");
    }
}
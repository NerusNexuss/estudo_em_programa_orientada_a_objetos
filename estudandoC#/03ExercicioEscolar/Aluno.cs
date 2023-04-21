using System; 

class Aluno
{

    // Atributos 
    public string nome; 

    public double nota1, nota2;   

    //Média 
    public double media()
    {
      return (nota1+nota2)/2; 
    }
    //Situação 
    public string Situação(double media)
    {
         return media >= 7 ? "aprovado" : "reprovado";
    }
    // Mensagem  
    public void mensagem()
    {

      // Obter a média 
      double ObterMedia = media(); 

      // Obter a Situação  
      string ObterSituacao = Situação(ObterMedia);

      // Mensagem   
      Console.WriteLine(nome+" está "+ObterSituacao+" com média "+ObterMedia);

    }


}
namespace School
{
    class Course{
           public string nome; 
           public double value; 

           public int qtdeAlunos = 0;  

           public double TotalArrecadado(){
             return qtdeAlunos* value;
           }

    }
}

 
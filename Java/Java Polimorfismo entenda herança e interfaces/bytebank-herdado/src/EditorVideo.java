public class EditorVideo extends Funcionario {

    public double getBonificacao(){
        System.out.println("Chamando o metodo de bonificação do Editor de video");
        return super.getBonificacao() + 100;
    }
}

public class Gerente extends Funcionario{
    private int senha;

    public void setSenha(int senha) {
        this.senha = senha;
    }

    public boolean autenticarSenha(int senha){
        if(this.senha == senha){
            return true;
        }
        return false;
    }

    public double getBonificacao(){
        System.out.println("Chamando a bonificação do Gerente");
        return super.getBonificacao() + super.getSalario();
    }
}

public class App {
    public static void main(String[] args) throws Exception {
        Cliente vitor = new Cliente();
        vitor.nome = "Vitor Santos";
        vitor.cpf = "222.222.222-12";
        vitor.profissao = "Estudante";

        Conta contaDoVitor = new Conta();
        contaDoVitor.deposita(100);

        contaDoVitor.titular = vitor;

        System.out.println(contaDoVitor.titular.nome);
        System.out.println(contaDoVitor.titular);
        System.out.println(vitor);
    }
}

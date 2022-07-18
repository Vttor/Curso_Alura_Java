public class App {
    public static void main(String[] args) throws Exception {
        Conta conta = new Conta();

        conta.setNumero(1337);
        System.out.println(conta.getNumero());

        conta.setTitular(new Cliente());

        conta.getTitular().setNome("Vitor Santos");
        conta.getTitular().setProfissao("Dev");
        
        Cliente titularDaConta = conta.getTitular();
        titularDaConta.setProfissao("Dev");

        System.out.println(titularDaConta);
        System.out.println(conta.getTitular());

        
    }
}

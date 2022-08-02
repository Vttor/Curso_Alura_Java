public class TesteGerente {
    public static void main(String[] args) {
        
        Gerente g1 = new Gerente();

        g1.setNome("Vitor");
        g1.setCpf("2321412");
        g1.setSalario(5000.0);

        System.out.println(g1.getNome());
        System.out.println(g1.getCpf());
        System.out.println(g1.getSalario());

        g1.setSenha(22222);

        System.out.println(g1.autenticarSenha(22222));
    }
}

public class TesteFuncionario {
        public static void main(String[] args) {
            Funcionario vitor = new Funcionario();
            vitor.setNome("Vitor Santos");
            vitor.setCpf("213214128-98");
            vitor.setSalario(2600.00);

            System.out.println(vitor.getNome());
            System.out.println(vitor.getBonificacao());

        }
}

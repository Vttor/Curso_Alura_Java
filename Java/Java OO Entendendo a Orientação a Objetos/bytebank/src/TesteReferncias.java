public class TesteReferncias {
    public static void main(String[] args) {
        Conta primeirConta = new Conta();
        primeirConta.saldo = 300;

        System.out.println("saldo da primeira conta: " + primeirConta.saldo);
        
        Conta segundaConta = primeirConta; 

        System.out.println("Saldo da segunda conta: " + segundaConta.saldo);
        
        
        segundaConta.saldo += 100;
        System.out.println("Saldo da segunda conta: " + segundaConta.saldo);
        
        System.out.println(primeirConta.saldo);

        if(primeirConta == segundaConta){
            System.out.println("São a mesma conta");
        }
        
        System.out.println(primeirConta);
        System.out.println(segundaConta);
    }
}

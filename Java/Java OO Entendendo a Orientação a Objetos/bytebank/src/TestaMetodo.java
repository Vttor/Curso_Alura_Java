public class TestaMetodo {
    public static void main(String[] args) {
        Conta contaDoVitor = new Conta();
        contaDoVitor.saldo = 100;
        contaDoVitor.deposita(50);
        System.out.println(contaDoVitor.saldo);
        boolean conseguiuRetirar = contaDoVitor.saca(20);
        System.out.println(contaDoVitor.saldo);
        System.out.println(conseguiuRetirar);

        Conta contaDaMarcela = new Conta();
        contaDaMarcela.deposita(1000);
        
        if(contaDaMarcela.transfere(3000, contaDoVitor)){
            System.out.println("Transferencia feita com sucesso");
        } else {
            System.out.println("faltou dinheiro");
        }
            
            System.out.println(contaDaMarcela.saldo);
            System.out.println(contaDoVitor.saldo);


            contaDoVitor.titular = "Vitor Santos";
            System.out.println(contaDoVitor.titular);
            
    }
}

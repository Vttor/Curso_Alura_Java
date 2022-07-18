public class Conta {
    private  double saldo;
    private int agencia;
    private int numero;
    private Cliente titular;
    private static int total;

    
    public Conta(int agencia, int numero){
        total++;
        System.out.println("O total é " + total);
        this.agencia = agencia;
        this.numero = numero;
        System.out.println("Estou criando uma conta " + numero);
    }
    
    public Cliente getTitular() {
        return this.titular;
    }
    
    public void setTitular(Cliente titular) {
        this.titular = titular;
    }
    
    public int getAgencia() {
        return this.agencia;
    }

    public void setAgencia(int agencia) {
        if(agencia <= 0){
            System.out.println("Não pode valor de agencia menor ou igual a 0");
            return;
        }
        this.agencia = agencia;
    }
    
    
    public void setNumero(int numero) {
        if(agencia <= 0){
            System.out.println("Não pode valor de numero menor ou igual a 0");
            return;
        }
        this.numero = numero;
    }
    
    public int getNumero() {
        return this.numero;
    }
    
    
    public void deposita(double valor){
        this.saldo += valor;
    }

    public boolean saca(double valor){
        if(this.saldo >= valor){
            this.saldo -= valor;
            return true;
        }
        return false;
    }
    
    public boolean transfere(double valor, Conta destino){
        if(this.saldo >= valor){
            this.saldo -= valor;
            destino.deposita(valor);
            return true;
        }
        return false;
    }
    
    public double pegaSaldo(){
        return this.saldo;
    }
    
    public static int getTotal() {
        return total;
    }
}

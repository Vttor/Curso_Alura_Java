public class TestaLacos {
    public static void main(String[] args) {
        for (int mutiplicador = 1; mutiplicador <= 10; mutiplicador++) {
            System.out.print("Mutilplos de " + mutiplicador + ": ");
            for (int contador = 0; contador <= 10; contador++) {
                System.out.print(mutiplicador*contador);
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}

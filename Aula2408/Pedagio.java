public class Pedagio {
    public static void main(String[] args) {
        //aplicação consumidora
        // constroi cancela #constructor e os veiculos
        //processa cobranças

        Cancela cancela01 = new Cancela();

        cancela01.preco_por_eixo = 3.00;

        Veiculo chevette = new Auto();

        Caminhao scania = new Caminhao();
        scania.numero_eixos_cobranca = 3;

        chevette.numero_eixos_cobranca = 1;

        double preco_cobrado = cancela01.cobrar(chevette);
        
        System.out.println(preco_cobrado);
    }
}

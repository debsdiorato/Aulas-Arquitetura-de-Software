public class Cancela {
    public double preco_por_eixo;
    public double cobrar(Veiculo veiculo){
        return this.preco_por_eixo * veiculo.numero_eixos_cobranca;
    }
}

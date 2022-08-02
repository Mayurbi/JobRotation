public class exercicioCinco{
	public static void main(String[] args) {
		String arroz = "Feijão não é embaixo do arroz";
		System.out.println(arroz);
		String pedrinho = feijao(arroz, arroz.length()-1);
		System.out.println(pedrinho);
	}


	static String feijao(String arroz, int index){
		if(index == 0){
			return arroz.charAt(0) + "";
		}
		char letter = arroz.charAt(index);
		return letter + feijao(arroz, index-1);
	}
}
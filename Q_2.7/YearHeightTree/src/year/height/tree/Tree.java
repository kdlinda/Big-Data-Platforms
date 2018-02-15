package year.height.tree;


public class Tree {

	public static String readTree(String X) {
			
		String[] components = X.split(";");
		String annee = components[5];
		String hauteur = components[6];
		
		return annee + '\t' + hauteur + '\n';
	}
}
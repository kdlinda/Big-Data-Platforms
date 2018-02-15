package Ex2_8;

public class ISD {
	
	public static String readIsd(String line) {

	// Store relevant info in string
			String USAF = line.substring(0, 6).trim();
			String name = line.substring(13, 42).trim();
			String FIPSID = line.substring(43, 45).trim();
			String elevation = line.substring(74,81).trim();

			return String.format("%s\t%s\t%s\t%s\n", USAF, name, FIPSID, elevation);
			}
}

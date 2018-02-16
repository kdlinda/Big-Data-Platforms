package year.height.tree;


import java.io.*;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;

public class DisplayCSV {

	public static void main(String[] args) throws IOException {
		
		String inputSrc = "/Users/noemiequere/Documents/SCHOOL/DSBA/T1/Big_Data_Algorithms/arbres.csv";
		String outputSrc = "";
		
				
		// Open the file
		Configuration conf = new Configuration();
		FileSystem fs = FileSystem.get(conf);
		InputStream in = fs.open(new Path(inputSrc));
		OutputStream ou = fs.create(new Path(outputSrc));
		
		try {
			InputStreamReader isr = new InputStreamReader(in);
			BufferedReader br = new BufferedReader(isr);
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(ou, "UTF-8"));
			
			// read line by line
			String line = br.readLine();
			
			while (line != null){
				// Process of the current line
				String treeX = Tree.readTree(line);
				bw.write(treeX);
				
				// Go to the next line
				line = br.readLine();
			}
			
			bw.close();
			br.close();
		}
		finally {
			in.close();
			fs.close();
		}		
	}

}
 

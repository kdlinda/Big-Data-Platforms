package Ex2_8;


import java.io.*;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;

public class displayFile {

	public static void main(String[] args) throws IOException {
		
		String inputSrc = "/Users/noemiequere/Documents/SCHOOL/DSBA/T1/Big_Data_Algorithms/isd-history.txt";
		String outputSrc = "/Users/noemiequere/Documents/SCHOOL/DSBA/T1/Big_Data_Algorithms/isd-output.txt";

				
		// Open the file
		Configuration conf = new Configuration();
		FileSystem fs = FileSystem.get(conf);
		InputStream in = fs.open(new Path(inputSrc));
		OutputStream ou = fs.create(new Path(outputSrc));
		
		try {
			InputStreamReader isr = new InputStreamReader(in);
			BufferedReader br = new BufferedReader(isr);
			BufferedWriter bw = new BufferedWriter( new OutputStreamWriter( ou, "UTF-8" ));
			
			// Read line by line
			String line = br.readLine();
			
			int i = 0;
			while (line != null){
				
				// Goes to the 23rd line
				if (i < 22) {
					line = br.readLine();
					i += 1;
					continue;
				}
				
				// Process of the current line
				bw.write(line);
				
				// Go to the next line
				line = br.readLine();
			}
			
			bw.close();
			br.close();
		}
		finally {
			// Close the file
			in.close();
			fs.close();
		}		
	}

}
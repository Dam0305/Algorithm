import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//baekjoon 5086
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			StringTokenizer tn = new StringTokenizer(input.readLine());
			
			int first = Integer.parseInt(tn.nextToken());
			int second = Integer.parseInt(tn.nextToken());
			
			if(first == 0 && second == 0) break;
			
			if (first < second  && second % first == 0)
				System.out.println("factor");
			else if(first > second && first % second == 0)
				System.out.println("multiple");
			else
				System.out.println("neither");
		}
		return;
	}
}

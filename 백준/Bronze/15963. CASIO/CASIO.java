import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

		String num1 = sc.next();
		String num2 = sc.next();
        
		if (num1.equals(num2)) {
			System.out.println(1);
		}else{
            System.out.println(0);
        }
    }
}
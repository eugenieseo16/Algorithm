import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");

        BigInteger num1 = new BigInteger(input[0]);
        BigInteger num2 = new BigInteger(input[1]);
        System.out.println(num1.add(num2).toString());
    }
}

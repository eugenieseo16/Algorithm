import java.math.BigInteger;
import java.util.Scanner;

import static java.math.BigInteger.valueOf;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        BigInteger num1 = new BigInteger(sc.next());
        BigInteger num2 = new BigInteger(sc.next());

        num1 = num1.add(num2);
        System.out.println(num1.toString());

    }

}


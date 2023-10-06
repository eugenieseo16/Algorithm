import java.math.BigInteger;
import java.util.Scanner;

import static java.math.BigInteger.valueOf;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        BigInteger num = new BigInteger(sc.nextLine());
        BigInteger gap = new BigInteger(sc.nextLine());

        BigInteger ans1 = num.subtract(gap).divide(valueOf(2)).add(gap);
        BigInteger ans2 = num.subtract(gap).divide(valueOf(2));
        
        System.out.println(ans1);
        System.out.println(ans2);
    }

}

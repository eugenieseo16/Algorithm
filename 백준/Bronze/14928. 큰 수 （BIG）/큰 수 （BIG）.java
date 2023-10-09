import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String num = sc.next();
        
        // 나머지 연산 분배 법칙 (A + B) % N = ((A % N) + (B % N)) % N
        long reminder = 0;
        for(int i = 0; i < num.length(); i++){
            reminder= (reminder * 10 + (num.charAt(i)- '0')) % 20000303;
        }

        System.out.println(reminder);
    }
}

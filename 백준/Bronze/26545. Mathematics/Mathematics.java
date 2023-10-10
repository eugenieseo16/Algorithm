import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int ans = 0;
        for(int i =0; i < num; i++){
            int temp = sc.nextInt();
            ans += temp;
        }
        System.out.println(ans);
    }
}

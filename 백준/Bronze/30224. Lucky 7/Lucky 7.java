import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        if(Integer.toString(num).contains("7")){
            if(num % 7 == 0){
                System.out.println(3);
            }else{
                System.out.println(2);
            }
        }else{
            if(num % 7 == 0){
                System.out.println(1);
            }else{
                System.out.println(0);
            }
        }
    }
}
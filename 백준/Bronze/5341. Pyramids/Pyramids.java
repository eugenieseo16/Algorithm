// import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        while(true){
            int num = sc.nextInt();
            if(num == 0){
                break;
            }else{
                int ans = (num * (num+1)) / 2;
                System.out.println(ans);
            }
        }
    }
}




import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int hour = sc.nextInt();
        int min = sc.nextInt();
        int sec = sc.nextInt();
        int time = sc.nextInt();

        sec  += time;

        if(sec >=60){
            int temp_min = sec / 60;
            sec = sec % 60;
            min += temp_min;
        }

        if(min >= 60){
            int temp_h = min / 60;
            min = min % 60;
            hour += temp_h;
        }

        hour = hour % 24;

        System.out.println(hour + " " + min+ " " + sec);
    }
}

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();

        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(num1);
        numbers.add(num2);
        numbers.add(num3);
        Collections.sort(numbers);
        System.out.println(numbers.get(1));
    }
}






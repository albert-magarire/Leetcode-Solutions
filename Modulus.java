// Check if a number is even or odd using modulus operator
import java.util.Scanner;

public class Modulus {
    public static void main(String[] args){
        Scanner user_input = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int number = user_input.nextInt();
        if (number % 2 == 0){
            System.out.println("Number " + number + " is even");
        }else{
            System.out.println("Number " + number + " is odd");
        }
    }
}

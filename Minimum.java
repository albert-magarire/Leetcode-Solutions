import java.util.ArrayList;
import java.util.Scanner;
public class Minimum{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        System.out.println("Enter elements. Use # to stop: ");
        while(input.nextInt() != '#'){
            list.add(input.nextInt());
        }

        findMin(list);
    }

    public static void findMin(ArrayList<Integer> list){
        int minVal = list.get(0);

        for (int i = 1; i < list.size(); i++){
            if (list.get(i) < minVal){
                minVal = list.get(i);
            }
        }

        System.out.println("The minimum value is: " + minVal);
    }

}

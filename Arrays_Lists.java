
import java.util.ArrayList;
import java.util.Scanner;
public class Arrays_Lists{
    public static void main(String[] args){
        /*
         * Static Arrays
         * - Fixed size
         * - Can hold primitives and objects
         * - Example: int[], String[]
         * - Syntax: type[] arrayName = new type[size];
         * - Example: int[] numbers = new int[5];
         * - Access elements using index: arrayName[index]
         * - Example: numbers[0] = 10;
         * - Limitations: cannot change size after creation
         * 
         * 
         * Dynamic Arrays (ArrayList)
         * - Resizable
         *  - Can only hold objects (use wrapper classes for primitives)
         * - Example: ArrayList<Integer>, ArrayList<String>
         * - Syntax: ArrayList<type> listName = new ArrayList<>();
         * - Example: ArrayList<Integer> numbers = new ArrayList<>();
         * - Add elements using add() method: listName.add(element)
         * - Example: numbers.add(10);
         * - Access elements using get() method: listName.get(index)
         * - Example: int num = numbers.get(0);
         * - Can change size dynamically
         * - Requires import: import java.util.ArrayList;
         * - Example: import java.util.ArrayList;
         * Comparison:
         * - Use static arrays when size is known and fixed
         * - Use ArrayList when size may change or is unknown
         * Example:
         * Static Array: int[] staticArray = new int[5];
         * Dynamic Array: ArrayList<Integer> dynamicArray = new ArrayList<>();
         * 
         */

        Scanner user_input = new Scanner(System.in);

        int[] intArray = {1,2,3,4,5};
        String[] strArray = {"apple", "banana", "cherry"};

        System.out.println("Enter an element to substitute in intArray: ");
        int userInt = user_input.nextInt();
        System.out.println("Entyer the index at whihc to make the substitution: ");
        int userIndex =  user_input.nextInt();
        System.out.println("Confirm: we will susbtitute " + intArray[userIndex] + "with " + userInt + " at index " + userIndex + ". (y/n)");
        char userConfirm = user_input.next().charAt(0); // get first char of user input
        if (userConfirm == 'y' || userConfirm == 'Y'){
            intArray[userIndex] = userInt;
            System.out.println("Substitution Completed.");
        }else if(userConfirm == 'n' || userConfirm == 'N'){
            System.out.println("Substitution Cancelled.");
        }
        //print intArray
        System.out.print("intArray: ");
        for (int i = 0; i < intArray.length; i++){
            System.out.print(intArray[i] + " ");
        }


        intArray[0] = 23;
        strArray[2] = "orange";

        ArrayList<Integer> intList = new ArrayList<>(); // Dynamic Array for integers
        ArrayList<String> strList = new ArrayList<>();

        intList.add(45);
        strList.add("grape");
        intList.set(0, 67);

        //print intList
        System.out.print("\nintList: ");
        for (int i = 0; i < intList.size(); i++){
            System.out.print(intList.get(i) + " ");
        }
    }
}
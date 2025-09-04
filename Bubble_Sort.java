import java.util.Scanner;
public class Bubble_Sort {
    public static void main(String[] args) {
        Scanner input  = new Scanner(System.in);
        System.out.println("Enter number of elements: ");
        int n = input.nextInt(); // number of elements
        int[] arr = new int[n]; // array to hold the elements
        System.out.println("Enter " + n + " integers: ");
        for (int i = 0; i < n; i++) {
            arr[i] = input.nextInt(); // read each integer
        }

        //print the unsorted array
        System.out.println("Unsorted array: ");
        for (int num : arr) {
            System.out.print(num + " ");
        }

        bubbleSort(arr); // call the bubble sort function
    }

        

        // Bubble sort algorithm
        public static void bubbleSort(int[] arr){
            int n = arr.length;
            boolean flag = true;
            while (flag) {
                flag = false;
                for (int i = 0; i < n - 1; i++) {
                    if (arr[i] > arr[i + 1]) {
                        // swap arr[i] and arr[i+1]
                        int temp = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = temp;
                        flag = true; // set flag to true to indicate a swap occurred
                    }
                }
                n--; // reduce the range of comparison  as the largest element is at the end
            // print the sorted array
            System.out.println("\nSorted array: ");
            for (int num : arr) {
                System.out.print(num + " ");
            }
        }
    }
}

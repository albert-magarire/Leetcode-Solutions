public class Fibonacci_Recursive {
    public static void main(String args[]){
        System.out.print(fibonacci(3));
    }

    //this code will calculate the fibonacci number at position n and has a time complexity of O(2^n)
    public static int fibonacci(int n){
        if (n == 0){
            return 0;
        }else if(n == 1){
            return 1;
        }else{
            return fibonacci(n -1) + fibonacci(n-2);
        }
    }
}

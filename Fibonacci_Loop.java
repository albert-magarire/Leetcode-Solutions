public class Fibonacci_Loop {
    public static void main(String[] args){
    int left_num = 0;
    int right_num = 1;

    System.out.println(left_num);
    System.out.println(right_num);

    for(int i= 0; i < 18; i++){
        int num_sum = left_num + right_num;
        System.out.println(num_sum);
        left_num = right_num;
        right_num = num_sum;
    }
}
}
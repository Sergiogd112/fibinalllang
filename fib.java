/**
 * fib
 */
public class fib {

    public static void main(String[] args) {
        int n=80;
        long[] fibarr=new long[n];
        fibarr[0]=0;
        fibarr[1]=1;
        for(int i =2;i<n;i++){
            fibarr[i]=fibarr[i-1]+fibarr[i-2];
        }
        System.out.println(fibarr[n-1]);
    }
}
import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            double a,b,c,d;
            a = sc.nextDouble();
            if (a==-1) break;
            b = sc.nextDouble();
            c = sc.nextDouble();
            d = sc.nextDouble();
            System.out.println((int)(a+b+c+d)%2);
        }
        sc.close();
    }
}

import java.lang.*;
import java.util.Scanner;
class Table
{
public static void main(String[] args)
{
Scanner sc = new Scanner(System.in);
System.out.println("Enter n table multiplication");
int n = sc.nextInt();
for(int i=0;i<=10;i++){
System.out.println(n+"*"+i+"="+(n*i));
}
}
}
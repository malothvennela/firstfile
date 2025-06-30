import java.util.Scanner;
class Add
{
public static void main(String[] args)
{
Scanner sc = new Scanner(System.in);
System.out.println("enter n numbers");
int number=sc.nextInt();
int sum=0;
System.out.println("enter numbers");
for(int i=0;i<number;i++)
{
int n = sc.nextInt();
sum+=n;
}
System.out.println("Result="+sum);
}
}

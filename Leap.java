import java.util.Scanner;
class Leap
{
public static void main(String args[])
{
Scanner sc= new Scanner(System.in);
System.out.println("Enter year");
int a=sc.nextInt();
if(a%4==0)
{
System.out.println("Leap year");
}else
{
System.out.println("not a Leap year");
}}}
import java.util.Scanner;
import java.lang.*;
class Array{
public static void main(String[] args)
{
String ans="";
Scanner sc=new Scanner(System.in);
System.out.println("Enter a string:");
String a= sc.nextLine();
int length = a.Length();
for(int i =a.length - 1; i >=0;i--)
{
ans=ans+a.charAt(i);
}
System.out.println(ans);
}
}
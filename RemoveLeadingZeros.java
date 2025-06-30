import java.lang.*;
import java.util.Scanner;
class RemoveLeadingZeros
{
public static void main(String args[])
{
Scanner scanner = new Scanner(System.in);
String str = scanner.next();
str = str.replaceFirst("^0+", "");
System.out.println(str);
}
}
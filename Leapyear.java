class Leapyear
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
System.out.println("enter a year");
Year = sc.nextInt();
if((year % 4 == 0)||(year % 100 == 0)||(year % 400 ==0))
System.out.println("given year is leapyear");
else
}
System.out.println("given year is not a leapyear");
}


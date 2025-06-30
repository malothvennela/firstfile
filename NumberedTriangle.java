import java.util.Scanner;
public class NumberedTriangle {
	public static void
main(String[] args) {
	Scanner scanner = new scanner(System.in);
System.out.println("Enter the number of rows:");
	int rows = scanner.nextInt();
	int num = 1;
	for(int i=1;i<=rows;i++) {
	for(int j=1;j<=i;j++) {
system.out.print(num +" ");
		num++;
system.put.println();
		}
	}
}
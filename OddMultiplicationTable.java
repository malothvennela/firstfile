public class
OddMultiplicationTable{
public static void main(String[]args){
int number = 5;
int limit = 10;
for(int i = 1,count = 0;count<limit;i += 2){
System.out.println(number+"*"+i+"="+(number*i));
count++;
}
}
}
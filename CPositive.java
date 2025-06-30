public class Positive1
{
public static void mian(String args[]){
int[] number = {5,3,2,0,7,1,8};
int sum =0;
for(int num : number){
if(num > 0){
sum += num;
}
}
System.out.println("Sum of positive numbers :" +sum);
}
}
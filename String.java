public class RemoveLeadingZeros {
    public static void main(String[] args) {
        String str = "000012357";
        str = str.replaceFirst("^0+", "");
        System.out.println(str); 
    }
}



public class ReverseInteger {

  public static void main(String[] args) {
    System.out.println(reverse(1534236469));
  }

  public static int reverse(Object x) {
    String pm = "";
    String tmp = x.toString();
    if (tmp.charAt(0) == '-'){
      pm = "-";
      tmp = tmp.substring(1);
    }
    long result = Long.parseLong(pm + new StringBuffer(tmp).reverse().toString());
    int maxValue = (int)Math.pow(2, 31)-1;
    int minValue = (int)Math.pow(-2, 31);
    System.out.println(result);
    if (!(result <= maxValue) || !(result >= minValue)){
      return 0;
    }
    return (int)result;
  }

}

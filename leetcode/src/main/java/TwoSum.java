public class TwoSum {

  public int[] twoSum(int[] nums, int target) {
    int[] answer = new int[2];
    for (int i = 0; i < nums.length; i++) {
      int a = nums[i];
      int b = 0;
      for (int j = 0; j < nums.length; j++) {
        if (i == j) {
          continue;
        }
        b = nums[j];
        System.out.println(a);
        System.out.println(b);
        if (a + b == target) {
          answer[0] = i;
          answer[1] = j;
          break;
        }
      }
      if (a + b == target) {
        break;
      }
    }
    return answer;
  }
}

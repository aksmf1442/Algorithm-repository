package com.example.demo;

public class LongestCommonPrefix {

  public String longestCommonPrefix(String[] strs) {
    if (strs.length == 0) {
      return "";
    }
    String tmp = "";
    int length = strs[0].length();
    for (String s : strs) {
      length = Math.min(s.length(), length);
    }
    for (int i = 0; i < length; i++) {
      boolean isTrue = true;
      for (int j = 0; j < strs.length - 1; j++) {
        if (strs[j].charAt(i) != strs[j + 1].charAt(i)) {
          isTrue = false;
          break;
        }
      }
      if (!isTrue) {
        break;
      }
      tmp += strs[0].charAt(i);
    }
    return tmp;
  }
}

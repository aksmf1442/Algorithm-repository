package com.example.demo;

public class PalindromeNumber {

  public boolean isPalindrome(int x) {
    StringBuffer tmp = new StringBuffer(Integer.toString(x)).reverse();
    if (Integer.toString(x).equals(tmp.toString())){
      return true;
    }
    return false;
  }
}

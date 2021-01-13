package com.example.demo;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
class PalindromeNumberTest {

  @Test
  @DisplayName("정수 회문 확인 👍")
  void isPalindromeTest(){
    PalindromeNumber p = new PalindromeNumber();
    assertAll(
        () -> assertEquals(true, p.isPalindrome(121),
            () -> "121 통과못함"),
        () -> assertEquals(false, p.isPalindrome(-121),
            () -> "-121 통과못함"),
        () -> assertEquals(false, p.isPalindrome((int)Math.pow(-2,31)),
            () -> "-2^31 통과못함"),
        () -> assertEquals(false, p.isPalindrome((int)Math.pow(2,31)-1),
            () -> "2^31-1 통과못함"),
        () -> assertEquals(true, p.isPalindrome(111),
            () -> "111 통과못함")
    );
  }

}
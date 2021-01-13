package com.example.demo;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class LongestCommonPrefixTest {

  @Test
  @DisplayName("공통 접두사 확인")
  void longestCommonPrefix() {
    LongestCommonPrefix l = new LongestCommonPrefix();
    assertAll(
        () -> assertEquals("fl", l.longestCommonPrefix(new String[]{"flower", "flow", "flight"}),
            () -> "flower, flow, flight 통과실패"),
        () -> assertEquals("", l.longestCommonPrefix(new String[]{"dog", "racecar", "car"}),
            () -> "dog, racecar, car 통과실패"),
        () -> assertEquals("", l.longestCommonPrefix(new String[]{}),
            () -> "비어있는배열 통과실패"),
        () -> assertEquals("dog", l.longestCommonPrefix(new String[]{"dog"}),
            () -> "dog 통과실패")
    );
  }
}
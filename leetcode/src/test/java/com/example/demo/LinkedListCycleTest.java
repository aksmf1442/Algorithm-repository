package com.example.demo;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class LinkedListCycleTest {

  @Test
  void hasCycle() {
    LinkedListCycle LLC = new LinkedListCycle();

    ListNode node1 = new ListNode(3);
    node1.next = new ListNode(2);
    node1.next.next = new ListNode(0);
    node1.next.next.next = new ListNode(4);
    node1.next.next.next.next = node1.next;

    ListNode node2 = new ListNode(3);
    node2.next = new ListNode(2);
    node2.next.next = node2;

    ListNode node3 = new ListNode(1);
    assertAll(
        () -> assertEquals(true, LLC.hasCycle(node1),
            () -> "실패"),
        () -> assertEquals(true, LLC.hasCycle(node2),
            () -> "실패"),
        () -> assertEquals(false, LLC.hasCycle(node3),
            () -> "실패")
    );
  }
}
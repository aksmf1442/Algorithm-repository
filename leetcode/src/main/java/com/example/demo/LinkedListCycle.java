package com.example.demo;

import java.util.ArrayList;
import java.util.List;

public class LinkedListCycle {
  public boolean hasCycle(ListNode head) {
    if (head == null){
      return 
    }
    List<ListNode> tmp = new ArrayList<>();
    ListNode node = head;
    while (!tmp.contains(node)){
      tmp.add(node);
      node = node.next;
      if (node == null){
        return false;
      }
    }
    return true;
  }
}


class ListNode {
   int val;
   ListNode next;
  ListNode(int x) {
       val = x;
       next = null;
   }
}

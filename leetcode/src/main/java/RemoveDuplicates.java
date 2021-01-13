import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

public class RemoveDuplicates {

  public static void main(String[] args) {
    ListNode c = new ListNode(-4);
    ListNode b = new ListNode(-3, c);
    ListNode a = new ListNode(-1, b);
    System.out.println(deleteDuplicates(a));
  }


  public static ListNode deleteDuplicates(ListNode head) {
    HashSet<Integer> result = new HashSet();
    ListNode node = head;

    while (node != null) {
      result.add(node.val);
      node = node.next;
    }
    List<Integer> lst = new ArrayList<>(result);
    Collections.sort(lst);
    ListNode header = null;
    ListNode nod = null;

    for (Integer num : lst) {
      ListNode tmp = nod;
      nod = new ListNode(num);
      if (header == null) {
        header = nod;
        continue;
      }
      tmp.next = nod;
    }

    return header;
  }
}

class ListNode {

  int val;
  ListNode next;

  ListNode() {
  }

  ListNode(int val) {
    this.val = val;
  }

  ListNode(int val, ListNode next) {
    this.val = val;
    this.next = next;
  }
}
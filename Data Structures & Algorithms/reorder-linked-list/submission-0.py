class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ptr = head
        arr = []

        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next

        res = ListNode(0)
        p = res
        n = len(arr)
        half = n // 2

        for i in range(half):
            p.next = ListNode(arr[i])
            p = p.next

            p.next = ListNode(arr[n - i - 1])
            p = p.next

        if n % 2 != 0:
            p.next = ListNode(arr[half])

        temp = head
        t = res.next
        while temp and t:
            temp.val = t.val
            temp = temp.next
            t = t.next

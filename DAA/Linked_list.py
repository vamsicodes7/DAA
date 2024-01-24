class list:
    def __init__(self, value):
        self.value = value
        self.next = None


    def loop(head):
        if not head or not head.next:
            return False
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False








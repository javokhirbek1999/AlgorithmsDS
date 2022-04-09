
class DNode{
    public int value;
    public DNode prev;
    public DNode next;

    public DNode(int value) {
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

public class DoublyLinkedList {

    public DNode head;
    public DNode tail;
    public int size;

    public DoublyLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public void print() {
        DNode current = this.head;

        while (current != null) {
            if (current.next == null) {
                System.out.print(current.value);
            } else {
                System.out.print(current.value + " -> ");
            }
            current = current.next;
        }
    }

    public boolean exists(int value) {
        if (this.head == null) {
            return false;
        }

        DNode current = this.head;

        while (current != null) {
            if (current.value == value) {
                return true;
            }
            current = current.next;
        }

        return false;
    }

    public void prepend(int value) {

        DNode node = new DNode(value);

        if (this.head == null) {
            this.head = node;
            this.tail = node;
        } else {
            node.next = this.head;
            this.head.prev = node;
            this.head = node;
        }

        this.size++;
    }

    public void append(int value) {

        DNode node = new DNode(value);

        if (this.head == null) {
            this.head = node;
            this.tail = node;
        } else {
            node.prev = this.tail;
            this.tail.next = node;
            this.tail = this.tail.next;
        }

        this.size++;
    }

    public int popRight() throws Exception {

        if (this.head == null) {
            throw new Exception("List is empty");
        }

        int tailValue = this.tail.value;

        if (this.head.next == null) {
            this.head = null;
            this.tail = null;
            this.size = 0;
        } else {
            this.tail = this.tail.prev;
            this.tail.next = null;
            this.size--;
        }


        return tailValue;

    }

    public int popLeft() throws Exception {

        if (this.head == null) {
            throw new Exception("List is empty");
        }

        int headValue = this.head.value;

        if (this.head.next == null) {
            this.head = null;
            this.tail = null;
            this.size = 0;
        } else {
            this.head = this.head.next;
            this.head.prev = null;
            this.size--;
        }

        return headValue;
    }

    public void removeByValue(int value) throws Exception {

        if (this.head == null) {
            throw new Exception("List is empty");
        }

        boolean exists = this.exists(value);

        if (!exists) {
            throw new Exception("Value does not exist");
        }

        if (this.head.value == value) {
            this.popLeft();
        } else if (this.tail.value == value) {
            this.popRight();
        } else {

            DNode current = this.head;

            while (current.next.value != value) {
                current = current.next;
            }
            current.next = current.next.next;
            this.size--;
        }
    }

    public void removeByIndex(int index) throws Exception {

        if (this.head == null) {
            throw new Exception("List is empty");
        }

        if (index < 0 || index >= this.size) {
            throw new Exception("Invalid index");
        }

        if (index == 0) {
            this.popLeft();
        } else if (index == this.size-1) {
            this.popRight();
        } else {

            DNode current = this.head;
            int currentIndex = 0;

            while (currentIndex < index-1) {
                current = current.next;
                currentIndex++;
            }

            if (current.next == this.tail) {
                current.next = null;
            } else {
                current.next = current.next.next;
            }
            this.size--;
        }
    }

    public void clear() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

}

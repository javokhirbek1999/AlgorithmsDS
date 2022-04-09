class Node{
    public int value;
    public Node next;

    public Node(int value) {
        this.value = value;
        this.next = null;
    }
}

public class SinglyLinkedList {
    public Node head;
    public Node tail;
    public int size;

    public SinglyLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public void print() {
        Node current = this.head;

        while (current != null) {
            if (current.next == null) {
                System.out.print(current.value);
            } else {
                System.out.print(current.value + " -> ");
            }
            current = current.next;
        }
    }

    public void prepend(int value) {

        Node node = new Node(value);

        if (this.head == null) {
            this.head = node;
            this.tail = node;
        } else {
            node.next = this.head;
            this.head = node;
        }

        this.size++;
    }

    public void append(int value) {

        Node node = new Node(value);

        if (this.head == null) {
            this.head = node;
            this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = this.tail.next;
        }

        this.size++;

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
            return headValue;
        } else {
            this.head = this.head.next;
        }

        this.size--;

        return headValue;
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
            return tailValue;
        }

        Node current = this.head;

        while (current.next != this.tail) {
            current = current.next;
        }
        current.next = null;
        this.tail = current;

        this.size--;

        return tailValue;
    }

    public boolean exists(int value) {
        if (this.head == null) {
            return false;
        }

        Node current = this.head;

        while (current != null) {
            if (current.value == value) {
                return true;
            }
            current = current.next;
        }

        return false;
    }

    public void removeByValue(int value) throws Exception{

        if (this.head == null) {
            throw new Exception("List is empty");
        }

        boolean exists = this.exists(value);

        if (!exists) {
            throw new Exception(value + " does not exist");
        }

        if (this.head.value == value) {
            this.popLeft();
        } else if (this.tail.value == value) {
            this.popRight();
        } else {

            Node current = this.head;

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

            Node current = this.head;
            int currentIndex = 0;

            while (currentIndex < index-1) {
                current = current.next;
                currentIndex++;
            }

            current.next = current.next.next;

            this.size--;
        }
    }

    public void clear() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }
}



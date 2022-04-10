package com.believer.LinkedList;

class Node <T> {
    protected T value;
    protected Node<T> next;

    public Node(T value) {
        this.value = value;
        this.next = null;
    }
}

public class SinglyLinkedList <T> {

    private Node<T> head;
    private Node<T> tail;
    private int size;

    public SinglyLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public void print() {

        Node<T> current = this.head;

        while (current != null) {
            if (current.next == null) {
                System.out.print(current.value);
            } else {
                System.out.print(current.value + " -> ");
            }
            current = current.next;
        }
    }

    public void prepend(T value) {

        Node<T> node = new Node<>(value);

        if (this.head == null) {
            this.head = node;
            this.tail = node;
        } else {
            node.next = this.head;
            this.head = node;
        }

        this.size++;
    }

    public void append(T value) {

        Node<T> node = new Node<>(value);

        if (this.head == null) {
            this.head= node;
            this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = this.tail.next;
        }

        this.size++;
    }

    public T popLeft() throws Exception {

        T popValue = null;

        if (this.head == null) {
            throw new Exception("Cannot pop from empty list");
        } else if (this.head.next == null) {
            popValue = this.head.value;
            this.head = null;
            this.tail = null;
        } else {
            popValue = this.head.value;
            this.head = this.head.next;
        }

        this.size--;

        return popValue;
    }

    public T popRight() throws Exception {


        if (this.head == null) {
            throw new Exception("Cannot pop from empty list");
        }

        T popValue = this.tail.value;

        if (this.head.next == null) {
            this.head = null;
            this.tail = null;
        } else {

            Node<T> current = this.head;

            while (current.next != this.tail) {
                current = current.next;
            }

            this.tail = current;
            this.tail.next = null;
        }

        this.size--;

        return popValue;
    }

    public void remove(int index) throws Exception {

        if (this.head == null) {
            throw new Exception("Cannot remove from empty list");
        }

        if (index < 0 || index > this.size-1) {
            throw new Exception("Invalid index");
        }

        if (index == 0) {
            this.popLeft();
        } else if (index == this.size-1) {
            this.popRight();
        } else {

            Node<T> current = this.head;
            int tempIndex = 0;

            while (tempIndex < index-1) {
                current = current.next;
                tempIndex++;
            }

            current.next = current.next.next;

            this.size--;
        }
    }

    public void remove(T value) throws Exception {

        if (this.head == null) {
            throw new Exception("Cannot remove from empty list");
        }

        if (this.head.value == value) {
            this.popLeft();
        } else if (this.tail.value == value) {
            this.popRight();
        } else {

            Node<T> current = this.head;

            while (current.next.value != value) {
                current = current.next;
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

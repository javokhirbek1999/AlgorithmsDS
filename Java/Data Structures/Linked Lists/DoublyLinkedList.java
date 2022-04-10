package com.believer.LinkedList;

class DNode <T> {
    protected T value;
    protected DNode<T> prev;
    protected DNode<T> next;

    public DNode(T value) {
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

public class DoublyLinkedList <T> {

    private DNode<T> head;
    private DNode<T> tail;
    private int size;

    public DoublyLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public void print() {

        DNode<T> current = this.head;

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

        DNode<T> node = new DNode<>(value);

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

    public void append(T value) {

        DNode<T> node = new DNode<>(value);

        if (this.head == null) {
            this.head= node;
            this.tail = node;
        } else {
            node.prev = this.tail;
            this.tail.next = node;
            this.tail = this.tail.next;
        }

        this.size++;
    }

    public T popLeft() throws Exception {

        if (this.head == null) {
            throw new Exception("Cannot pop from empty list");
        }

        T popValue = this.head.value;

        if (this.head.next == null) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = this.head.next;
        }

        this.size--;

        return popValue;
    }

    public T popRight() throws Exception {


        if (this.head == null) {
            throw new Exception("Cannot pop from empty list");
        }
        T popValue = this.head.value;

        if (this.head.next == null) {
            this.head = null;
            this.tail = null;
        } else {
            this.tail = this.tail.prev;
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

            DNode<T> current = this.head;
            int tempIndex = 0;

            while (tempIndex < index-1) {
                current = current.next;
                tempIndex++;
            }
            current.next = current.next.next;
            current.next.prev = null;

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

            DNode<T> current = this.head;

            while (current.next.value != value) {
                current = current.next;
            }

            current.next = current.next.next;
            current.next.prev = null;

            this.size--;
        }
    }

    public void clear() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

}

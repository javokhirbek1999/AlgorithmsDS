package com.believer.StackAndQueue;

class Node <T> {
    protected T value;
    protected Node<T> next;

    public Node(T value) {
        this.value = value;
    }
}

class SinglyLinkedList <T> {

    protected Node<T> head;
    protected Node<T> tail;
    protected int size;

    public SinglyLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
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

}

public class LLQueue<T> {

    private SinglyLinkedList<T> queue;
    private int size;

    public LLQueue() {
        this.queue = new SinglyLinkedList<>();
        this.size = 0;
    }

    public void print() {

        Node<T> current = this.queue.head;

        while (current != null) {
            System.out.print(current.value + " ");
            current = current.next;
        }
    }

    public boolean isEmpty() {
        return this.size == 0;
    }

    public void enQueue(T value) {

        this.queue.append(value);
        this.size++;

    }

    public T deQueue() throws Exception {

        if (this.size == 0) {
            throw new Exception("Cannot remove from empty queue");
        }

        return this.queue.popLeft();
    }
}

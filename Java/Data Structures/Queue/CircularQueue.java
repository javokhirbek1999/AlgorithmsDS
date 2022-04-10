package com.believer.StackAndQueue;

class QNode<T> {
    protected T value;
    protected QNode<T> next;

    public QNode(T value) {
        this.value = value;
    }
}

class QSinglyLinkedList <T> {

    protected QNode<T> head;
    protected QNode<T> tail;
    protected int size;

    public QSinglyLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public void append(T value) {

        QNode<T> node = new QNode<>(value);

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

public class CircularQueue<T> {

    private QSinglyLinkedList<T> circularQueue;
    private int size;
    private int maxSize;

    public CircularQueue(int maxSize) {
        this.circularQueue = new QSinglyLinkedList<>();
        this.size = 0;
        this.maxSize = maxSize;
    }

    public void print() {

        QNode<T> current = this.circularQueue.head;

        while (current != null) {
            if (current.next == null) {
                System.out.print(current.value);
            } else {
                System.out.print(current.value + " ");
            }
            current = current.next;
        }
    }

    public boolean isEmpty() {
        return this.size == 0;
    }

    public boolean isFull() {
        return this.size == this.maxSize;
    }

    public void enQueue(T value) throws Exception {

        if (this.isFull()) {
            throw new Exception("Queue is full");
        }

        this.circularQueue.append(value);
        this.size++;
    }

    public T deQueue() throws Exception {

        if (this.isEmpty()) {
            throw new Exception("Queue is empty");
        }

        this.size--;
        return this.circularQueue.popLeft();
    }


}

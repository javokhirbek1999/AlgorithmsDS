package com.believer.StackAndQueue;

import java.util.ArrayList;

public class Queue <T> {

    private ArrayList<T> queue;

    public Queue() {
        this.queue = new ArrayList<>();
    }

    public boolean isEmpty() {
        return this.queue.size() == 0;
    }

    public void enQueue(T value) {

        this.queue.add(value);
    }

    public T deQueue() throws Exception {

        if (this.isEmpty()) {
            throw new Exception("Queue is Empty");
        }

        T temp = this.queue.get(0);
        this.queue.remove(0);

        return temp;
    }
}

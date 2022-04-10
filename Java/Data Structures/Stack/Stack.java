package com.believer.StackAndQueue;

import java.util.ArrayList;

public class Stack<T> {

    private ArrayList<T> stack;

    public Stack() {
        this.stack = new ArrayList<>();
    }

    public boolean isEmpty() {
        return this.stack.size() == 0;
    }

    public void push(T value) {
        this.stack.add(value);
    }

    public T pop() {

        if (this.stack.isEmpty()) {
            System.out.println("Cannot Pop from Empty Stack");
        }

        int size = this.stack.size();

        T value = this.stack.get(size-1);
        this.stack.remove(this.stack.size()-1);

        return value;
    }

    public void print() {
        int size = this.stack.size();
        for (int i = size-1; i>-1; i--) {
            System.out.println(this.stack.get(i));
        }
    }

}

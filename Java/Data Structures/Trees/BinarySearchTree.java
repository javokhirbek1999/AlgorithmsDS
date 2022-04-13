package com.believer.Trees;

import java.util.ArrayList;

public class BST {
    private int value;
    private BST left;
    private BST right;

    public BST(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    public void preOrder(BST root) {
        if (root != null) {
            System.out.println(root.value);
            this.preOrder(root.left);
            this.preOrder(root.right);
        }
    }

    public void inOrder(BST root) {
        if (root != null) {
            this.inOrder(root.left);
            System.out.println(root.value);
            this.inOrder(root.right);
        }
    }

    public void postOrder(BST root) {
        if (root != null) {
            this.postOrder(root.left);
            System.out.println(root.value);
            this.postOrder(root.right);
        }
    }

    public void levelOrder(BST root) {
        if (root != null) {
            ArrayList<BST> queue = new ArrayList<>();
            queue.add(root);
            while (queue.size()>0) {
                BST node = queue.remove(0);

                System.out.print(node.value + " ");

                if (node.left != null) {
                    queue.add(node.left);
                }

                if (node.right != null) {
                    queue.add(node.right);
                }
            }
        }
    }

    public void insert(BST root, int value) {
        if (root == null) {
            root = new BST(value);
        } else {
            if (value < root.value) {
                if (root.left == null) {
                    root.left = new BST(value);
                } else {
                    this.insert(root.left, value);
                }
            } else {
                if (root.right == null) {
                    root.right = new BST(value);
                } else {
                    this.insert(root.right, value);
                }
            }
        }
    }

    public BST findMinNode(BST root) {
        if (root == null) {
            return null;
        }

        BST current = root;

        while (current.left != null) {
            current = current.left;
        }

        return current;
    }

    public int successor(BST root) {
        root = root.right;

        while (root.left != null) {
            root = root.left;
        }

        return root.value;
    }

    public int predecessor(BST root) {
        root = root.left;

        while (root.right != null) {
            root = root.right;
        }

        return root.value;
    }

    public BST remove(BST root, int value) throws Exception {
        if (root == null) {
            throw new Exception("Cannot remove from empty tree");
        } else {
            if (value < root.value) {
                root.left = this.remove(root.left, value);
            } else if (value > root.value) {
                root.right = this.remove(root.right, value);
            } else {
                if (root.left == null && root.right == null) {
                    root = null;
                } else if (root.right != null) {
                    root.value = this.successor(root);
                    root.right = this.remove(root.right, root.value);
                } else {
                    root.value = this.predecessor(root);
                    root.left = this.remove(root.left, root.value);
                }
            }
        }
        return root;
    }
}

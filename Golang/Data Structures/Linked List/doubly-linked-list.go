type Any interface {
	int | int8 | int16 | int32 | int64 | uint | uint8 | uint16 | uint32 | uint64 | float32 | float64 | string
}

type Node[any Any] struct {
	Val  any
	Prev *Node[any]
	Next *Node[any]
}

type DoublyLinkedList[any Any] struct {
	Head *Node[any]
	Tail *Node[any]
	Size int
}

func (this *DoublyLinkedList[any]) Constructor() DoublyLinkedList[any] {
	doublyLinkedList := &DoublyLinkedList[any]{nil, nil, 0}

	return *doublyLinkedList
}

func (this *DoublyLinkedList[any]) getSize() int {
	return this.Size
}

func (this *DoublyLinkedList[any]) append(val any) {
	node := &Node[any]{val, nil, nil}

	if this.Head == nil {
		this.Head = node
		this.Tail = node
	} else {
		node.Prev = this.Tail
		this.Tail.Next = node
		this.Tail = this.Tail.Next
	}

	this.Size++
}

func (this *DoublyLinkedList[any]) prepend(val any) {
	node := &Node[any]{val, nil, nil}

	if this.Head == nil {
		this.Head = node
		this.Tail = node
	} else {
		this.Head.Prev = node
		node.Next = this.Head
		this.Head = node
	}

	this.Size++
}

func (this *DoublyLinkedList[any]) insert(val any, index int) {
	if index < 0 || index > this.Size {
		return
	}

	node := &Node[any]{val, nil, nil}

	if index == 0 {
		this.prepend(val)
	} else if index == this.Size {
		this.append(val)
	} else {
		current := this.Head
		i := 0

		for i < index-1 {
			current = current.Next
			i++
		}
		current.Next.Prev = node
		node.Next = current.Next
		node.Prev = current
		current.Next = node

		this.Size++
	}
}

func (this *DoublyLinkedList[any]) Print() {
	if this.Size == 0 {
		fmt.Println("[]")
	}

	current := this.Head

	for current != nil {
		fmt.Print(current.Val)
		if current.Next != nil {
			fmt.Print(" ")
		}
		current = current.Next
	}
	fmt.Println()
}

func (this *DoublyLinkedList[any]) PopRight() any {

	var errorValue int = -1

	if this.Size == 0 {
		return any(rune(errorValue))
	}

	temp := this.Head.Val

	if this.Size == 1 {
		this.Head = nil
		this.Tail = nil
		this.Size = 0
	} else {
		temp = this.Tail.Val
		this.Tail = this.Tail.Prev
		this.Tail.Next = nil
		this.Size--
	}

	return temp
}

func (this *DoublyLinkedList[any]) PopLeft() any {

	var errorValue int = -1

	if this.Size == 0 {
		return any(rune(errorValue))
	}

	temp := this.Head.Val

	if this.Size == 1 {
		this.Head = nil
		this.Tail = nil
		this.Size = 0
	} else {
		this.Head = this.Head.Next
		this.Size--
	}

	return temp
}

func (this *DoublyLinkedList[any]) Remove(index int) {

	if this.Size == 0 {
		fmt.Println("List is Empty!")
		return
	}

	if index < 0 || index > this.Size {
		fmt.Println("Invalid Index")
		return
	}

	if index == 0 {
		this.PopLeft()
	} else if index == this.getSize()-1 {
		this.PopRight()
	} else {

		current := this.Head

		currentIndex := 0

		for currentIndex < index-1 {
			current = current.Next
			currentIndex++
		}
		current.Next = current.Next.Next
		this.Size--
	}
}

func (this *DoublyLinkedList[any]) Clear() {
	this.Head = nil
	this.Tail = nil
	this.Size = 0
}

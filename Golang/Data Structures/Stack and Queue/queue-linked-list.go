type Any interface {
	int | int8 | int16 | int32 | int64 | uint | uint8 | uint16 | uint32 | uint64 | float32 | float64 | string
}

type Node[any Any] struct {
	Val  any
	Prev *Node[any]
	Next *Node[any]
}

type Queue[any Any] struct {
	Head *Node[any]
	Tail *Node[any]
	Size int
}

func (this *Queue[any]) Constructor() Queue[any] {

	doublyLinkedList := &Queue[any]{}

	return *doublyLinkedList
}

func (this *Queue[any]) EnQueue(value any) {

	node := &Node[any]{value, nil, nil}

	if this.Size == 0 {
		this.Head = node
		this.Tail = node
		this.Size = 1
	} else {
		node.Prev = this.Tail
		this.Tail.Next = node
		this.Tail = this.Tail.Next
		this.Size++
	}
}

func (this *Queue[any]) DeQueue() {

	if this.Size == 0 {
		fmt.Printf("ERROR: Queue is EMPTY !")
		return
	}

	this.Head = this.Head.Next
	this.Size--
}

func (this *Queue[any]) getSize() int {
	return this.Size
}

func (this *Queue[any]) isEmpty() bool {
	return this.Size == 0
}

func (this *Queue[any]) Print() {
	if this.Size == 0 {
		return
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

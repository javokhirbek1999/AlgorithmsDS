type Any interface {
	int | int8 | int16 | int32 | int64 | uint | uint8 | uint16 | uint32 | uint64 | float32 | float64 | string
}

type Node[any Any] struct {
	Val  any
	Prev *Node[any]
	Next *Node[any]
}

type Stack[any Any] struct {
	Head *Node[any]
	Tail *Node[any]
	Size int
}

func (this *Stack[any]) Constructor() Stack[any] {
	stack := &Stack[any]{nil, nil, 0}

	return *stack
}

func (this *Stack[any]) Push(value any) {

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

func (this *Stack[any]) Pop() any {

	var errorValue int = -1

	if this.Size == 0 {
		return any(rune(errorValue))
	}

	temp := this.Tail.Val
	this.Tail = this.Tail.Prev
	this.Size--

	return temp
}

func (this *Stack[any]) Top() any {

	var errorValue int = -1

	if this.Size == 0 {
		return any(rune(errorValue))
	}

	return this.Head.Val
}

func (this *Stack[any]) isEmpty() bool {
	return this.Size == 0
}

func (this *Stack[any]) Print() {

	if this.Size == 0 {
		fmt.Println("ERROR: Stack is EMPTY!")
		return
	}

	current := this.Tail

	for current != nil {
		fmt.Println(current.Val)
		current = current.Prev
	}
}

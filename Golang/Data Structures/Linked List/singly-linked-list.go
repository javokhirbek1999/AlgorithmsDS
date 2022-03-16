type Node struct {
	Value int
	Next  *Node
}

type List struct {
	Head *Node
	Tail *Node
	Size int
}

func (list *List) Init() *List {

	ll := &List{nil, nil, 0}

	return ll
}

func (list *List) size() int {
	return list.Size
}

func (list *List) print() {
	current := list.Head
	if list.Size == 0 {
		return
	}
	for current != nil {
		fmt.Printf("%v ", current.Value)
		current = current.Next
	}
}

func (list *List) prepend(val int) {
	node := &Node{val, nil}

	if list.Head == nil {
		list.Head = node
		list.Tail = node
	} else {
		node.Next = list.Head
		list.Head = node
	}

	list.Size++
}

func (list *List) append(val int) {
	node := &Node{val, nil}

	if list.Size == 0 {
		list.Head = node
		list.Tail = node
	} else {
		list.Tail.Next = node
		list.Tail = list.Tail.Next
	}

	list.Size++
}

func (list *List) popLeft() {

	if list.Size > 0 {
		list.Head = list.Head.Next
		list.Size--
	}
}

func (list *List) popRight() {

	if list.Size > 0 {
		current := list.Head

		for current.Next != list.Tail {
			current = current.Next
		}
		list.Tail = current
		current.Next = nil
		list.Size--
	}
}

func (list *List) insert(value, index int) {

	if index > list.Size {
		fmt.Println("ERROR: Index of insert poisiton must be less than the size of the Linked List")
	}

	if index < 0 {
		fmt.Println("Error: Index of insert position must be greater than 0")
	}

	if index == 0 {
		list.prepend(value)
	} else if index == list.Size {
		list.append(value)
	} else {
		current := list.Head
		i := 0
		for i < index-1 {
			i++
			current = current.Next
		}
		node := &Node{value, nil}
		nextNode := current.Next
		node.Next = nextNode
		current.Next = node
		list.Size++
	}
}

func (list *List) remove(index int) {

	if index >= list.Size {
		fmt.Println("ERROR: Index must be less than the size of Linked List")
	}

	if index < 0 {
		fmt.Println("ERROR: Index must be greater than 0")
	}

	if index == 0 {
		list.popLeft()
	} else if index == list.Size-1 {
		list.popRight()
	} else {

		current := list.Head
		i := 0
		for i < index-1 {
			current = current.Next
			i++
		}

		current.Next = current.Next.Next
		list.Size--
	}

}

func (list *List) clear() {
	list.Head = nil
	list.Tail = nil
	list.Size = 0
}

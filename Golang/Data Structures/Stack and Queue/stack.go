type Any interface {
	int | int8 | int16 | int32 | int64 | uint | uint8 | uint16 | uint32 | uint64 | string
}

type Stack[any Any] struct {
	Stack []any
	Size  int
}

func (this *Stack[any]) Constructor() Stack[any] {

	stack := &Stack[any]{[]any{}, 0}

	return *stack
}

func (this *Stack[any]) GetSize() int {
	return this.Size
}

func (this *Stack[any]) Push(val any) {
	this.Stack = append(this.Stack, val)
	this.Size++
}

func (this *Stack[any]) Pop() any {

	var errorValue int = -1

	if this.Size == 0 {
		fmt.Println("Stack is empty!")
		return any(rune(errorValue))
	}
	top := this.Stack[this.GetSize()-1]
	this.Stack = this.Stack[:this.GetSize()-1]
	this.Size--

	return top
}

func (this *Stack[any]) Top() any {

	var errorValue int = -1

	if this.Size == 0 {
		fmt.Println("Stack is empty !")
		return any(rune(errorValue))
	}

	return this.Stack[this.GetSize()-1]
}

func (this *Stack[any]) isEmpty() bool {
	return this.Size == 0
}

func (this *Stack[any]) Print() {

	for i := this.GetSize() - 1; i > -1; i-- {
		fmt.Println(this.Stack[i])
	}
}

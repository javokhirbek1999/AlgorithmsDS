type Any interface {
	int | int8 | int16 | int32 | int64 | uint | uint8 | uint16 | uint32 | uint64 | float32 | float64 | string
}

type Queue[any Any] struct {
	queue []any
	size  int
}

func (this *Queue[any]) Constructor() Queue[any] {
	queue := &Queue[any]{[]any{}, 0}

	return *queue
}

func (this *Queue[any]) Size() int {
	return this.size
}

func (this *Queue[any]) EnQueue(value any) {

	this.queue = append(this.queue, value)
	this.size++
}

func (this *Queue[any]) DeQueue() {

	this.queue = this.queue[1:]
	this.size--
}

func (this *Queue[any]) isEmpty(value any) bool {
	return this.size == 0
}

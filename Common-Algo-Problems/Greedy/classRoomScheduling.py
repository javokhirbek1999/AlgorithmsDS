# The classroom scheduling problem
# Suppose you have a classroom and you want to hold as many classes as possible 
# __________________________
#| class | start   |  end  	|
#|_______|_________|________|
#| Art   | 9:00 am | 10:30am|
#|_______|_________|________|
#| Eng	 | 9:30am  | 10:30am|
#|_______|_________|________|
#| Math  |  10 am  | 11 am  |
#|_______|_________|________|
#|	CS	 |  10:30am| 11.30am|
#|_______|_________|________|
#| Music | 11 am   | 12 pm  |
#|_______|_________|________|
#|
def schedule(classes):
	possible_classes = []
	possible_classes.append(classes[0])
  
	for i in range(2,len(classes)):
		if possible_classes[-1][1]<=classes[i][0]:
			possible_classes.append(classes[i])

	return possible_classes

# An animal shelter which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat(and will receive the oldest animal of that type). They cannot select any specific animal.


class Queue : 
    def __init__(self) :
        self.animals = []

    def addAnimal(self,typeOfAnimal) :
        if(typeOfAnimal != "dog" and typeOfAnimal != "cat") :
            print("You can only add a dog or a cat")
            return
        self.animals.append(typeOfAnimal)
        return

    def dequeue(self) :
        if len(self.animals) == 0 :
            print("The queue is empty")
        else :
            return self.animals.pop(0)

    def dequeueDog(self) :
        if len(self.animals) == 0 :
            print("Queue is empty")
            return
        for i,animal in enumerate(self.animals) :
            if animal == "dog" :
                return self.animals.pop(i)

    def dequeueCat(self) :
        if len(self.animals) == 0 :
            print("Queue is empty")
            return
        for i,animal in enumerate(self.animals) :
            if animal == "cat" :
                return self.animals.pop(i)

q = Queue()
q.addAnimal("dog")
q.addAnimal("cat")
q.addAnimal("dog")
q.addAnimal("dog")
q.addAnimal("cat")
q.addAnimal("cat")
q.addAnimal("dog")
q.addAnimal("cat")
q.addAnimal("horse")
print(q.dequeueCat())
print(q.dequeue())
print(q.dequeueDog())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())


from fifo_animal_shelter import FifoAnimalShelter


def test_enqueue():
  shelter = FifoAnimalShelter()
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Cat')
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Cat')

  assert shelter.front.value == "Dog"
  assert shelter.rear.value == "Cat"
  assert shelter.length == 5

def test_dequeue_no_pref():
  shelter = FifoAnimalShelter()
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Cat')
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Cat')

  assert shelter.dequeue_dog_or_cat() == "Dog"

def test_dequeue_with_pref():
  shelter = FifoAnimalShelter()
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Cat')
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Cat')

  shelter.dequeue_dog_or_cat('Cat')
  assert shelter.front.next.value == "Dog"
  assert shelter.length == 4

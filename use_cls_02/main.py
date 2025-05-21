
class Counter:
    class_count = 0 # Class Variable/ Attribute

    # Constructor
    def __init__(self):
        Counter.class_count += 1 # Plus class_count By One Whenever New Instance of Class will Be Created

    # Class Method to Show Counts
    @classmethod
    def show_counts(cls):
        print(f'Total Objects Created: {cls.class_count}')

object1 = Counter() # object 1
object2 = Counter()
object3 = Counter()
object4 = Counter() # object 4

Counter.show_counts() # output: 4


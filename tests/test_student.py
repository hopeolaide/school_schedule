from school_schedule.student import Student

def test_check_attributes_correctly_set():
    # arrange

    # act
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )
    # assert
    #assert student
    assert student.name == "Quinn"
    assert student.grade == "junior"
    assert student.classes == [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
    ]
def test_add_subject():
    #arange

    #assert
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )
    student.add_class("Art")
    assert len(student.classes) == 7    
    assert student.classes == [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition",
                    "Art"
                ]   

def test_get_num_classes():
    #arrange

    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

    # act 
    num_classes = student.get_num_classes()
    # assert
    assert num_classes == 6
         
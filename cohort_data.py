"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    houses = set()

    hagworts_data = open(filename, "r")

    for student in hagworts_data:
      house = student[:-1].split("|")[2]
      if house:
        houses.add(house)
    
    return houses

all_houses('cohort_data.txt')


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """
    hagworts_data = open(filename)

    students = []

    for line in hagworts_data:
      first, last, _, _, cohort_name = line.rstrip().split("|")
      
      if cohort_name not in ("I", "G") and cohort in ("All", cohort_name):
        students.append(f'{first} {last}')

    return sorted(students)
    
students_by_cohort("cohort_data.txt")


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    full_list = []

    hagworts_data = open(filename)
    hagworts_data

    for line in hagworts_data:
      first, last, house, _, cohort = line.rstrip().split("|")
      name = f'{first} {last}'

      if house:
        if house == "Dumbledore's Army":
          dumbledores_army.append(name)
        if house == "Gryffindor":
          gryffindor.append(name)
        if house == "Hufflepuff":
          hufflepuff.append(name)
        if house == "Ravenclaw":
          ravenclaw.append(name)
        if house == "Slytherin":
          slytherin.append(name)
      else:
        if cohort == "G":
          ghosts.append(name)
        if cohort == "I":
          instructors.append(name)

    full_list.append(sorted(dumbledores_army))
    full_list.append(sorted(gryffindor))
    full_list.append(sorted(hufflepuff))
    full_list.append(sorted(ravenclaw))
    full_list.append(sorted(slytherin))
    full_list.append(sorted(ghosts))
    full_list.append(sorted(instructors))

    return full_list

all_names_by_house("cohort_data.txt")

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    all_data = []

    hagworts_data = open(filename)
    
    for line in hagworts_data:
     first, last, house, instructor, cohort = line.rstrip().split("|")
     name = f'{first} {last}'

     hagworts_tuple = (name, house, instructor, cohort)
     
     all_data.append(hagworts_tuple)

    return all_data

all_data('cohort_data.txt')

def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    hagworts_data = open(filename)

    for data in hagworts_data:
      first, last, _, _, cohort = data.rstrip().split("|")
      full_name = f'{first} {last}'
      if name == full_name:
         return cohort
      

get_cohort_for("cohort_data.txt", "Dennis Creevey")

def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    hagworts_data = open(filename)
    
    names = []

    duplicates = []

    for data in hagworts_data:
      _, last, _, _, _ = data.rstrip().split("|")
      if last not in names:
        names.append(last)
      elif last in names:
        duplicates.append(last)
    return set(duplicates)

find_duped_last_names("cohort_data.txt")


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """


    housemates = set()

    for student in all_data(filename):
      full_name, house, _, cohort = student

      if full_name == name:
        selected_student = student
        selected_student_house = house
        selected_student_cohort = cohort
      
        if selected_student:

          for full_name, house, _, cohort in all_data(filename):
            if house == selected_student_house and cohort == selected_student_cohort and full_name != name:
              housemates.add(full_name)
    return housemates

sorted(get_housemates_for("cohort_data.txt", "Orla Quirke"))

##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')


  # housemates = set()

    # for line in hagworts_data:
    #   first, last, house, _, cohort = line.rstrip().split("|")
    #   full_name = f'{first} {last}'
      
    #   if name == full_name:
    #     selected_student = full_name
    #     student_house = house
    #     student_cohort = cohort

    #   for student in full_name, house, cohort:
    #     if house == student_house and cohort == student_cohort and full_name != selected_student:
    #       housemates.add(full_name)

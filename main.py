# importing copy module
import copy

from itertools import permutations

number_of_agents, number_of_distinct_skills = input().split()
number_of_agents = int(number_of_agents)
number_of_distinct_skills = int(number_of_distinct_skills)

required_skills = input()
required_skills_list = [str(i) for i in required_skills.split(' ')]
required_skills_set = set(required_skills_list)

#trying a list
agents = []

for i in range(0, number_of_agents):
    skills_num = values = input()
    skills = input()
    skills_list = [i for i in skills.split(' ')]
    agents.append(skills_list)

#now doing brute force
minimum_people = number_of_agents   #watch out this could cause errors


def permute(lst, _required_skills_set, _number_of_distinct_skills, f=0):
    # put required skills into set, recurse through and check if it adds up to number of distinct_skills

    global minimum_people

    # base case - no more swaps we can make
    if f >= len(lst):

        current_skills_set = set()
        person_num = 0

        for i in range(0, len(lst)):
            person_num = person_num + 1

            #Optimization 1 - stop if the number of people is greater than the smallest number discovered so far
            if person_num >= minimum_people:
                break;
            else:
                for j in range(0, len(lst[i])):
                    if lst[i][j] in _required_skills_set:
                        current_skills_set.add(lst[i][j])

                if len(current_skills_set) == _number_of_distinct_skills:
                    minimum_people = person_num
                    return
        return

    for s in range(f, len(lst)):
        lst[f], lst[s] = lst[s], lst[f]
        permute(lst, _required_skills_set, _number_of_distinct_skills, f + 1)
        lst[f], lst[s] = lst[s], lst[f]




def permute2(lst, _required_skills_set, _number_of_distinct_skills,f=0):
    # put required skills into set, recurse through and check if it adds up to number of distinct_skills

    global minimum_people

    # base case - no more swaps we can make
    if f >= len(lst):
        current_skills_set = set()
        person_num = 0

        for i in range(0, len(lst)):
            person_num = person_num + 1

            # Optimization 1 - stop if the number of people is greater than the smallest number discovered so far
            if person_num >= minimum_people:
                break;
            else:
                for j in range(0, len(lst[i])):
                    if lst[i][j] in _required_skills_set:
                        current_skills_set.add(lst[i][j])

                if len(current_skills_set) == _number_of_distinct_skills:
                    minimum_people = person_num
                    return
        return

#from 0 to length of the list
    for s in range(f, len(lst)):
        #mix of list
        lst[f], lst[s] = lst[s], lst[f]

        #calculate the permutations
        current_skills_set = set()
        person_num = 0

        for i in range(0, len(lst)):
            person_num = person_num + 1

            # Optimization 1 - stop if the number of people is greater than the smallest number discovered so far
            if person_num >= minimum_people:
                break;
            else:
                for j in range(0, len(lst[i])):
                    if lst[i][j] in _required_skills_set:
                        current_skills_set.add(lst[i][j])

                if len(current_skills_set) == _number_of_distinct_skills:
                    minimum_people = person_num
                    return
        if person_num >= minimum_people:
            permute(lst, _required_skills_set, _number_of_distinct_skills, f + 1)
            lst[f], lst[s] = lst[s], lst[f]
            return
        else:
            permute(lst, _required_skills_set, _number_of_distinct_skills, f + 1)
            lst[f], lst[s] = lst[s], lst[f]



def permute3(lst, _required_skills_set, _number_of_distinct_skills, f=0):
    # put required skills into set, recurse through and check if it adds up to number of distinct_skills

    global minimum_people

    # base case - no more swaps we can make
    if f >= len(lst):
        '''current_skills_set = set()
        person_num = 0

        for i in range(0, len(lst)):
            person_num = person_num + 1

            # Optimization 1 - stop if the number of people is greater than the smallest number discovered so far
            if person_num >= minimum_people:
                break;
            else:
                for j in range(0, len(lst[i])):
                    if lst[i][j] in _required_skills_set:
                        current_skills_set.add(lst[i][j])

                if len(current_skills_set) == _number_of_distinct_skills:
                    minimum_people = person_num
                    return'''
        return

# from 0 to length of the list
    for s in range(f, len(lst)):
        # mix of list
        lst[f], lst[s] = lst[s], lst[f]

        # calculate the permutations
        current_skills_set = set()
        person_num = 0

        for i in range(0, f):
            person_num = person_num + 1

            # Optimization 1 - stop if the number of people is greater than the smallest number discovered so far
            if person_num >= minimum_people:
                break;
            else:
                for j in range(0, len(lst[i])):
                    if lst[i][j] in _required_skills_set:
                        current_skills_set.add(lst[i][j])

                if len(current_skills_set) == _number_of_distinct_skills:
                    minimum_people = person_num
                    return
        if person_num >= minimum_people:
            return
        else:
            permute3(lst, _required_skills_set, _number_of_distinct_skills, f + 1)
            lst[f], lst[s] = lst[s], lst[f]

# make sure the change the permute at the bottom
# currently the best one - gets you 240/400
def permute4(lst, _required_skills_set, _number_of_distinct_skills, current_skills_set, person_num, f=0):
    # put required skills into set, recurse through and check if it adds up to number of distinct_skills

    global minimum_people

    # base case - no more swaps we can make
    if f >= len(lst):
        return

# from 0 to length of the list
    for s in range(f, len(lst)):
        # mix of list
        lst[f], lst[s] = lst[s], lst[f]

        current_skills_set2 = set(current_skills_set)

        # Optimization 1 - stop if the number of people is greater than the smallest number discovered so far
        if person_num >= minimum_people:
            lst[f], lst[s] = lst[s], lst[f]
        else:
            for j in range(0, len(lst[f])):
                if lst[f][j] in _required_skills_set:
                    current_skills_set2.add(lst[f][j])

            if len(current_skills_set2) == _number_of_distinct_skills:
                minimum_people = person_num
            permute4(lst, _required_skills_set, _number_of_distinct_skills, current_skills_set2, person_num+1, f + 1)
            lst[f], lst[s] = lst[s], lst[f]


def permute5(lst, _required_skills_set, _number_of_distinct_skills,person_num, current_skills_set, f=0):
    # put required skills into set, recurse through and check if it adds up to number of distinct_skills

    global minimum_people

    # base case - no more swaps we can make
    if f >= len(lst):
        return

# from 0 to length of the list
    for s in range(f, len(lst)):
        # mix of list
        lst[f], lst[s] = lst[s], lst[f]

        if person_num >= minimum_people:
            return
        else:
            current_skills_set2 = set(current_skills_set)
            for j in range(0, len(lst[f])):
                if lst[f][j] in _required_skills_set:
                    current_skills_set2.add(lst[i][j])

                if len(current_skills_set2) == _number_of_distinct_skills:
                    minimum_people = person_num

            if ((len(current_skills_set2) + len(lst[f+1])) < _number_of_distinct_skills):
                return
            else:
                permute3(lst, _required_skills_set, _number_of_distinct_skills, person_num + 1, current_skills_set2,
                         f + 1)
                lst[f], lst[s] = lst[s], lst[f]

            #elif((len(current_skills_set2) + len(lst[f+1]) + len(lst[f+2])) < _number_of_distinct_skills):

            permute3(lst, _required_skills_set, _number_of_distinct_skills, person_num + 1, current_skills_set2, f + 1)
            lst[f], lst[s] = lst[s], lst[f]


def permute6(lst, _required_skills_set, _number_of_distinct_skills, current_skills_set, person_num, f=0):
    # put required skills into set, recurse through and check if it adds up to number of distinct_skills

    global minimum_people

    # base case - no more swaps we can make
    if f >= len(lst):
        return

# from 0 to length of the list
    for s in range(f, len(lst)):
        # mix of list
        lst[f], lst[s] = lst[s], lst[f]

        current_skills_set2 = set(current_skills_set)

        # Optimization 1 - stop if the number of people is greater than the smallest number discovered so far
        if person_num >= minimum_people:
            lst[f], lst[s] = lst[s], lst[f]
        else:
            for j in range(0, len(lst[f])):
                if lst[f][j] in _required_skills_set:
                    current_skills_set2.add(lst[f][j])

            if len(current_skills_set2) == _number_of_distinct_skills:
                minimum_people = person_num

            # Optimization - dont permute if it wont give you an answer
            if f+1 < len(lst) and len(current_skills_set2) + len(lst[f+1]) < _number_of_distinct_skills:
                return
            elif f+2 < len(lst) and len(current_skills_set2) + len(lst[f+1]) + len(lst[f+2]) < _number_of_distinct_skills:
                return
            else:
                permute6(lst, _required_skills_set, _number_of_distinct_skills, current_skills_set2, person_num + 1,
                         f + 1)
                lst[f], lst[s] = lst[s], lst[f]



#optimization 2 - remove subsets
agents2 = agents[:]
for m in agents:
    for n in agents:
        if set(m).issubset(set(n)) and m != n:
            agents2.remove(m)
            break


#optimization 3 - sort list so the agents that have the most skills are put in first
agents2.sort(key=len, reverse=True)

#permute(agents2, required_skills_set, number_of_distinct_skills)
#permute3(agents2, required_skills_set, number_of_distinct_skills)

current_skills_set = set()
person_num = 1
#permute4(agents2, required_skills_set, number_of_distinct_skills, current_skills_set, person_num)
permute6(agents2, required_skills_set, number_of_distinct_skills, current_skills_set, person_num)

print(minimum_people)




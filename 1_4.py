# importing copy module
import copy

from itertools import permutations

# https://www.youtube.com/watch?v=mYBBaVnCthc&t=614s - citation for the recursion for the permutation
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

        # Optimization 1 - stop if the number of people is greater than the smallest number discovered so far
        if person_num >= minimum_people:
            lst[f], lst[s] = lst[s], lst[f]
        else:
            current_skills_set2 = set(current_skills_set)

            for j in range(0, len(lst[f])):
                if lst[f][j] in _required_skills_set:
                    current_skills_set2.add(lst[f][j])

            if len(current_skills_set2) == _number_of_distinct_skills:
                minimum_people = person_num
            permute4(lst, _required_skills_set, _number_of_distinct_skills, current_skills_set2, person_num+1, f + 1)
            lst[f], lst[s] = lst[s], lst[f]

# Need a function that will check if the remainig answers will give you a solution for the funciton
def backtracking(lst, _required_skills_set, number_of_distinct_skills, current_skills_set, f):
    # if the temp skill set has everything no need to go further
    if len(current_skills_set) == number_of_distinct_skills:
        return False

    temp_skill_set = set(current_skills_set)

    for s in range(f, len(lst)):
        #debg
        if f >= 8:
            debug = 1
        for i in range(0, len(lst[s])):
            if lst[s][i] in _required_skills_set:
                temp_skill_set.add(lst[s][i])

    if len(temp_skill_set) == number_of_distinct_skills:
        return True
    else:
        return False





# 238/ 400
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

        # Optimization 1 - stop if the number of people is greater than the smallest number discovered so far
        if person_num >= minimum_people:
            lst[f], lst[s] = lst[s], lst[f]
        else:
            current_skills_set2 = set(current_skills_set)

            addition_num = 0
            for j in range(0, len(lst[f])):
                if lst[f][j] in _required_skills_set and lst[f][j] not in current_skills_set2:
                    current_skills_set2.add(lst[f][j])
                    addition_num = addition_num + 1

            # optimization - if a person didnt add anything thenthe additional permutations will not be optimal
            if addition_num != 0:
                if len(current_skills_set2) == _number_of_distinct_skills:
                    minimum_people = person_num

                permute6(lst, _required_skills_set, _number_of_distinct_skills, current_skills_set2, person_num+1, f + 1)
            lst[f], lst[s] = lst[s], lst[f]


def permute7(lst, _required_skills_set, _number_of_distinct_skills, current_skills_set, person_num, f=0):
    # put required skills into set, recurse through and check if it adds up to number of distinct_skills

    global minimum_people

    # base case - no more swaps we can make
    if f >= len(lst):
        return

# from 0 to length of the list
    for s in range(f, len(lst)):
        # mix of list
        lst[f], lst[s] = lst[s], lst[f]

        # Optimization 1 - stop if the number of people is greater than the smallest number discovered so far
        if person_num >= minimum_people:
            lst[f], lst[s] = lst[s], lst[f]
        else:
            current_skills_set2 = set(current_skills_set)

            addition_num = 0
            for j in range(0, len(lst[f])):
                if lst[f][j] in _required_skills_set and lst[f][j] not in current_skills_set2:
                    current_skills_set2.add(lst[f][j])
                    addition_num = addition_num + 1

            backtracking_result = backtracking(lst, _required_skills_set, _number_of_distinct_skills,
                                               current_skills_set2, f + 1)

            # optimization - if a person didnt add anything thenthe additional permutations will not be optimal
            if addition_num != 0:
                if len(current_skills_set2) == _number_of_distinct_skills:
                    minimum_people = person_num

                if backtracking_result:
                    permute7(lst, _required_skills_set, _number_of_distinct_skills, current_skills_set2, person_num + 1,
                             f + 1)
            lst[f], lst[s] = lst[s], lst[f]



def backtracking2(lst, _required_skills_set, number_of_distinct_skills, current_skills_set):
    # if the temp skill set has everything no need to go further
    #if len(current_skills_set) == number_of_distinct_skills:
     #   return False

    temp_skill_set = set(current_skills_set)

    for s in range(0, len(lst)):
        for i in range(0, len(lst[s])):
            if lst[s][i] in _required_skills_set:
                temp_skill_set.add(lst[s][i])

    if len(temp_skill_set) == number_of_distinct_skills:
        return True
    else:
        return False


# 344/400
def permute8(lst, _required_skills_set, _number_of_distinct_skills, current_skills_set, _person_num):

    global minimum_people
    global number_of_agents

    # bounding
    if _person_num >= minimum_people:
        return number_of_agents

    if len(lst) == 0:
        if len(current_skills_set) == _number_of_distinct_skills:
            if _person_num < minimum_people:
                minimum_people = _person_num
            return _person_num
        else:
            return number_of_agents

    curr_item = lst.pop()

    backtracing_result_ex = backtracking2(lst[:], _required_skills_set, _number_of_distinct_skills, current_skills_set)

    excluded = False

    if backtracing_result_ex:
        excluded = permute8(lst[:], _required_skills_set, _number_of_distinct_skills, current_skills_set, _person_num)


    current_skills_set2 = set(current_skills_set)
    _person_num = _person_num + 1
    addition_num = 0

    for i in range(0, len(curr_item)):
        if curr_item[i] in _required_skills_set and curr_item[i] not in current_skills_set2:
            current_skills_set2.add(curr_item[i])
            addition_num = addition_num + 1

    backtracing_result_inc = backtracking2(lst[:], _required_skills_set, _number_of_distinct_skills, current_skills_set2)

    included = False

    if backtracing_result_inc:
        included = permute8(lst[:], _required_skills_set, _number_of_distinct_skills, current_skills_set2, _person_num)

    if backtracing_result_ex and backtracing_result_inc:
        return min(included, excluded)
    elif backtracing_result_ex:
        return included
    elif backtracing_result_inc:
        return excluded
    else:
        number_of_agents





# Similarly, at every level in the recursion, check for people who are now subsets of others with regard to the remaining skills
# optimization 2 - remove subsets
agents2 = agents[:]
for m in agents:
    for n in agents:
        if set(m).issubset(set(n)) and m != n:
            agents2.remove(m)
            break


#optimization 3 - sort list so the agents that have the most skills are put in first
#agents2.sort(key=len, reverse=True)
agents2.sort(key=len, reverse=True) #bad you pop from the back

#permute(agents2, required_skills_set, number_of_distinct_skills)
#permute3(agents2, required_skills_set, number_of_distinct_skills)

current_skills_set = set()
# person_num = 1
#permute4(agents2, required_skills_set, number_of_distinct_skills, current_skills_set, person_num)
#permute7(agents2, required_skills_set, number_of_distinct_skills, current_skills_set, person_num)

person_num = 0
permute8(agents2, required_skills_set, number_of_distinct_skills, current_skills_set, person_num)

print(minimum_people)

# need to implement backtracing - wull I even get a solution
# Need a function that will check if the remainig answers will give you a solution for the funciton





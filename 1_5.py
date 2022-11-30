#406/400

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

    backtracing_result = backtracking2(lst, _required_skills_set, _number_of_distinct_skills, current_skills_set)

    if backtracing_result:
        excluded = permute8(lst[:], _required_skills_set, _number_of_distinct_skills, current_skills_set, _person_num)


    current_skills_set2 = set(current_skills_set)
    _person_num = _person_num + 1
    addition_num = 0

    for i in range(0, len(curr_item)):
        if curr_item[i] in _required_skills_set and curr_item[i] not in current_skills_set2:
            current_skills_set2.add(curr_item[i])
            addition_num = addition_num + 1

    included = permute8(lst[:], _required_skills_set, _number_of_distinct_skills, current_skills_set2, _person_num)

    if backtracing_result:
        return min(included, excluded)
    else:
        return included




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
agents2.sort(key=len)

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
import multiprocessing
import time

number_of_agents, number_of_distinct_skills = input().split()
number_of_agents = int(number_of_agents)
number_of_distinct_skills = int(number_of_distinct_skills)

minimum_people = number_of_agents

# current error, have the input code for question 2 in not 1
agents = []

for i in range(0, number_of_agents):
    skills_num = input()
    skills_num = int(skills_num)
    distinct_skills = input()
    # print(distinct_skills)
    skills = [int(c) for c in distinct_skills.split(' ')]
    # print(skills)
    # skills = distinct_skills

    agents.append([skills_num, skills, i])

# Get rid of subsets
agents2 = agents[:]
# Took too long
'''for m in agents:
    for n in agents:
        if set(m[1]).issubset(set(n[1])) and m != n:
            agents2.remove(m)
            break'''


rarity_dict = {}
# sort by how rare
for i in range(0, number_of_agents):
    for j in range(0, len(agents2[i][1])):
        if agents2[i][1][j] in rarity_dict:
            rarity_dict[agents2[i][1][j]] = rarity_dict[agents2[i][1][j]]+1
        else:
            rarity_dict[agents2[i][1][j]] = 1

for i in range(0, number_of_agents):
    rarity_score = 0
    for j in range(0, len(agents2[i][1])):
        rarity_score = rarity_score + rarity_dict[agents2[i][1][j]]
    adjusted_rarity = (rarity_score/len(agents2[i][1]))
    agents2[i].append(adjusted_rarity)

# sort by how rare the skill is
agents2.sort(key=lambda x: int(x[3]))  # sorted in reverse order


def backtracking2(lst, number_of_distinct_skills, current_skills_set):

    temp_skill_set = set(current_skills_set)

    for s in range(0, len(lst)):
        for i in range(0, len(lst[s][1])):
                temp_skill_set.add(lst[s][1][i])

    if len(temp_skill_set) == number_of_distinct_skills:
        return True
    else:
        return False


def permute8(lst, _number_of_distinct_skills, current_skills_set, _person_num):

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

    backtracing_result_ex = backtracking2(lst, _number_of_distinct_skills, current_skills_set)

    excluded = False

    if backtracing_result_ex:
        excluded = permute8(lst[:], _number_of_distinct_skills, current_skills_set, _person_num)


    current_skills_set2 = set(current_skills_set)
    _person_num = _person_num + 1
    addition_num = 0

    for i in range(0, len(curr_item[1])):
        if curr_item[1][i] not in current_skills_set2:
            current_skills_set2.add(curr_item[1][i])
            addition_num = addition_num + 1

    backtracing_result_inc = backtracking2(lst, number_of_distinct_skills, current_skills_set2)

    included = False

    if backtracing_result_inc:
        included = permute8(lst[:], _number_of_distinct_skills, current_skills_set2, _person_num)

    if backtracing_result_ex and backtracing_result_inc:
        return min(included, excluded)
    elif backtracing_result_ex:
        return included
    elif backtracing_result_inc:
        return excluded
    else:
        number_of_agents


current_skills_set = set()
person_num = 0


p = multiprocessing.Process(target=permute8(agents2, number_of_distinct_skills, current_skills_set, person_num), name="Foo", args=(9,))
p.start()

time.sleep(9)

# Terminate foo
p.terminate()

# Cleanup
p.join()

print(minimum_people)
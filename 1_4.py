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


permute(agents, required_skills_set, number_of_distinct_skills)

print(minimum_people)




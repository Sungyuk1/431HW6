import random

number_of_agents, number_of_distinct_skills = input().split()
number_of_agents = int(number_of_agents)
number_of_distinct_skills = int(number_of_distinct_skills)

agents = []

for i in range(0, number_of_agents):
    skills_num = input()
    skills_num = int(skills_num)
    distinct_skills = input()
    #print(distinct_skills)
    skills = [int(c) for c in distinct_skills.split(' ')]
    #print(skills)
    #skills = distinct_skills

    agents.append([skills_num,skills, i])

best = number_of_agents

def bruteForce(agents, num_agents, current_solution):
    global best

    if num_agents >= best:
        return current_solution

    # base case only 1 agents
    if len(agents) == 0:
        return {}

    curr_item = agents.pop()

    #create a new set which has the new agent included
    included_set = set()
    included_set.update(curr_item)
    included_set.update(current_solution)

    included = bruteForce(agents[:], num_agents + 1, included_set)
    excluded = bruteForce(agents[:], num_agents, current_solution)

    if (len(included) < len(excluded)):
        return included
    else:
        return excluded


print(bruteForce(agents, 0, set()))
number_of_agents, number_of_distinct_skills = input().split()
number_of_agents = int(number_of_agents)
number_of_distinct_skills = int(number_of_distinct_skills)

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


#this is causing the error
agents2.sort(key=lambda x: int(x[0]), reverse=True) # sorted in reverse order

skills_set = set()
agents_chosen = []
for i in range(0, len(agents2)):
    num_added = 0
    for j in range(0, len(agents2[i][1])):
        if agents2[i][1][j] not in skills_set:
            skills_set.add(agents2[i][1][j])
            num_added = num_added + 1
    if num_added != 0:
        agents_chosen.append(agents2[i][2])
        i = i + 1

print(len(agents_chosen))
print(agents_chosen)
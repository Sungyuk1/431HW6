number_of_agents, number_of_distinct_skills = input().split()
number_of_agents = int(number_of_agents)
number_of_distinct_skills = int(number_of_distinct_skills)

agents = []

for i in range(0,number_of_agents):
    skills_num = input()
    skills_num = int(skills_num)
    distinct_skills = input()
    #print(distinct_skills)
    skills = [int(c) for c in distinct_skills.split(' ')]
    #print(skills)
    #skills = distinct_skills

    agents.append([skills_num,skills, i])

#this is causing the error
agents.sort(key=lambda x: int(x[0])) #sorted in reverse order

skills_set = set()
i =len(agents) -1
agents_chosen = []
while len(skills_set) < number_of_distinct_skills:
    for j in range(0, len(agents[i][1])):
        debug = agents[i][1][j]
        skills_set.add(agents[i][1][j])
    agents_chosen.append(agents[i][2])
    i = i-1

print(len(agents_chosen))
print(agents_chosen)









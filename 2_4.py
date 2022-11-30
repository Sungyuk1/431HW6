number_of_agents, number_of_distinct_skills = input().split()
#print(number_of_agents)
#print("Before Conversion : " + number_of_distinct_skills)
number_of_agents = int(number_of_agents)
# print("After Conversion" + str(number_of_agents))
number_of_distinct_skills = int(number_of_distinct_skills)

# current error, have the input code for question 2 in not 1
agents = []

for i in range(0, number_of_agents):
    skills_num = input()
    #print("skills num : " + skills_num)
    #skills_num = int(skills_num)
    distinct_skills = list(map(int, input().split()))
    # print(distinct_skills)
    #skills = [c for c in distinct_skills.split(' ')]
    # print(skills)
    # skills = distinct_skills

    agents.append([skills_num, distinct_skills, i])

agents2 = agents[:]

rarity_dict = {}
# sort by how rare
for i in range(0, number_of_agents):
    for j in range(0, len(agents2[i][1])):
        if agents2[i][1][j] in rarity_dict:
            rarity_dict[agents2[i][1][j]] = rarity_dict[agents2[i][1][j]]+1
        else:
            rarity_dict[agents2[i][1][j]] = 1

for i in range(0, number_of_agents):
    rarity_score = 1000000000000
    for j in range(0, len(agents2[i][1])):
        if rarity_dict[agents2[i][1][j]] < rarity_score:
            rarity_score = rarity_dict[agents2[i][1][j]]
    agents2[i].append(rarity_score)

#this is causing the error
#agents2.sort(key=lambda x: int(x[0])) # sorted in reverse order

#sort by how rare the skill is
agents2.sort(key=lambda x: x[3]) # sorted in reverse order

skills_set = set()
agents_chosen = []

for i in range(0, int(len(agents2)/2)):
    num_added = 0
    for j in range(0, len(agents2[i][1])):
        if agents2[i][1][j] not in skills_set:
            skills_set.add(agents2[i][1][j])
            num_added = num_added + 1
    if num_added != 0:
        agents_chosen.append(agents2[i][2])

    if len(skills_set) >= number_of_distinct_skills/(1.5):
        break





print(len(agents_chosen))
print(agents_chosen)
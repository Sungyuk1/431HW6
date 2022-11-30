number_of_agents, number_of_distinct_skills = input().split()
number_of_agents = int(number_of_agents)
number_of_distinct_skills = int(number_of_distinct_skills)

list_of_agents = []

for i in range(0, number_of_agents):
    number_of_skills = int(input())
    skills = set([int(x) for x in input().split()])
    list_of_agents.append([skills, i])

# remove subsets
agents2 = list_of_agents[:]
for m in list_of_agents:
    for n in list_of_agents:
        if m[0].issubset(n[0]) and m != n:
            agents2.remove(m)
            break

skills = set()
#agents2.sort(key=lambda x: len(x[0]), reverse=True) doesnt help cause most have the same number

rarity_dict = {}
# sort by how rare
for i in range(0, number_of_agents):
    for j in agents2[i][0]:
        if j in rarity_dict.keys():
            rarity_dict[j] = rarity_dict[j]+1
        else:
            rarity_dict[j] = 1

for i in range(0, number_of_agents):
    rarity_score = 1000000000000
    for j in agents2[i][0]:
        if rarity_dict[j] < rarity_score:
            rarity_score = rarity_dict[j]
    agents2[i].append(rarity_score)

# sort by how rare the skill is
agents2.sort(key=lambda x: int(x[2]))  # sorted in reverse order


agent_num = 0
agents_chosen = []
answer = 0

skill_use_dict = {}

for i in range(0, int(len(agents2))):
    number_added = 0
    for x in agents2[i][0]:
        if x not in skills:
            skills.add(x)
            number_added = number_added + 1

    if number_added > 0:
        agents_chosen.append(agents2[i])

        for x in agents2[i][0]:
            if x not in skill_use_dict.keys():
                skill_use_dict[x] = 1
            else:
                skill_use_dict[x] = skill_use_dict[x] + 1


    if len(skills) >= number_of_distinct_skills:
        break


to_remove = []

for i in agents_chosen:
    not_1 = 0
    for x in i[0]:
        if skill_use_dict[x] == 1:
            not_1 = not_1 + 1

    if not_1 == 0:
        for x in i[0]:
            if skill_use_dict[x] <=0:
                debug = 0
            skill_use_dict[x] = skill_use_dict[x] - 1
        to_remove.append(i)



output = [x for x in agents_chosen if x not in to_remove]

to_remove2 = []

for i in output:
    not_1 = 0
    for x in i[0]:
        if skill_use_dict[x] == 1:
            not_1 = not_1 + 1

    if not_1 == 0:
        for x in i[0]:
            if skill_use_dict[x] <=0:
                debug = 0
            skill_use_dict[x] = skill_use_dict[x] - 1
        to_remove2.append(i)



output2 = [x for x in output if x not in to_remove2]

to_remove3 = []

for i in output2:
    not_1 = 0
    for x in i[0]:
        if skill_use_dict[x] == 1:
            not_1 = not_1 + 1

    if not_1 == 0:
        for x in i[0]:
            if skill_use_dict[x] <=0:
                debug = 0
            skill_use_dict[x] = skill_use_dict[x] - 1
        to_remove3.append(i)



output3 = [x for x in output2 if x not in to_remove3]


#print(len(agents_chosen))
#print("skills : " + str(len(skills)))
#for i in range(0, len(agents_chosen)):
#    print(agents_chosen[i][1], end=" ")

'''skill_set2 = set()
for i in range(0, len(agents_chosen)):
    for x in agents_chosen[i][0]:
        skill_set2.add(x)'''

print(len(output3))
#print("skills : " + str(len(skills)))
for i in range(0, len(output3)):
    print(output3[i][1], end=" ")

#skill_set2 = set()
# for i in range(0, len(output2)):
#     for x in output2[i][0]:
#         skill_set2.add(x)
#
# print("number of skills : " + str(len(skill_set2)))





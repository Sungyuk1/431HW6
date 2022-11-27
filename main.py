# importing copy module
import copy

number_of_agents, number_of_distinct_skills = input().split()
number_of_agents = int(number_of_agents)
number_of_distinct_skills = int(number_of_distinct_skills)

required_skills = input()
required_skills_list = [str(i) for i in required_skills.split(' ')]

#trying a list
agents = []

for i in range(0, number_of_agents):
    skills_num = values = input()
    skills = input()
    skills_list = [i for i in skills.split(' ')]
    agents.append(skills_list)

#now doing brute force
minimum_people = number_of_agents   #watch out this could cause errors

for i in range(0, len(agents)):

    #new agent number tracker and list
    current_agent_number = 1
    required_skills_list2 = copy.deepcopy(required_skills_list)

    #check for current agent
    for x in range(0, len(agents[i])):
        if agents[i][x] in required_skills_list2:
            required_skills_list2.remove(agents[i][x])

    if len(required_skills_list2) == 0:
        minimum_people = 1
        break

    for j in range(0, len(agents)):
        current_agent_number = current_agent_number+1
        if(current_agent_number >= minimum_people):
            break
        elif i != j:
            for x in range(0, len(agents[j])):
                if agents[j][x] in required_skills_list2:
                    required_skills_list2.remove(agents[j][x])

            if len(required_skills_list2) == 0:
                minimum_people = current_agent_number
                break

print(minimum_people)




"""
while(len(required_skills_list2) > 0):
    current_agent_number = 0;
    for i in range(0, len(agents)):
        current_agent_number = current_agent_number + 1
        for x in range(0, len(agents[i])):
            if agents[x] in required_skills_list2:
                required_skills_list2.remove(agents[x])

        if len(required_skills_list2) == 0:


        for j in range(0, len(agents)):
            if(i != j):
            """





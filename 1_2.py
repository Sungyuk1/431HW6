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

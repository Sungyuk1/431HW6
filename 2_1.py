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

#this is causing the error
agents.sort(key=lambda x: int(x[0]), reverse=True) # sorted in reverse order

skills_set = set()
i = 0
agents_chosen = []
while len(skills_set) < number_of_distinct_skills:
    num_added = 0
    for j in range(0, len(agents[i][1])):
        debug = agents[i][1][j]
        skills_set.add(agents[i][1][j])
        num_added = num_added + 1
    if num_added != 0:
        agents_chosen.append(agents[i][2])
        i = i + 1

print(len(agents_chosen))
print(agents_chosen)




#approx is used here was get all the inputs, sort by who has the most distinct skills, and then go
#trhough from the ones wiht the most till you have the number of distinct skills


'''
advice from professor : 
- Similarly, at every level in the recursion, check for people who are now subsets of others with regard to the remaining skills
- Before your recursion, run a greedy algorithm to give you a decent answer that you can use for bounding
- Check whether there is any single person in the remaining pool that would give you a solution (note that if you do this you can also push your bounding farther)

'''

# no graph
# right path -
# mabe q 1 answer with timer. - only for 5 seconds or whatever.

#use sets not list for aprox


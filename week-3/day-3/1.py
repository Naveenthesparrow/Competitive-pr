Question Name:  sum_of_chemistry


from collections import Counter

def sum_of_chemistry(n, skills):
    total_sum = sum(skills)
    if total_sum % (n // 2) != 0:
        return -1
    
    target = total_sum // (n // 2)
    skill_counter = Counter(skills)
    chemistry_sum = 0
    
    for skill in sorted(skill_counter):
        if skill_counter[skill] == 0:
            continue
        
        pair_skill = target - skill
        if pair_skill < skill:
            continue
        
        if skill_counter[skill] > 0 and skill_counter[pair_skill] > 0:
            if skill == pair_skill:
                pairs = skill_counter[skill] // 2
                chemistry_sum += pairs * (skill * skill)
                skill_counter[skill] = 0
            else:
                pairs = min(skill_counter[skill], skill_counter[pair_skill])
                chemistry_sum += pairs * (skill * pair_skill)
                skill_counter[skill] -= pairs
                skill_counter[pair_skill] -= pairs
    
    if any(skill_counter.values()):
        return -1
    
    return chemistry_sum

# Input from the user
n = int(input("Enter the number of players (even length): "))
skills = list(map(int, input("Enter the skill levels separated by spaces: ").split()))

result = sum_of_chemistry(n, skills)
print(result)

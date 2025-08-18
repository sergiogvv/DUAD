def upper_lower(string):
    upper=0
    lower=0
    for char in string:
        if char.isupper():
            upper += 1
        if char.islower():
            lower+= 1
    print(f'There’s {upper} upper cases and {lower} lower cases')
    return upper, lower


upper_lower('I love Nación Sushi')

upper_lower('Rugen runs away. Inigo chases him throughout the castle until Rugen suddenly throws a knife at him and seriously wounds him, mocking his quest as he prepares to deliver the fatal blow. At the last second, Inigo recovers his strength and duels his father''s murderer, repeating his fateful words as he corners Rugen, inflicting on him the same dueling scars. Rugen begs for his life and offers to give Inigo anything he wants before trying to attack him again; Inigo catches Rugen''s sword arm and replies, "I want my father back, you son of a bitch," as he kills him.')

# It's recommended to always start/end a tuple with parentheses, even though they're
# optional. Explicit is better than implicit.

zoo = ('python', 'elephant', 'tigers')
print('Number of animals in the zoo is', len(zoo))
new_zoo = 'kangaroo', 'camel', zoo
print('Number of cages in the new zoo is', len(zoo))
print('All animals in the new zoo are', new_zoo)
print('Animals bought from old zoo are', new_zoo[2])
print('Last animal bought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
       len(new_zoo)-1+len(new_zoo[2]))

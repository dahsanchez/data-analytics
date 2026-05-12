movies = ['The Sandlot',
          'The Nightmare Before Christmas', 
          'Twilight Saga']

print(f'The list movies includes my top {len(movies)} favorite movies')

print(sorted(movies))
print(movies)

movies.sort()
print(movies)

movies.append('Coraline')
print(f'The list movies includes my top {len(movies)} favorite movies')
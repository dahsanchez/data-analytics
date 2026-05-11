fave_things = ['Oliver',
               'Pizza',
               'Anime',
               'Japan',
               'Hungarian']
for things, fave_things in enumerate(fave_things,start=1) :
    if things == 1:
        print(f'{things}.{fave_things} <--- Top pick')
    else:
        print(f'{things}.{fave_things}')
f = open('about_me.txt', 'r')
print(f.read())
f.close()

f = open('about_me.txt', 'r')
print(f.read(50))
print(f.read(50))
f.close()

f = open('about_me.txt', 'r')
print(f.readlines(10))
print(f.readlines())

for i in range(1, 5):
    print(f.readlines)
f.close()

f = open('about_me.txt', 'r')
# print(f.readlines(1))
# print(f.readlines(1))
print(f.readlines(10))
print(f.readlines(10))
print(f.readlines(100))
print(f.readlines(-1))
f.close()

f = open('about_me.txt', 'r')
first_50 = f.read(50)
nxt_4_lines = []
for i  in range(4):
    nxt_4_lines.append(f.readline())

next_100 = f.readlines(100)
f.close()

print(f'First 50 charactors: {first_50}')
print(f'Next four lines: {nxt_4_lines}')
print(f'Next 100 charactors: {next_100}')

number_of_students = int(input("How many boys and girls : "))
boy_heights = sorted(map(int, input("Enter the heights of boys: ").split()))
girl_heights = sorted(map(int, input("Enter the heights of girls: ").split()))
is_boy_girl_pattern_valid = True
is_girl_boy_pattern_valid = True
for i in range(number_of_students - 1):
    if boy_heights[i] > boy_heights[i + 1] or girl_heights[i] > girl_heights[i + 1] or boy_heights[i] > girl_heights[i]:
        is_boy_girl_pattern_valid = False
        break
for i in range(number_of_students - 1):
    if girl_heights[i] > girl_heights[i + 1] or boy_heights[i] > boy_heights[i + 1] or girl_heights[i] > boy_heights[i]:
        is_girl_boy_pattern_valid = False
        break
if is_boy_girl_pattern_valid or is_girl_boy_pattern_valid:
    print("YES")
else:
    print("NO")
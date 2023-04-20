# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй

test_str = "Pythonist"
count = 0
for i in test_str: 
    if i == 'o': 
        count = count + 1
print ("Count of t in Pythonist is : " + str(count)) 
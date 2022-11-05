def Welcome():
    print('welcome')
    print('Choose a number depending on what you want to do with the dictionary.')
    print('')
    print('1. Search for a specific word.')
    print('2. Update the dictionary')
    print('3. Display the entire dictionary')
    print('4. Exit')

students = {
'CPU':'Central processing unit',
'WHO': 'World Health Organization',
'Python': 'Programming language',
'Anisa': 'A somali, tall, arrogant and smart gal',
'Moureen': 'Fat and Anisas best friend',
'Jodick': 'Short Burundian, rude and lazy badman'}
while True:

    a = input('Hello, wanna interact with the dictionary or press q to quit?: ').lower()
    if a == 'q':
        break
    elif a != 'yes':
        print('You would have said yes if you wanted to')
        continue
    else:
        print(Welcome())

        print('')

    while True:
        number = int(input('Choose a number corresponding to what you want to do: '))
        if number == 1:
            word = input('Which word do you want to search for?: ')

            if word in students:
                    print(students[word])
            else:
                print('the word not found.')

        elif number == 2:
            upd = input('What is the word do you want to update?: ')
            mng = input('what is the meaning of that world')

            students[upd] = mng

            print(students)
        elif number == 3:
            print('The entrire dictionary as you requested is down below.')
            print('')
            print(students)
        elif number == 4:
            quit()
        else:
            continue
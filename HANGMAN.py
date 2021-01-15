q=["I’m tall when I’m young, and I’m short when I’m old. What am I?","What goes up but never comes down?","I shave every day, but my beard stays the same. What am I?","I have branches, but no fruit, trunk or leaves. What am I?","The more of this there is, the less you see. What is it?","What has many keys but can’t open a single lock?","What invention lets you look right through a wall?","It belongs to you, but other people use it more than you do. What is it?","I am an odd number. Take away a letter and I become even. What number am I?","What five-letter word becomes shorter when you add two letters to it?"]
a=['candle','age','barber','bank','darkness','piano','window','name','seven','short']
print(f'HANGMAN\nRules:\nThere are {len(q)} questions.\nYou will be given 3 chances to answer a question.\nSuccessfully answering a question will award you 1 point.\nEnjoy!')
chance=1
score=0
for i in range (len(q)):
    print('>',q[i])
    while chance<=3:
        guess=(input('Guess: '))
        chance+=1
        if guess==a[i]:
            print('That is correct. Proceeding to next question...')
            score+=1
            chance=1
            break
        else:
            print('Wrong. Try Again!')           
    else:
        print('Correct Answer:',a[i])
        print('Proceeding to next question...')
        chance=1
print(f'Final score is {score}/{len(q)}\nThank you!')
input('Press enter to exit')

def order_highscores(highscores):
    for i in range(4):
        for j in range(i + 1, 5):
            if highscores[1][j] > highscores[1][i]:

                #swap highscores if it is higher
                temp = highscores[1][i] 
                highscores[1][i] = highscores[1][j]
                highscores[1][j] = temp

                #swap relavent users
                temp = highscores[0][i] 
                highscores[0][i] =  highscores[0][j]
                highscores[0][j] = temp

def check_new_highscore(highscores, user, score):

    if score > highscores[1][4]:
        highscores[1][4] = score
        highscores[0][4] = user
        order_highscores(highscores)



def get_highscores():
    #read highscores from text file
    highscore_file = open("highscores.txt")
    # store all the lines in the file as a list
    scores = highscore_file.readlines()
    highscore_file.close()

    highscores = [[0] * 5,[0] * 5]
    for i in range(5):
        user = scores[i].split("~")
        highscores[0][i] = user[0]
        highscores[1][i] = int(user[1][:-1])


    return highscores

def save_highscores(highscores):
    #write highscore into textfile

    order_highscores(highscores)

    score_list = []
    for i in range(5):
        score_list.append(highscores[0][i] + ' ~ ' + str(highscores[1][i]) + '\n')
    
    highscore_file = open("highscores.txt", "w")
    highscore_file.writelines(score_list)
    highscore_file.close()
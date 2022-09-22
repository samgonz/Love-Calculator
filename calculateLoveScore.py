def calculateLoveScore(userName, loverName):
    userScoreT = userName.count('T')
    userScoreR = userName.count('R')
    userScoreU = userName.count('U')
    userScoreE = userName.count('E')

    userScoreL = userName.count('T')
    userScoreO = userName.count('R')
    userScoreV = userName.count('U')
    userScoreE2 = userName.count('E')

    loverScoreT = loverName.count('T')
    loverScoreR = loverName.count('R')
    loverScoreU = loverName.count('U')
    loverScoreE = loverName.count('E')

    loverScoreL = loverName.count('T')
    loverScoreO = loverName.count('R')
    loverScoreV = loverName.count('U')
    loverScoreE2 = loverName.count('E')

    scoreTrue = str(userScoreT + userScoreR + userScoreU + userScoreE + loverScoreT + loverScoreR + loverScoreU + loverScoreE )
    scoreLove = str(userScoreL + userScoreO + userScoreV + userScoreE2 + loverScoreL + loverScoreO + loverScoreV + loverScoreE2)
    totalScore = int(scoreTrue + scoreLove)
    return totalScore
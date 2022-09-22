import calculateLoveScore
import splashScreens
import getNames

splashScreens.welcomeSplash()
loverScore = calculateLoveScore.calculateLoveScore(getNames.getLoverUser(), getNames.getLoverOther())

print(f'Your total love score is {loverScore}%')

import pyautogui
# pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

totalRaidCount = 0
successfulRaids = 0
failedRaids = 0

started = 0
diffSelected = 0
teamSelected = 0

def start_raid():
    # find the summon button and click it
    global started
    if pyautogui.locateOnScreen('summon.png'):
        summonBtn = pyautogui.locateOnScreen('summon.png')
        summonBtnCtr = pyautogui.center(summonBtn)
        pyautogui.click(summonBtnCtr)
        print('Starting a new raid...')
        started = 1

def select_difficulty():
    global diffSelected
    if pyautogui.locateOnScreen('heroic.png'):
        heroicBtn = pyautogui.locateOnScreen('heroic.png')
        heroicBtnCtr = pyautogui.center(heroicBtn)
        pyautogui.click(heroicBtnCtr)
        print('Selecting Heroic difficulty...')
        diffSelected = 1

def accept_team():
    global teamSelected
    global totalRaidCount
    if pyautogui.locateOnScreen('accept.png'):
        totalRaidCount += 1
        acceptBtn = pyautogui.locateOnScreen('accept.png')
        acceptBtnCtr = pyautogui.center(acceptBtn)
        pyautogui.click(acceptBtnCtr)
        print('Accepting team...')
        teamSelected = 1
        print('Raid started!')

def failed_raid():
    global started
    global diffSelected
    global teamSelected
    global failedRaids
    if pyautogui.locateOnScreen('close.png'):
        print('Raid completed...')
        failedRaids += 1
        closeBtn = pyautogui.locateOnScreen('close.png')
        closeBtnCtr = pyautogui.center(closeBtn)
        pyautogui.click(closeBtnCtr)
        started = 0
        diffSelected = 0
        teamSelected = 0
        print('Failed =( ...')
        print(str(failedRaids) + ' failed raids out of ' + str(totalRaidCount) + ' total raids so far.')
        print('##########----------##########')

def success_raid():
    global started
    global diffSelected
    global teamSelected
    global successfulRaids
    if pyautogui.locateOnScreen('cleared.png'):
        print('Raid completed...')
        successfulRaids += 1
        yesBtn = pyautogui.locateOnScreen('yes.png')
        yesBtnCtr = pyautogui.center(yesBtn)
        pyautogui.click(yesBtnCtr)
        started = 0
        diffSelected = 0
        teamSelected = 0
        print('Success! ...')
        print(str(successfulRaids) + ' successful raids out of ' + str(totalRaidCount) + ' total raids so far.')
        print('##########----------##########')

def out_of_resources():
    global started
    global diffSelected
    global teamSelected
    global totalRaidCount
    if pyautogui.locateOnScreen('outOfShards.png'):
        totalRaidCount -= 1
        started = 0
        diffSelected = 0
        teamSelected = 0
        print('Out of shards! ...')
        print(str(totalRaidCount) + ' total raids')
        print(str(successfulRaids) + ' successful raids')
        print(str(failedRaids) + ' failed raids')


def run_raids():
    while True:

        start_raid()

        if started:
            select_difficulty()

            if diffSelected:
                accept_team()

                if teamSelected:

                    failed_raid()
                    success_raid()
                    out_of_resources()

run_raids()

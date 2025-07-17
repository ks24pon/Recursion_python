def howLongToReachFundGoal(capitalMoney,goalMoney,interest):
    # helper関数に移ります
    return howLongToReachFundGoalHelper(capitalMoney,goalMoney,interest,0)

# 引数にyearを追加し、経過年を追跡できるようにします
def howLongToReachFundGoalHelper(capitalMoney,goalMoney,interest,year):
    # capitalMoneyがgoalMoney以上になったら経過年を返します
    if capitalMoney >= goalMoney:
      return year
    # 80年以上経過した場合は80を返します
    if year >= 80:
      return 80

    # 経過年yearが偶数の時はgoalMoneyを2%、奇数の時は3%増加させます
    if year % 2 == 0:
       goalMoney *= 1.02
    else:
       goalMoney *= 1.03

    # capitalMoneyに年利を加えます
    capitalMoney *= (1+interest/100)

    # yearに1加えて再帰を行います
    return howLongToReachFundGoalHelper(capitalMoney, goalMoney, interest, year+1)
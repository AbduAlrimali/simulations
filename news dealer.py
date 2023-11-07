#عبدالرحمن محمد محمود احمد الرمالي
#Student ID: 22011460

#global lists
data = []

#global variables
daily_production = int(input("enter daily production rate: "))
n= int(input("enter days to run: "))
buying_rate = float(input("enter buying rate per NP: "))
selling_rate = float(input("enter selling rate per NP: "))
scrap_price = float(input("enter scrap price: "))
lost_profit_rate = selling_rate - buying_rate
NT = 0
demand = 0
revenue_from_sales_v = 0
cost_of_NPs_v = 0
lost_profit_v = 0
scrap_revenue_v = 0
dailty_profit_v = 0
total_profit = 0

#global functions
def newsTypeGen(RN):
    if (RN <= 35 and RN >=1) and RN % 1 == 0:
        return "good"
    elif (RN <= 80 and RN >=36) and RN % 1 == 0:
        return "fair"
    elif (RN <= 100 and RN >=81) and RN % 1 == 0:
        return "poor"
    else:
        newsTypeGen(input())
        
def demandGen(RN):
    if NT == "good":
        if (RN <= 3 and RN >=1) and RN % 1 == 0:
            return 40
        elif (RN <= 8 and RN >=4) and RN % 1 == 0:
            return 50
        elif (RN <= 23 and RN >=9) and RN % 1 == 0:
            return 60
        elif (RN <= 43 and RN >=24) and RN % 1 == 0:
            return 70
        elif (RN <= 78 and RN >=44) and RN % 1 == 0:
            return 80
        elif (RN <= 93 and RN >=79) and RN % 1 == 0:
            return 90
        elif (RN <= 100 and RN >=94) and RN % 1 == 0:
            return 100
        else:
            demandGen(input())
    elif NT == "fair":
        if (RN <= 10 and RN >=1) and RN % 1 == 0:
            return 40
        elif (RN <= 28 and RN >=11) and RN % 1 == 0:
            return 50
        elif (RN <= 68 and RN >=29) and RN % 1 == 0:
            return 60
        elif (RN <= 88 and RN >=69) and RN % 1 == 0:
            return 70
        elif (RN <= 96 and RN >=89) and RN % 1 == 0:
            return 80
        elif (RN <= 100 and RN >=97) and RN % 1 == 0:
            return 90
        else:
            demandGen(input())
    else:
        if (RN <= 44 and RN >=1) and RN % 1 == 0:
            return 40
        elif (RN <= 66 and RN >=45) and RN % 1 == 0:
            return 50
        elif (RN <= 82 and RN >=67) and RN % 1 == 0:
            return 60
        elif (RN <= 94 and RN >=83) and RN % 1 == 0:
            return 70
        elif (RN <= 100 and RN >=95) and RN % 1 == 0:
            return 80
        else:
            demandGen(input())
def printData():
    print ("{:<8} {:<15} {:<15} {:<15} {:<10} {:<20} {:<15} {:<15} {:<15} {:<15}".format('Day','RN for NT','News Type','RN for Demand', 'Demand', 'Revenue from Sales', 'Cost of NPs', 'Lost Profit', 'Scrap Revenue', 'Dialy Profit'))
    for i in data:
        print ("{:<8} {:<15} {:<15} {:<15} {:<10} {:<20.1f} {:<15.1f} {:<15.1f} {:<15.1f} {:<15.1f}".format(i[0],i[1],i[2],i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
    print("total profit: {:.1f}".format(total_profit))
current = 0
while current < n:
    NT_RN = int(input("enter newspaper RN: "))
    DEMAND_RN = int(input("enter demand RN: "))
    NT = newsTypeGen(NT_RN)
    demand = demandGen(DEMAND_RN)
    revenue_from_sales_v = demand * selling_rate
    cost_of_NPs_v = buying_rate * daily_production
    if(demand <= daily_production):
        lost_profit_v = 0
    else:
        lost_profit_v = (demand - daily_production) * lost_profit_rate

    if(demand >= daily_production):
        scrap_revenue_v = 0
    else:
        scrap_revenue_v = (daily_production - demand) * scrap_price
    dailty_profit_v = revenue_from_sales_v - cost_of_NPs_v - lost_profit_v + scrap_revenue_v
    total_profit += dailty_profit_v

    current+=1
    data.append([current, NT_RN, NT, DEMAND_RN, demand, revenue_from_sales_v, cost_of_NPs_v, lost_profit_v, scrap_revenue_v, dailty_profit_v])

    printData()
    
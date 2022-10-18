import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
plt.style.use('seaborn-white')

def Month(Money_spent_towards_the_home_loan, total_money_available_for_investment):
    global what_month_is_it
    money_saved = total_available_money_per_month - Money_spent_towards_the_home_loan
    total_money_available_for_investment += money_saved
    what_month_is_it  += 1
    if  what_month_is_it ==13:
            what_month_is_it =1
            total_money_available_for_investment = one_year(total_money_available_for_investment)
    return total_money_available_for_investment


def one_year(total):
    global interest_rate, what_year_is_it
    what_year_is_it += 1
    return total * (1+(interest_rate/100))


def person(total_money_available_for_investment,downpayment, numberofyears, monthlypayment):
    global what_month_is_it, what_year_is_it
    savinghistory = []
    what_year_is_it = starting_year
    total_money_available_for_investment = total_money_available_for_investment - downpayment
    for i in range(numberofyears*12):
        total_money_available_for_investment = Month(monthlypayment, total_money_available_for_investment)
        savinghistory.append(total_money_available_for_investment)
    if numberofyears !=30:
        for i in range(360 - (numberofyears*12)):
            total_money_available_for_investment = Month(0, total_money_available_for_investment)    
            savinghistory.append(total_money_available_for_investment)
    People.append(savinghistory)
   

def draw():
    global People
    global interest_rate
    fig = plt.figure(figsize =(9, 4)) 
    colors = ['tab:purple', 'tab:cyan', 'tab:pink']
    colors= list(mcolors.TABLEAU_COLORS)
    for j, i in enumerate(People):
        plt.plot(i,  linestyle="solid", label="Person: {j}".format(j=j+1)) # color="green" color=colors[random.randint(0,len(colors)-1)]
        plt.text(len(i),i[-1],"The house + $%.2f"%i[-1], horizontalalignment='right', fontsize=12, color="brown")

    People = []
    #plt.plot(saving_history_30, color="red", linestyle="solid")
    plt.title('Savings over the 30 years period at interest rate =  {rate}%'.format(rate=interest_rate),fontsize=16, color="gold")
    plt.grid(color = 'tab:pink', linestyle = '--', linewidth = 0.5)
    plt.ylabel("Total Saving")
    plt.xlabel("Years")
    ticks =  ["'"+str(i) for i in range(starting_year-2000,what_year_is_it-2000)]
    plt.xticks(range(0,len(i),12) ,ticks , fontsize=8, color="green")
    plt.legend(edgecolor="red",facecolor="blue", loc="best")  # upper left
    plt.show()
    


starting_year = 2022
what_month_is_it = 1 # January
total_available_money_per_month = 2000
People = []


for i in range(0,11):
    interest_rate = i
    person(120000, 120000, 15, 2000)# # 120K DOWN FOR 15 YEARS 
    person(120000, 40000, 30, 1877)   # 40k down for 40 years 
    person(40000,  40000, 30, 1877)  
    #person(100000, 100000, 20, 1700)
    draw()


#def calculate_savings() ``:
#    global what_month_is_it, what_year_is_it, total_money_available_for_investment, saving_history_15, saving_history_30
#    total_money_available_for_investment, saving_history_15, what_year_is_it = 100000, [], starting_year
#    # person 1
#    downpayment = 100000
#    total_money_available_for_investment = total_money_available_for_investment - downpayment
#    
#    for i in range(180): # 180 month is 15 years
#        Month(2000)
#        saving_history_15.append(total_money_available_for_investment)
#    for i in range(180): 
#        Month(0)
#        saving_history_15.append(total_money_available_for_investment)
#    
#    total_money_available_for_investment, saving_history_30, what_year_is_it = 100000, [], starting_year
#    ## person 2
#    downpayment = 100000
#    total_money_available_for_investment =  total_money_available_for_investment - downpayment
#    
#    for i in range(360): # 360 month is 30 years
#        Month(1400)
#        saving_history_30.append(total_money_available_for_investment)



loanAmount = 400000 -40000
years = 30  * 12
interestRate = 4.75  / 100 / 12

mortgagePayment = loanAmount * (interestRate * (1 + interestRate)** years) / ((1 + interestRate) ** years - 1)
print("The monthly mortgage payment is\n (%.2f) " % mortgagePayment)

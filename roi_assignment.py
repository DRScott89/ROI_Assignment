class return_on_investment():

    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cashFlow = 0
        self.cashOnCash = 0
        self.investmentReturn = 0
        
        
    def totalIncome(self):
        rental_income = int(input(f'\nEnter to calculate income...\n\nRental: '))
        laundry_income = int(input(f'Laundry: '))
        storage_income = int(input(f'Storage: '))
        misc_income = int(input(f'Misc: '))
        
        self.income = rental_income + laundry_income + storage_income + misc_income
        print(f'\nTotal Income: ${self.income}')
        
        
    def totalExpenses(self):
        tax_expense = int(input(f'\nEnter to calculate expenses...\n\nTax: '))
        insurance_expense = int(input(f'Insurance: '))
        utilities_expense = int(input(f'Utilities: \n(Electric, Water, Sewer, Gas, etc.) '))
        hoa_expense = int(input(f'HOA: '))
        lawn_care_expense = int(input(f'Lawn Care: '))
        vacancy_expense = int(input(f'Vacancy: '))
        repairs_expense = int(input(f'Repairs: '))
        capEx_expense = int(input(f'Cap Ex: '))
        property_management_expense = int(input(f'Property Management: '))
        mortgage_expense = int(input(f'Mortgage: '))

        self.expenses = (tax_expense + insurance_expense + utilities_expense + hoa_expense
                        +lawn_care_expense + vacancy_expense + repairs_expense + capEx_expense + property_management_expense
                        +mortgage_expense)
        print (f'\nTotal Expenses: ${self.expenses}')

        
    def totalCashFlow(self):
        self.cashFlow = self.income - self.expenses 
        print(f'\nTotal Monthly Cash: ${self.cashFlow}')
    
    
    def totalCashOnCash(self):
        down_payment = int(input(f'\nEnter to calculate total investment...\n\nDown Payment: '))
        closing_costs = int(input(f'Closing Costs: '))
        repair_reno = int(input(f'Repair/Renovation: '))
        misc = int(input(f'Misc: '))
    
        self.cashOnCash = down_payment + closing_costs + repair_reno + misc
        print(f'\nTotal Investment: ${self.cashOnCash}')
    

        
    def returnOnInvestment(self):
        annualCash = self.cashFlow * 12
        returnOnInvestment = annualCash / self.cashOnCash * 100
        print(f'\n\nROI = {returnOnInvestment}%' )
        
rentalProperty = return_on_investment()   

def run():
    while True:
        rentalProperty.totalIncome()
        rentalProperty.totalExpenses()
        rentalProperty.totalCashFlow() 
        rentalProperty.totalCashOnCash()
        rentalProperty.returnOnInvestment()    
        break
run()
   




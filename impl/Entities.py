import textwrap

class Employee:
    def __init__(self,name,postition,description):
        self.name = name
        self.position = postition
        self.description = description


    def printAbout(self):
        print '[name]: ',self.name
        print '[position]: ',self.position
        print '[description]: ',self.description

#Klasa kompanija - u nasem slucaju to ce biti GreenPeace.inc
class Company:

    def __init__(self,about,history,campaigns,employees):
        self.about=about
        self.history=history
        self.campaigns = campaigns
        self.employees=employees

    #nigde je ne koristimo ali cisto primer "validacije" unosa
    def add_employees(self,emp):
        if isinstance(emp,Employee):
            self.employees.append(emp)
        else: raise Exception('Objekat mora biti instanca zaposlenog')

    #primer upotrebe textwrap-a, narocito koristan kod ispisa u fajl
    def printAboutCompany(self):
        print '[ABOUT]:',(textwrap.fill(self.about,width=150))
        print
        print '[HISTORY]: ',(textwrap.fill(self.history,width=150))


    def printCampaigns(self):
        print '---------[CAMPAIGNS]---------'
        i=1
        for key in self.campaigns.keys():
            print i,'.','[CAMPAIGN]: ',key
            print i,'.','[LINK TO CAMPAIGN]: ',self.campaigns[key]
            i=i+1


    def printEmployees(self):
        print "EMPLOYEES: --->"
        for employee in self.employees:
            Employee.printAbout(employee)

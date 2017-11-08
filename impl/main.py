from crawler import *
import webbrowser
#Moze se koristiti i specificni browser, mada je windows dovoljno pametan da sam locira path
#chrome_path = "C:/Program Files(x86)/Google/Chrome/Application/chrome.exe"

if  __name__ == '__main__':
    while(True):
        print "Welcome to Greenpeace"
        print "[1]Would you like to read something about us?"
        print "[2]Would you like to see our campaigns?"
        print "[3]Would you like to see list of our employees?"
        print "[4] Exit"


        #pravimo kompaniju i dodeljujemo joj crawl-ovane vrednosti
        company = Company(crawl_about(),crawl_history(),crawl_camapigns(),crawl_employees())

        #korisnik bira jednu od opcija
        x=int(input('>>>'))
        if(x==1):
            company.printAboutCompany()
            print "[1] Back"
            print "[2] Exit"
            p=int(input('>>>'))
            if(p==2):
                break
            elif(p==1):
                continue
            else:
                raise Exception('Pogresan unos, prekida se program.')
                #moze i samo primitivan print da se uradi
                break
        elif(x==2):
            company.printCampaigns()
            print "[1] Open Campaign"
            print "[2] Back"
            print "[3] Exit"
            p=(input('>>>'))
            if (p == 3):
                break
            elif (p == 2):
                continue
            elif (p == 1):
                name = raw_input()
                if name in company.campaigns.keys():
                    #otvara u novi tab ako je moguce
                    new = 2
                    webbrowser.open(company.campaigns[name],new=new)
                else: raise Exception('Uneta je nepostojeca kampanja')
                print 'You have been redirected to Home navigation '
                continue

            else:
                raise Exception('Pogresan unos, prekida se program.')
                # moze i samo primitivan print da se uradi
                break
        elif(x==3):
            company.printEmployees()
            print "[1] Back"
            print "[2] Exit"
            p=int(input('>>>'))
            if (p == 2):
                break
            elif (p == 1):
                continue
            else:
                raise Exception('Pogresan unos, prekida se program.')
                # moze i samo primitivan print da se uradi
                break
        elif(x==4):
            print "Bye"
            break

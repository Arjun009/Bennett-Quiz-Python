import random
import os
import webbrowser
import datetime

#EASY QUESTIONS
list_of_easy_questions=["How many kilometers was the Bennethon?","Who is the caterer for Bennett University?","Which of the following is not a club at Bennett University?",
                        "What is the cost of Cheese Maggi at Bennett University?","Which of the following is not the name of any shop present in Bennett University?",
"What is the name of tuck shop present in Bennett University?","How many teams are present in cricket tournament of Bennett University?",
"How many games were played during Halloween at Bennett University?","Which movie was first played in THE DARK ROOM at Bennett University?",
                        "Which famous Chinese item is not served at Bennett University Mess?","Which of the following is a doctor at Bennett University?","Name the sport which is not played in Bennett University?",
                        "Who was the winner of Bennett miss freshers contest?","Who became the oppo fresh face of Bennett University in male category?",
                        "How many Computer science labs for students are present in Bennett University?","How many acres does Bennett University occupy?","Who is the Sports Officer of Bennett University?",
                        "Which team won the Futheroes 2.0 in Bennett University?","Which company of computers is not used in Bennett University?"]
options_for_easy_questions=["A.9 kms\nB.6 kms\nC.7 kms\nD.5 kms","A.Manglam caterers\nB.Sunrise Group\nC.Utsav Caterers\nD.ICS",
                       "A.Isaac\nB.Flucs\nC.Spandhan\nD.Spark","A.30 Rs.\nB.25 Rs.\nC.35 Rs.\nD.20 Rs.","A.Cold Cafe\nB.Nukkad\nC.Chit Chat\nD.Surya","A.Urja\nB.Surya\nC.Asha\nD.Suraj","A.10\nB.11\nC.9\nD.12",
                            "A.3\nB.4\nC.5\nD.2","A.IT\nB.Harry Potter\nC.Arjun Reddy\nD.Gangs of Wasseypur","A.Noodles\nB.Manchurian\nC.Momos\nD.Fried Rice","A.Nandan Mishra\nB.Abhinav Sharma\nC.Jennifer Thomas\nD.Aarti Singh",
                            "A.Football\nB.Squash\nC.Badminton\nD.Table Tennies","A.Shriya Tyagi\nB.Muskan Kriti\nC.Sahaana Das\nD.Manvi","A.Aditya Bhardwaj\nB.Ritvik Mehta\nC.Madhav Ginoria\nD.Anupam Dhonchak",
                            "A.3\nB.4\nC.5\nD.6","A.67 acres\nB.57 acres\nC.68 acres\nD.58 acres","A.Akansha Singh\nB.Abhinav Bindra\nC.Anjali Rathore\nD.Akansha Chauhan",
                            "A.Ganadores F.C.\nB.Daddy F.C.\nC.ABCDE F.C.\nD.Smoking Aces","A.Dell\nB.Lenovo\nC.Apple\nD.Acer"]
list_of_answers_easy=["B","D","C","C","A","B","A","A","C","C","A","B","D","A","B","C","A","A","B"]
x_halfoptions=["A.9 kms\nB.6 kms","C.Utsav Caterers\nD.ICS","B.Flucs\nC.Spandhan","A.30 Rs.\nC.35 Rs.","A.Cold Cafe\nC.Chit Chat","B.Surya\nD.Suraj","A.10\nD.12","A.3\nB.4","C.Arjun Reddy\nD.Gangs of Wasseypur","C.Momos\nD.Fried Rice","A.Nandan Mishra\nB.Abhinav Sharma",
                            "B.Squash\nC.Badminton","A.Shriya Tyagi\nD.Manvi","A.Aditya Bhardwaj\nC.Madhav Ginoria",
                            "B.4\nC.5","A.69\nC.68","A.Akansha Singh\nD.Akansha Chauhan",
                            "A.Ganadores F.C.\nC.ABCDE F.C.","A.Dell\nB.Lenovo"]
#MEDIUM QUESTIONS
list_of_medium_questions=["In which subject Dr.Rajinder Singh Chauhan did his research ?","Where did Nidhi Sinha ma'am had experienced as Holiday Consultant ?",
                          "In which country did Dr.Rama S Komaragiri done his PhD?","Where did Dr.Vinit Jakhetiya  worked as Senior Engineer?","On what topic did Dr.Sarika Goyal done her Phd?",
                          "From Where did Dr.Suneet Tuli  completed his btech degree?","Where did Prof.V.C.Vivekanandan Sir started his teaching career?","Where did Dr.Trichi Krishnan sir done his Phd in management?",
                          "Where did Dr.Nilanjan Banik sir worked as Associate  Professor?","Where did Dr.Milind Shrikant Padalkar sir done his B.tech?",
                          "How many faculty from School of Management has/have done B.tech?","Where did Dr.Mayank Gupta sir worked as a Teaching Assistant?",
                          "What does Dr.Sangeeta Shukla mam teaches about?","How many faculty from school of management teaches about finance?","Name the associate proffesor of CSE Department"]
options_for_medium_questions=["A.Water  pollution\nB.Industrial waste\nC.Soil pollution\nD.Gene discovery in high value medicinal herbs.",
                              "A.Club Mahindra  \nB.Bharat petroleum corporation\nC.Educomp solutions \nD.Jaypee","A.Germany\nB.America\nC.Singapore\nD.Australia",
                            "A.Hong Kong University of Science and Technology,Hong Kong\nB.LNM Institute of Information Technology,Jaipur\nC.Hong Kong Applied Sciences and Technology Reasearch Institute,Hong Kong\nD.Nanyang Technological University,Singapore",
                       "A.Commutative Algebra\nB.Differential equations \nC.Analysis of Elliptical PDE\nD.Technology and Geometry","A.BITS,Pilani\nB.IIT Delhi\nC.BITS,Hyderabad\nD.IIT Bombay",
 "A.National Law School of India University,Banglore\nB.IIT Kharagpur\nC.Buisiness School of SUNY Buffalo\nD.IIT Roorkee " ,
                         "A.Madras University,India \nB.Rice University,Houston\nC.University of Texas at Dallas,Texas,USA\nD.Tilburg University,Netherlands",
         "A.Madras School of Economics\nB.Calcutta University\nC.Delhi University\nD.Mahindra Ecole Centrale",
                       "A.IIT Roorkee \nB.IIT Kanpur\nC.IIT Kharagpur\nD.IIT Delhi","A.0\nB.1\nC.2\nD.3","A.Jindal School of Government and Public Policy,Jindal Global University\nB.University of Venice Ca'Foscari,Padova & Verona Italy\nC.Cass Business School City University,London,UK\nD.Heriot-Watt University,UK",
                          "A.Marketing \nB.Business Communication\nC.Finance\nD.Economics",  "A.4\nB.6\nC.8\nD.10",  "A.Seung-Hwa Chung\nB.Suneet Tuli\nC.Deepak garg\nD.Samaveer Singh"]
list_of_answers_medium=["D","A","A","C","C","A","A","C","D","D","B","C","B","B","A"]


y_halfoptions=["C.Soil pollution\nD.Gene discovery in high value medicinal herbs.", "A.Club Mahindra  \nD.Jaypee","A.Germany\nB.America",
               "A.Hong Kong University of Science and Technology,Hong Kong\nC.Hong Kong Applied Sciences and Technology Reasearch Institute,Hong Kong",
               "C.Analysis of Elliptical PDE\nD.Technology and Geometry","A.BITS,Pilani\nD.IIT Bombay",
               "A.National Law School of India University,Banglore\nC.Buisiness School of SUNY Buffalo " ,
               "C.University of Texas at Dallas,Texas,USA\nD.Tilburg University,Netherlands",
               "A.Madras School of Economics\nD.Mahindra Ecole Centrale",
               "A.IIT Roorkee \nD.IIT Delhi","B.1\nD.3","B.University of Venice Ca'Foscari,Padova & Verona Italy\nC.Cass Business School City University,London,UK",
               "A.Marketing \nB.Business Communication","B.6\nC.8","A.Seung-Hwa Chung\nD.Samaveer Singh"]

#HARD QUESTIONS
list_of_hard_questions=["Where did Dr.Souradyuti Ghosh done his MS?","In which IIIT did Arti Singh ma’am had her experience before?",
                          "Where did Dr.Vinayak Ranjan worked as assistant professor?","During which year did Dr.Alok Shukla worked as Research Associate",
                          "Where did Dr.Samayveer Singh done his PhD?","In which area did Dr.Talakokula Visalakshi mam done her research?","Where did Dr.Ashvani Kumar had his last experience before joining Bennett University?",
                        "In which year did Dr.Deepali Atheaya completed her M.Tech?","Where did Dr.Ayan Khan worked as Post-Doctoral Research  associate?",
                        "In which year did Dr.Trichi Krishnan completed his Masters in International Management Studies?","In which area did Dr.Nilanjan Banik had done his research?",
                        "Which of the following is the research which was not done by  Dr.Mayank Gupta?","Which faculty from school of management worked in Express Publications?",
                        "Which faculty from school of management worked as Assistant Manager in Axis Bank Limited during 2007-2009?","Where did Dr.Deepak Sangroya had done his MBA?",
                        "Name the only Associate Professor in School of Management at Bennett University?","Name the Professor who teaches economics in School of Management?"]
options_for_hard_questions=["A.IIT Guwahati\nB.IIT Madras\nC.IIT Delhi\nD.IIT Bombay","A.IIIT Hyderabad\nB.IIIT Nuzvid\nC.IIIT Bangalore\nD.IIIT Delhi",
                            "A.IIT Bhubaneshwar\nB.IIT Dhanbad\nC.IIT Kolkata\nD.NIT Durgapur","A.1996-1997\nB.1997-1998\nC.1998-1999\nD.1999-2000",
                            "A.NIT Jalandhar,Punjab\nB.Uttar Pradesh Technology University,Lucknow\nC.Raj Kumar Goel Institute of Technology,Ghaziabad\nD.Netaji Subhas Institute of technology,Delhi",
                            "A.Thermal stress intesity factors\nB.Corrosion in Reinforced Concrete Structures\nC.Electrokinetic Decontamination of Soils\nD.Seismic Site Characterisation",
"A.IIT Roorkee\nB.Diamond Elements Pvt.Ltd.,Surat\nC.Seoul National University,Korea\nD.CCS University,Meerut","A.2002\nB.2003\nC.2004\nD.2005","A.Gitam University,Banglore\nB.IISc,Kolkata\nC.Pusan National University,South Korea\nD.Bilkent University,Turkey",
"A.1982\nB.1992\nC.2002\nD.1994","A.International Business\nB.International Economics\nC.Monetary Economics\nD.Health Economics",
"A.Monetary Economics\nB.Financial Econometrics\nC.Shadow Banking\nD.Asset Pricing","A.Dr.Rajib Sarkar\nB.Dr.S.Ray\nC.Dr.Khanindra Das \nD.Dr.Deepak Sangroya ",
"A.Dr.Sangeetha Shukla \nB.Dr.Anupama Sharma \nC.Dr.Suparna Ray \nD.Dr.Deepika Dhingra ","A.IIT Roorkee \nB.IIT Delhi\nC.NIT Kurukshetra\nD.NIT Warangal",
"A.Dr.S.Ray \nB.Dr.Sangeeta Shukla \nC.Dr.Anupama Sharma\nD.Dr.Pankaj Medhi ","A.Dr.Nilanjan Banik \nB.Dr.Milind Padalkar \nC.Dr.Mayank Gupta \nD.Dr.Sangeeta Shukla "]
list_of_answers_hard=["C","B","B","C", "D", "B","B","A","D","B","B","A","A","D","C","B","A"]
z_halfoptions=["C.IIT Delhi\nD.IIT Bombay","A.IIIT Hyderabad\nB.IIIT Nuzvid",
                            "B.IIT Dhanbad\nC.IIT Kolkata","A.1996-1997\nC.1998-1999",
                            "C.Raj Kumar Goel Institute of Technology,Ghaziabad\nD.Netaji Subhas Institute of technology,Delhi",
                            "B.Corrosion in Reinforced Concrete Structures\nD.Seismic Site Characterisation",
"B.Diamond Elements Pvt.Ltd.,Surat\nC.Seoul National University,Korea\nD.CCS University,Meerut","A.2002\nD.2005","C.Pusan National University,South Korea\nD.Bilkent University,Turkey",
"B.1992\nC.2002","A.International Business\nB.International Economics",
"A.Monetary Economics\nB.Financial Econometrics","A.Dr.Rajib Sarkar\nD.Dr.Deepak Sangroya ",
"C.Dr.Suparna Ray \nD.Dr.Deepika Dhingra ","C.NIT Kurukshetra\nD.NIT Warangal",
"A.Dr.S.Ray \nB.Dr.Sangeeta Shukla ","A.Dr.Nilanjan Banik\nC.Dr.Mayank Gupta  "]

#PROFILE AND INSTRUCTIONS
print("\t*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
print("   "+"\t\t\t\tWelcome to Bennett Quiz!\n".upper())
print("\t*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n\n")
bb=input("Enter Your name"+"  ")
file_3=open("12345.txt","r")
cc=file_3.read()
z=cc.split()
while True:
    if bb not in z:
        print("Hello",bb)
        break
    else:
        print("Bye! User Already Exist")
        bb=input("Enter your name"+"  ")
file_1=open("12345.txt","a")
file_1.write(str(bb)+" ")
file_1.close()
            
course=(input("Enter your course: "+"  ").upper())

print("\nHere are the instructions for the game: ".upper())
print("\n1.Your response should be in the form of A,B,C,D")
print("2.There are total 10 questions, 4 easy, 3 medium and 3 hard ones")
print("3.The game continues till you answer any wrong question or answer all the questions.")
print("4.There are two life lines a. Flip the question ")
print("                                    "+"b. 50-50 (Removes two options)")
print("5.For flip the question use key P \n For 50-50 use key f")
print("6.Attention! you can use lifetime only one time !")

print("\nSo "+str(bb)+" ! Are you ready to play?\nType yes or no accordingly.")
ready=input().upper()
timenow=datetime.datetime.now()
print("You are playing Bennett Quiz on: ",timenow)
if ready=="YES":
    print("\nOkay let's begin the game")
    #WORKING
    score=0
    r=0
    i=0
    j=0
    k=0
    passs=1
    fifty=1
    a=set()
    while len(a)!=6:
        a.add(random.randint(0,18))
    b=list(a)
    m=set()
    while len(m)!=6:
        m.add(random.randint(0,14))
    h=list(m)
    d=set()
    while len(d)!=6:
        d.add(random.randint(0,18))
    v=list(d)
    while score<4:
        #LEVEL 1- EASY
        #Generate a random question from the list of easy questions
        print("\nQuestion NO. "+str(score+1)+": ")
        print(list_of_easy_questions[b[i]])
        print(options_for_easy_questions[b[i]])
        answer=input("\nWhat is your final answer?\n").upper()
        c=b[i]

        #FOR PASSING
        if answer=="P" and passs==1:
            print("\nQuestion NO. "+str(score+1)+": ")
            print(list_of_easy_questions[b[i+1]])
            print(options_for_easy_questions[b[i+1]])
            answer=input("\nWhat is your final answer?\n").upper()
            passs-=1
            c=b[i+1]
            i+=1
            if answer=="F" and fifty==1:
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_easy_questions[b[i]])
                print(x_halfoptions[b[i]])
                c=b[i]
                answer=input("\nWhat is your final answer?\n").upper()
                fifty-=1
            elif answer=="F" and fifty==0:
                print("SORRY")
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_easy_questions[b[i]])
                print(options_for_easy_questions[b[i]])
                answer=input("\nWhat is your final answer?\n").upper()
            elif answer=="P" and passs==0:
                print("SORRY")
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_easy_questions[b[i]])
                print(options_for_easy_questions[b[i]])
                answer=input("\nWhat is your final answer?\n").upper()
                c=b[i]
        elif answer=="P" and passs==0:
            print("SORRY")
            print("\nQuestion No. "+str(score+1)+": ")
            print(list_of_easy_questions[b[i]])
            print(options_for_easy_questions[b[i]])
            answer=input("\nWhat is your final answer?\n").upper()
            c=b[i]

        #FOR FIFTY
        if answer=="F" and fifty==1:
            print("\nQuestion No. "+str(score+1)+": ")
            print(list_of_easy_questions[b[i]])
            print(x_halfoptions[b[i]])
            answer=input("\nWhat is your final answer?\n").upper()
            c=b[i]
            fifty-=1
            if answer=="P" and passs==1:
                print("\nQuestion NO. "+str(score+1)+": ")
                print(list_of_easy_questions[b[i+1]])
                print(options_for_easy_questions[b[i+1]])
                answer=input("\nWhat is your final answer?\n").upper()
                c=b[i+1]
                i+=1
                passs-=1
            elif answer=="P" and passs==0:
                print("SORRY")
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_easy_questions[b[i]])
                print(x_halfoptions[b[i]])
                answer=input("\nWhat is your final answer?\n").upper()
                c=b[i]
            elif answer=="F" and fifty==0:
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_easy_questions[b[i]])
                print(x_halfoptions[b[i]])
                answer=input("\nWhat is your final answer?\n").upper()
                c=b[i]
        elif answer=="F" and fifty==0:
            print("SORRY! You have already used Fifty-Fifty!!")
            print("\nQuestion No. "+str(score+1)+": ")
            print(list_of_easy_questions[b[i]])
            print(options_for_easy_questions[b[i]])
            answer=input("\nWhat is your final answer?\n").upper()
            c=b[i]


        #FOR CHECKING
        if answer==list_of_answers_easy[c]:
            score+=1
            print("CORRECT! "+str(answer)+" is the right answer.")
            print("Your current score is: ",score)
            i+=1
        else:
            print("\nOOPS! "+str(answer)+" is wrong.\n"+str(list_of_answers_easy[b[i]])+" is the correct answer.")
            print("\nGAME OVER! Your final score is: "+str(score)+" /10. ")
            print("Thanks for playing "+str(bb)+" !!")
            webbrowser.open("https://cdn.grb.uk.com/fileadmin/uploads/blog/content/never_give_up.gif")
            break
        
    while score>3 and score<7:
        #LEVEL 2- MEDIUM
        #Generate a random question from the list of medium questions
        print("\nQuestion NO. "+str(score+1)+": ")
        print(list_of_medium_questions[h[j]])
        print(options_for_medium_questions[h[j]])
        answer=input("\nWhat is your final answer?\n").upper()
        p=h[j]
        #FOR PASSING
        if answer=="P" and passs==1:
            print("\nQuestion NO. "+str(score+1)+": ")
            print(list_of_medium_questions[h[j+1]])
            print(options_for_medium_questions[h[j+1]])
            answer=input("\nWhat is your final answer?\n").upper()
            passs-=1
            p=h[j+1]
            j+=1
            if answer=="F" and fifty==1:
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_medium_questions[h[j]])
                print(y_halfoptions[h[j]])
                p=h[j]
                answer=input("\nWhat is your final answer?\n").upper()
                fifty-=1
            elif answer=="F" and fifty==0:
                print("SORRY")
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_medium_questions[h[j]])
                print(options_for_medium_questions[h[j]])
                answer=input("\nWhat is your final answer?\n").upper()
            elif answer=="P" and passs==0:
                print("SORRY")
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_medium_questions[h[j]])
                print(options_for_medium_questions[h[j]])
                answer=input("\nWhat is your final answer?\n").upper()
                p=h[j]
        elif answer=="P" and passs==0:
            print("SORRY")
            print("\nQuestion No. "+str(score+1)+": ")
            print(list_of_medium_questions[h[j]])
            print(options_for_medium_questions[h[j]])
            answer=input("\nWhat is your final answer?\n").upper()
            p=h[j]

        #FOR FIFTY
        if answer=="F" and fifty==1:
            print("\nQuestion No. "+str(score+1)+": ")
            print(list_of_medium_questions[h[j]])
            print(y_halfoptions[h[j]])
            answer=input("\nWhat is your final answer?\n").upper()
            p=h[j]
            fifty-=1
            if answer=="P" and passs==1:
                print("\nQuestion NO. "+str(score+1)+": ")
                print(list_of_medium_questions[h[j+1]])
                print(options_for_medium_questions[h[j+1]])
                answer=input("\nWhat is your final answer?\n").upper()
                p=h[j+1]
                j+=1
                passs-=1
            elif answer=="P" and passs==0:
                print("SORRY")
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_medium_questions[h[j]])
                print(y_halfoptions[h[j]])
                answer=input("\nWhat is your final answer?\n").upper()
                p=h[j]
            elif answer=="F" and fifty==0:
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_medium_questions[h[j]])
                print(y_halfoptions[h[j]])
                answer=input("\nWhat is your final answer?\n").upper()
                p=h[j]
        elif answer=="F" and fifty==0:
            print("SORRY! You have already used Fifty-Fifty!!")
            print("\nQuestion No. "+str(score+1)+": ")
            print(list_of_medium_questions[h[j]])
            print(options_for_medium_questions[h[j]])
            answer=input("\nWhat is your final answer?\n").upper()
            p=h[j]


        #FOR CHECKING
        if answer==list_of_answers_medium[p]:
            score+=1
            print("CORRECT! "+str(answer)+" is the right answer.")
            print("Your current score is: ",score)
            j+=1
        else:
            print("\nOOPS! "+str(answer)+" is wrong.\n"+str(list_of_answers_medium[h[j]])+" is the correct answer.")
            print("\nGAME OVER! Your final score is: "+str(score)+" /10. ")
            print("Thanks for playing "+str(bb)+" !!")
            webbrowser.open("https://cdn.grb.uk.com/fileadmin/uploads/blog/content/never_give_up.gif")
            break

        

    while score>6 and score<10:
        #LEVEL 3- HARD
        #Generate a random question from the list of hard questions
        print("\nQuestion NO. "+str(score+1)+": ")
        print(list_of_hard_questions[v[k]])
        print(options_for_hard_questions[v[k]])
        answer=input("\nWhat is your final answer?\n").upper()
        e=v[k]

        #FOR PASSING
        if answer=="P" and passs==1:
            print("\nQuestion NO. "+str(score+1)+": ")
            print(list_of_hard_questions[v[k+1]])
            print(options_for_hard_questions[v[k+1]])
            answer=input("\nWhat is your final answer?\n").upper()
            passs-=1
            e=v[k+1]
            k+=1
            if answer=="F" and fifty==1:
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_hard_questions[v[k]])
                print(z_halfoptions[v[k]])
                e=v[k]
                answer=input("\nWhat is your final answer?\n").upper()
                fifty-=1
            elif answer=="F" and fifty==0:
                print("SORRY")
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_hard_questions[v[k]])
                print(options_for_hard_questions[v[k]])
                answer=input("\nWhat is your final answer?\n").upper()
            elif answer=="P" and passs==0:
                print("SORRY")
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_hard_questions[v[k]])
                print(options_for_hard_questions[v[k]])
                answer=input("\nWhat is your final answer?\n").upper()
                e=v[k]
        elif answer=="P" and passs==0:
            print("SORRY")
            print("\nQuestion No. "+str(score+1)+": ")
            print(list_of_hard_questions[v[k]])
            print(options_for_hard_questions[v[k]])
            answer=input("\nWhat is your final answer?\n").upper()
            e=v[k]

        #FOR FIFTY
        if answer=="F" and fifty==1:
            print("\nQuestion No. "+str(score+1)+": ")
            print(list_of_hard_questions[v[k]])
            print(z_halfoptions[v[k]])
            answer=input("\nWhat is your final answer?\n").upper()
            e=v[k]
            fifty-=1
            if answer=="P" and passs==1:
                print("\nQuestion NO. "+str(score+1)+": ")
                print(list_of_hard_questions[v[k+1]])
                print(options_for_hard_questions[v[k+1]])
                answer=input("\nWhat is your final answer?\n").upper()
                e=v[k+1]
                k+=1
                passs-=1
            elif answer=="P" and passs==0:
                print("SORRY")
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_hard_questions[v[k]])
                print(z_halfoptions[v[k]])
                answer=input("\nWhat is your final answer?\n").upper()
                e=v[k]
            elif answer=="F" and fifty==0:
                print("\nQuestion No. "+str(score+1)+": ")
                print(list_of_hard_questions[v[k]])
                print(z_halfoptions[v[k]])
                answer=input("\nWhat is your final answer?\n").upper()
                e=v[k]
        elif answer=="F" and fifty==0:
            print("SORRY! You have already used Fifty-Fifty!!")
            print("\nQuestion No. "+str(score+1)+": ")
            print(list_of_hard_questions[v[k]])
            print(options_for_hard_questions[v[k]])
            answer=input("\nWhat is your final answer?\n").upper()
            e=v[k]


        #FOR CHECKING
        if answer==list_of_answers_hard[e]:
            score+=1
            print("CORRECT! "+str(answer)+" is the right answer.")
            print("Your current score is: ",score)
            k+=1
        else:
            print("\nOOPS! "+str(answer)+" is wrong.\n"+str(list_of_answers_hard[v[k]])+" is the correct answer.")
            print("\nGAME OVER! Your final score is: "+str(score)+" /10. ")
            print("Thanks for playing "+str(bb)+" !!")
            webbrowser.open("https://cdn.grb.uk.com/fileadmin/uploads/blog/content/never_give_up.gif")
            break
        
    if score==10:
        print("\nCONGRATULATIONS. YOU HAVE WON THE GAME!")
        print("\nThanks for playing "+str(bb)+" !!")
        os.system("C:/Users/Siddhanth/Downloads/videoplayback.m4a")
        webbrowser.open("https://media.giphy.com/media/VoByuwmUpCOXe/giphy.gif")
else:
    print(str(bb)+"\nOkay. Come back when you are ready.")

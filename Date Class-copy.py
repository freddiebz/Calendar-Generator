#Author: Frederica Zhang
#Date: Nov. 2, 2019
#Purpose: Output a date class with a calendar's month and year
#T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T
from tkinter import *

window = Tk()
window.title ("Date and Calendar")

userDay = StringVar()
userDay.set (value = "")

userMonth = StringVar()
userMonth.set (value = "")

userYear = StringVar()
userYear.set (value = "")


#   Date Class
#Author: Frederica Zhang
#Date: Nov. 2, 2019
#Purpose: Create a date for the user
#Fields:
#   - intDay: number from 1 - maxDay to represent the day
#   - intMonth: number from 1 -12 to represent the month
#   - intYear: number >= 1600 to represent the year
#Methods:
#   - returnMonthName: returns the name of the month
#   - returnLeapYear: determines if the year is a leap year
#   - returnMaxDay: determine the max. days of the month
#   - calcZeller: determine the day of week of the inputted date
#   - returnDayName: returns the name of the day
#   - calcValid: determine if the inputted date is valid
#   - getDate: get a date from the user
#   - getPositiveInteger: edit for a postive integer between a min. and a max. value
#   -__str__: changes the date class into a string (e.g. Friday, 13 October 2002)
#   - displayCalendar: print the calendar, month, and year of the date
#   - dayOfYear: determine the dates day of the year
#   - textboxCalendar: prints calendar in a textbox

class Date:
    def __init__ (self, day = 1, month = 1, year = 2018):

        if self.calcValid(day, month, year):
            self.year = year
            self.month = month
            self.day = day
        else:
            self.year = 2018
            self.month = 1
            self.day = 1


    #returnMonthName
    #Author: Frederica Zhang
    #Date: Nov. 5, 2019
    #Purpose: Returns the name of the month
    #Parameters: One integer(intMonth)
    #Returns: Name of month
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def returnMonthName(self, intMonth = 1):

        if intMonth == 1:
            strMonth = "January"
            
        elif intMonth == 2:
            strMonth = "February"
            
        elif intMonth == 3:
            strMonth = "March"
            
        elif intMonth == 4:
            strMonth = "April"
            
        elif intMonth == 5:
            strMonth = "May"
            
        elif intMonth == 6:
            strMonth = "June"
            
        elif intMonth == 7:
            strMonth = "July"
            
        elif intMonth == 8:
            strMonth = "August"
            
        elif intMonth == 9:
            strMonth = "September"
            
        elif intMonth == 10:
            strMonth = "October"
            
        elif intMonth == 11:
            strMonth = "November"
            
        else:
            strMonth = "December"

        return strMonth

        
    #returnLeapYear
    #Author: Frederica Zhang
    #Date: Nov. 5, 2019
    #Purpose: Determines if the year is a leap year
    #Parameters: One integer(intYear)
    #Returns: True if the year is a leap year
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def returnLeapYear(self, intYear = 2018):

        if intYear % 100 == 0:
            if intYear % 400 == 0:
                leapYear = True
            else:
                leapYear = False
        else:
            if intYear % 4 == 0:
                leapYear = True
            else:
                leapYear = False

        return leapYear


    #returnMaxDay
    #Author: Frederica Zhang
    #Date: Nov. 5, 2019
    #Purpose: Determine the max. days of the month
    #Parameters: Two integer(intMonth and intYear)
    #Returns: Max. days of inputted month
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def returnMaxDay(self, intMonth = 1, intYear = 2018):

        if (intMonth % 2 == 1 and intMonth <=7) or (intMonth % 2 == 0 and intMonth >= 8):
            maximum = 31
        elif intMonth != 2 and (intMonth % 2 == 0 and intMonth <=7) or (intMonth % 2 == 1 and intMonth >= 8):
            maximum = 30
        else:
            if self.returnLeapYear(intYear):
                maximum = 29
            else:
                maximum = 28

        return maximum


    #calcZeller
    #Author: Frederica Zhang
    #Date: Nov. 6, 2019
    #Purpose: Determine the day of week of the inputted date
    #Parameters: 3 integers (intDay, intMonth, intYear)
    #Returns: Day of the week as an integer from 0-6
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def calcZeller(self, intDay = 1, intMonth = 1, intYear = 2018):

        month = intMonth - 2
        year = intYear
        if month <= 0:
            month = month + 12
            year = year - 1

        p = year // 100
        r = year % 100
        dayOfWeek = (intDay + (26 * month - 2)//10 + r + r//4 + p//4 + 5 * p) % 7

        return dayOfWeek


    #returnDayName
    #Author: Frederica Zhang
    #Date: Nov. 6, 2019
    #Purpose: Returns the name of the day
    #Parameters: 3 integers (intDay, intMonth, intYear)
    #Returns: Name of day of the week
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def returnDayName(self, intDay = 1, intMonth = 1, intYear = 2018):

        dayOfWeek = self.calcZeller(intDay, intMonth, intYear)

        if dayOfWeek == 0:
            strDay = "Sunday"
        elif dayOfWeek == 1:
            strDay = "Monday"
        elif dayOfWeek == 2:
            strDay = "Tuesday"
        elif dayOfWeek == 3:
            strDay = "Wednesday"
        elif dayOfWeek == 4:
            strDay = "Thursday"
        elif dayOfWeek == 5:
            strDay = "Friday"
        else:
            strDay = "Saturday"

        return strDay


    #calcValid
    #Author: Frederica Zhang
    #Date: Nov. 6, 2019
    #Purpose: Determine if the inputted date is valid
    #Parameters: 3 integers (intDay, intMonth, intYear)
    #Returns: True if the date is valid
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def calcValid(self, intDay = 1, intMonth = 1, intYear = 2018):

        if intYear >= 1600 and intYear <= 2500:
            validYear = True
        else:
            validYear = False

        if intMonth >= 1 and intMonth <=12:
            validMonth = True
        else:
            validMonth = False

        if intDay >= 1 and intDay <= self.returnMaxDay(intMonth, intYear):
            validDay = True
        else:
            validDay = False

        if validYear and validMonth and validDay:
            validDate = True
        else:
            validDate = False

        return validDate


    #getDate:
    #Author: Frederica Zhang
    #Date: Nov. 6, 2019
    #Purpose: Get the date from the user
    #Parameters: None
    #Returns: Date class
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def getDate(self):

        day = 0
        month = 0
        year = 0
        firstTry = True
        
        while not self.calcValid(day, month, year):
            if not firstTry:
                print("That date is not valid! Re-enter a proper one this time >:( ")
            day = self.getPositiveInteger("Enter the day: ", 31, 1)
            month = self.getPositiveInteger("Enter the number of the month(e.g. April is 4): ", 12, 1)
            year = self.getPositiveInteger("Enter the year (1600 - 2500): ", 2500, 1600)
            firstTry = False
        
        date = Date(day, month, year)

        return date


    #getPositiveInteger
    #Author: Frederica Zhang
    #Date: Oct. 20, 2019
    #Purpose: Edit for a postive integer between a min. and a max. value
    #Parameters: One string(strPrompt), two integers (low and high)
    #Returns: A positive integer between a min. and a max. value
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def getPositiveInteger(self, strPrompt, high, low):

        number = -1
        firstInput = True
        
        while number < low or number > high:
            if firstInput == False:
                print("Please input a POSSIBLE number.")
                
            strNumber = input(strPrompt)
            
            while not strNumber.isdigit():
                print("Please input a POSSIBLE number.")
                strNumber = input(strPrompt)
            number = int(strNumber)
            firstInput = False
            
        return number


    #__str__
    #Author: Frederica Zhang
    #Date: Nov. 6, 2019
    #Purpose: Changes the date class into a string (e.g. Friday, 13 October 2002)
    #Parameters: None
    #Returns: String form of Date class
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def __str__(self):

        dayOfWeek = self.returnDayName(self.day, self.month, self.year)
        day = str(self.day) + " "
        monthName = self.returnMonthName(self.month) + " "
        year = str(self.year)
        
        date = dayOfWeek + ", " + day + monthName + year

        return date


    #displayCalendar
    #Author: Frederica Zhang
    #Date: Nov. 8 2019
    #Purpose: Print the calendar, month, and year of the date
    #Parameters: None
    #Returns: Nothing
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def displayCalendar(self):

        calendarHeader = self.returnMonthName(self.month) + " " + str(self.year)
        print("%9s%15s%9s" % (" ", calendarHeader, " "))
        print("%33s" % ("Sun  Mon  Tue  Wed  Thu  Fri  Sat"))

        startDay = self.calcZeller(1, self.month, self.year)
        maxDay = self.returnMaxDay(self.month, self.year)

        day = 1
        if day == 1:
            for weekDay in range(7):

                if weekDay >= startDay:
                    print("%3s" % (day), end = "  ")
                    day = day + 1
                else:
                    print("%3s" % (" "), end = "  ")

            print()
                
        for restOfDays in range(abs(8 - startDay), maxDay + 1, 7):

            if restOfDays + 7 <= maxDay:
                for weekDay in range(restOfDays, restOfDays + 7):
                    print("%3s" % (weekDay), end = "  ")
            else:
                for weekDay in range(restOfDays, maxDay + 1):
                    print("%3s" % (weekDay), end = "  ")
                
            print()

        print()


    #dayOfYear
    #Author: Frederica Zhang
    #Date: Nov. 8, 2019
    #Purpose: Determine the dates day of the year
    #Parameters: None
    #Returns: Integer between 1-365
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def dayOfYear(self):

        dayOfYear = 0
        
        for months in range(1, self.month):
            dayOfYear = dayOfYear + self.returnMaxDay(months, self.year)

        dayOfYear = dayOfYear + self.day

        return dayOfYear


    #textboxCalendar
    #Author: Frederica Zhang
    #Date: Nov. 11, 2019
    #Purpose: Prints calendar in a textbox
    #Parameters: None
    #Returns: Nothing
    #~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
    def textboxCalendar(self):

        calendarHeader = self.returnMonthName(self.month) + " " + str(self.year) + "\n"
        display.insert(INSERT, calendarHeader)
        display.insert(INSERT, "%35s \n" % (" Sun  Mon  Tue  Wed   Thu    Fri    Sat"))
        display.insert(INSERT, "\n")
        startDay = self.calcZeller(1, self.month, self.year)
        maxDay = self.returnMaxDay(self.month, self.year)

        day = 1
        if day == 1:
            for weekDay in range(7):

                if weekDay >= startDay:
                    display.insert(INSERT, "%5s   " % (day))
                    day = day + 1
                else:
                    display.insert(INSERT, "%6s   " % (" "))
 
            display.insert(INSERT, "\n")
                
        for restOfDays in range(abs(8 - startDay), maxDay + 1, 7):

            if restOfDays + 7 <= maxDay:
                for weekDay in range(restOfDays, restOfDays + 7):
                    if weekDay//10 == 0:
                        display.insert(INSERT, "%5s   " % (weekDay))
                    else:
                        display.insert(INSERT, "%4s   " % (weekDay))
            else:
                for weekDay in range(restOfDays, maxDay + 1):
                    display.insert(INSERT, "%4s   " % (weekDay))
                
            display.insert(INSERT, "\n")

        display.insert(INSERT, "\n")
        
        display.tag_config("header", justify = "center", font = ("Times", 20, "normal"), underline = True)
        display.tag_config("center", justify = "center")
        display.tag_add("header", "1.0", "2.0")
        display.tag_add("center", "3.0", "5.0")

#displayDate
#Author: Frederica Zhang
#Date: Nov. 11, 2019
#Purpose: Displays date and calendar in a textbox
#Parameters: None
#Returns: Nothing
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~    
def displayDate():

    display.delete(1.0, END)
    userDate = Date()
    strDay = userDay.get()
    strMonth = userMonth.get()
    strYear = userYear.get()

    if strDay.isdigit() and strMonth.isdigit() and strYear.isdigit():
        intDay = int(userDay.get())
        intMonth = int(userMonth.get())
        intYear = int(userYear.get())

        if userDate.calcValid(intDay, intMonth, intYear):
            lblPrompt2.config(text = "")
            userDate = Date(intDay, intMonth, intYear)

            display.insert(INSERT, userDate)
            display.insert(INSERT, "\n")
            display.insert(INSERT, "\n")      
            userDate.textboxCalendar()
            dayOfYear = userDate.dayOfYear()
            display.insert(INSERT, "This is day %i of %i!" % (dayOfYear, userDate.year))

        else:
            lblPrompt2.config(text = "Please enter a valid date.")
            
    else:
        lblPrompt2.config(text = "Please enter a valid date.")


#editCalendar
#Author: Frederica Zhang
#Date: Nov. 15, 2019
#Purpose: Changes month and year and displays calendar
#Parameters: One integer (number)
#Returns: Nothing
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~            
def editCalendar(number):

    strMonth = userMonth.get()
    strYear = userYear.get()

    if strMonth.isdigit() and strYear.isdigit():
        originalMonth = int(userMonth.get())
        originalYear = int(userYear.get())
        #subtract month
        if number == 0:
            newMonth = originalMonth - 1
            userMonth.set(newMonth)
            if newMonth == 0 and originalYear > 1600:
                userMonth.set(12)
                userYear.set(originalYear - 1)
                if originalYear - 1 < 1700:
                    btnDownCentury.config(state = DISABLED)  
                
            if newMonth == 1 and originalYear == 1600:
                btnDownMonth.config(state = DISABLED)
                btnDownCentury.config(state = DISABLED)
                btnDownYear.config(state = DISABLED)

            btnUpMonth.config(state = NORMAL)
            btnUpCentury.config(state = NORMAL)
            btnUpYear.config(state = NORMAL)
        #add month
        elif number == 1:
            newMonth = originalMonth + 1
            userMonth.set(newMonth)
            if newMonth == 13 and originalYear < 2500:
                userMonth.set(1)
                userYear.set(originalYear + 1)
                if originalYear + 1 > 2400:
                    btnUpCentury.config(state = DISABLED)

            if newMonth == 12 and originalYear == 2500:
                btnUpMonth.config(state = DISABLED)
                btnUpCentury.config(state = DISABLED)
                btnUpYear.config(state = DISABLED)

            btnDownMonth.config(state = NORMAL)
            btnDownCentury.config(state = NORMAL)
            btnDownYear.config(state = NORMAL)
        #subtract century
        elif number == 2:
            newYear = originalYear - 100
            userYear.set(newYear)
            if newYear < 1700:
                btnDownCentury.config(state = DISABLED)
                if newYear % 100 == 0:
                    btnDownYear.config(state = DISABLED)
                    if originalMonth == 1:
                        btnDownMonth.config(state = DISABLED)

            btnUpMonth.config(state = NORMAL)
            btnUpYear.config(state = NORMAL)
            btnUpCentury.config(state = NORMAL)
        #add century
        elif number == 3:
            newYear = originalYear + 100
            userYear.set(newYear)
            if newYear > 2400:
                btnUpCentury.config(state = DISABLED)
                if newYear % 100 == 0:
                    btnUpYear.config(state = DISABLED)
                    if originalMonth == 12:
                        btnUpMonth.config(state = DISABLED)

            btnDownMonth.config(state = NORMAL)
            btnDownCentury.config(state = NORMAL)
            btnDownYear.config(state = NORMAL)
        #subtract year
        elif number == 4:
            newYear = originalYear - 1
            userYear.set(newYear)
                
            if newYear < 1700:
                btnDownCentury.config(state = DISABLED)
                if newYear % 100 == 0:
                    btnDownYear.config(state = DISABLED)
                    if originalMonth == 1:
                        btnDownMonth.config(state = DISABLED)
                    else:
                        btnDownMonth.config(state = NORMAL)

            btnUpMonth.config(state = NORMAL)
            btnUpYear.config(state = NORMAL)
            if newYear <= 2400:
                btnUpCentury.config(state = NORMAL)
        #add year
        else:
            newYear = originalYear + 1
            userYear.set(newYear)
            if newYear > 2400:
                btnUpCentury.config(state = DISABLED)
                if newYear % 100 == 0:
                    btnUpYear.config(state = DISABLED)
                    if originalMonth == 12:
                        btnUpMonth.config(state = DISABLED)
                    else:
                        btnUpMonth.config(state = NORMAL)

            btnDownMonth.config(state = NORMAL)
            btnDownYear.config(state = NORMAL)
            if newYear >= 1700:
                btnDownCentury.config(state = NORMAL)

        displayDate()


#~~~MAIN PROGRAM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

lblPrompt = Label(window, text = "Enter a date and we'll print out \nthe month's calendar for you to see.", \
                  font = ("Comic Sans", 17, "normal"))
display = Text(window, height = 20, width = 31, font = ("Times", 15, "normal"), wrap = WORD)

entryGroup = LabelFrame(window, text = "What's the Date?", font = ("Comic Sans", 15, "bold"))
lblDay = Label(entryGroup, text = "Enter the day: " ,font = ("Comic Sans", 13, "normal"))
lblMonth = Label(entryGroup, text = "Enter the number of the month (e.g. April is 4) : ",\
                 font = ("Comic Sans", 13, "normal"))
lblYear =  Label(entryGroup, text = "Enter the year (1600 and later only) : ", \
                 font = ("Comic Sans", 13, "normal"))
entDay = Entry(entryGroup, textvariable = userDay, width = 8)
entMonth = Entry(entryGroup, textvariable = userMonth, width = 8)
entYear = Entry(entryGroup, textvariable = userYear, width = 8)

editCalendarGroup = LabelFrame(window, text = "Change the calendar directly!", font = ("Comic Sans", 15, "bold"))
lblEditMonth = Label(editCalendarGroup, text = "Month", font = ("Comic Sans", 15, "normal"))
lblEditCentury = Label(editCalendarGroup, text = "Century", font = ("Comic Sans", 15, "normal"))
lblEditYear = Label(editCalendarGroup, text = "Year", font = ("Comic Sans", 15, "normal"))
btnDownMonth = Button(editCalendarGroup, text = "<", font = ("Comic Sans", 15, "normal"), \
                      command = lambda: editCalendar(0))
btnUpMonth = Button(editCalendarGroup, text = ">", font = ("Comic Sans", 13, "normal"), \
                    command = lambda: editCalendar(1))
btnDownCentury = Button(editCalendarGroup, text = "<", font = ("Comic Sans", 13, "normal"), \
                        command = lambda: editCalendar(2))
btnUpCentury = Button(editCalendarGroup, text = ">", font = ("Comic Sans", 13, "normal"), \
                      command = lambda: editCalendar(3))
btnDownYear = Button(editCalendarGroup, text = "<", font = ("Comic Sans", 13, "normal"), \
                     command = lambda: editCalendar(4))
btnUpYear = Button(editCalendarGroup, text = ">", font = ("Comic Sans", 13, "normal"), \
                   command = lambda: editCalendar(5))

btnPrint = Button(window, text = "Show Calendar!", font = ("Comic Sans", 20, "bold"), \
                  width = 15, command = lambda: displayDate())
lblPrompt2 = Label(window, text = "", font = ("Comic Sans", 15, "normal"))

#place widgets
lblPrompt.grid(column = 1, row = 0, padx = 5, pady = 5)
display.grid(column = 0, row = 0, rowspan = 5, padx = 5, pady = 5)

entryGroup.grid(column = 1, row = 1, padx = 5, pady = 5)
lblDay.grid(column = 0, row = 0, sticky = W, padx = 10, pady = 5)
lblMonth.grid(column = 0, row = 1, sticky = W, padx = 10, pady = 5)
lblYear.grid(column = 0, row = 2, sticky = W, padx = 10, pady = 5)
entDay.grid(column = 1, row = 0, padx = 5, pady = 5)
entMonth.grid(column = 1, row = 1, padx = 5, pady = 5)
entYear.grid(column = 1, row = 2, padx = 5, pady = 5)

editCalendarGroup.grid(column = 1, row = 2, padx = 5, pady = 5)
lblEditMonth.grid(column = 0, columnspan = 2, row = 0, padx = 25, pady = 5)
lblEditCentury.grid(column = 2, columnspan = 2, row = 0, padx = 25, pady = 5)
lblEditYear.grid(column = 4, columnspan = 2, row = 0, padx = 25, pady = 5)
btnDownMonth.grid(column = 0, row = 1, sticky = E, padx = 5, pady = 5)
btnUpMonth.grid(column = 1, row = 1, sticky = W, padx = 5, pady = 5)
btnDownCentury.grid(column = 2, row = 1, sticky = E, padx = 5, pady = 5)
btnUpCentury.grid(column = 3, row = 1, sticky = W, padx = 5, pady = 5)
btnDownYear.grid(column = 4, row = 1, sticky = E, padx = 5, pady = 5)
btnUpYear.grid(column = 5, row = 1, sticky = W, padx = 5, pady = 5)

btnPrint.grid(column = 1, row = 3, padx = 10, pady = 5)
lblPrompt2.grid(column = 1, row = 4, padx = 5, pady = 5)

mainloop()
    

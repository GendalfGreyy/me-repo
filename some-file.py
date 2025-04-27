def verifacation(N):
    if N <= 10 or N >= 20:
        if (N % 10) == 0 or ((N % 10) >= 5 and (N % 10) <= 9):
            return "-- часов"
        elif (N % 10) == 1:
            return "-- час"
        else:
            return "-- часа"
    else:
        return "-- часов"

def todaymake():
    print("1:", "Время потраченное на спорт             --", TODAYtimeforSPORT - TODAYtimeforSPORT // 60 * 60, (2 - len(str(TODAYtimeforSPORT - TODAYtimeforSPORT // 60 * 60))) * " ", "-- минут --", TODAYtimeforSPORT // 60, verifacation(TODAYtimeforSPORT // 60), sep="")
    print("2:", "Время потраченное на с++               --", TODAYtimeforC - TODAYtimeforC // 60 * 60, (2 - len(str(TODAYtimeforC - TODAYtimeforC // 60 * 60))) * " ", "-- минут --", TODAYtimeforC // 60, "-- часов", sep="")
    print("3:", "Время потраченное на python            --", TODAYtimeforPYTHON - TODAYtimeforPYTHON // 60 * 60, (2 - len(str(TODAYtimeforPYTHON - TODAYtimeforPYTHON // 60 * 60))) * " ", "-- минут --", TODAYtimeforPYTHON // 60, verifacation(TODAYtimeforPYTHON // 60), sep="")
    print("4:", "Время потраченное на егэ по русскому   --", TODAYtimeforEGER - TODAYtimeforEGER // 60 * 60, (2 - len(str(TODAYtimeforEGER - TODAYtimeforEGER // 60 * 60))) * " ", "-- минут --", TODAYtimeforEGER // 60, verifacation(TODAYtimeforEGER // 60), sep="")
    print("5:", "Время потраченное на егэ по математике --", TODAYtimeforEGEM - TODAYtimeforEGEM // 60 * 60, (2 - len(str(TODAYtimeforEGEM - TODAYtimeforEGEM // 60 * 60))) * " ", "-- минут --", TODAYtimeforEGEM // 60, verifacation(TODAYtimeforEGEM // 60), sep="")
    print("6:", "Время потраченное на по информатике    --", TODAYtimeforEGEI - TODAYtimeforEGEI // 60 * 60, (2 - len(str(TODAYtimeforEGEI - TODAYtimeforEGEI // 60 * 60))) * " ", "-- минут --", TODAYtimeforEGEI // 60, verifacation(TODAYtimeforEGEI // 60), sep="")
    print("7:", "Время потраченное на уборку            --", TODAYtimeforCLEANING - TODAYtimeforCLEANING // 60 * 60, (2 - len(str(TODAYtimeforCLEANING - TODAYtimeforCLEANING // 60 * 60))) * " ", "-- минут --", TODAYtimeforCLEANING // 60, verifacation(TODAYtimeforCLEANING // 60), sep="")
    print("8:", "Время потраченное на ТОЙФЛ             --", TODAYtimeforTOYFL - TODAYtimeforTOYFL // 60 * 60, (2 - len(str(TODAYtimeforTOYFL - TODAYtimeforTOYFL // 60 * 60))) * " ", "-- минут --", TODAYtimeforTOYFL // 60, verifacation(TODAYtimeforTOYFL // 60), sep="")
    print("9:", "Время потраченное на ЧТЕНИЕ            --", TODAYtimeforREADING - TODAYtimeforREADING // 60 * 60, (2 - len(str(TODAYtimeforREADING - TODAYtimeforREADING // 60 * 60))) * " ", "-- минут --", TODAYtimeforREADING // 60, verifacation(TODAYtimeforREADING // 60), sep="")


def totalmake():
    print("1:", "Время потраченное на спорт             --", timeforSPORT - timeforSPORT // 60 * 60, (2 - len(str(timeforSPORT - timeforSPORT // 60 * 60))) * " ", "-- минут --", timeforSPORT // 60, verifacation(timeforSPORT // 60), sep="")
    print("2:", "Время потраченное на с++               --", timeforC - timeforC // 60 * 60, (2 - len(str(timeforC - timeforC // 60 * 60))) * " ", "-- минут --", timeforC // 60, verifacation(timeforC // 60), sep="")
    print("3:", "Время потраченное на питон             --", timeforPYTHON - timeforPYTHON // 60 * 60, (2 - len(str(timeforPYTHON - timeforPYTHON // 60 * 60))) * " ", "-- минут --", timeforPYTHON // 60, verifacation(timeforPYTHON // 60), sep="")
    print("4:", "Время потраченное на егэ по русскому   --", timeforEGER - timeforEGER // 60 * 60, (2 - len(str(timeforEGER - timeforEGER // 60 * 60))) * " ", "-- минут --", timeforEGER // 60, verifacation(timeforEGER // 60), sep="")
    print("5:", "Время потраченное на егэ по математике --", timeforEGEM - timeforEGEM // 60 * 60, (2 - len(str(timeforEGEM - timeforEGEM // 60 * 60))) * " ", "-- минут --", timeforEGEM // 60, verifacation(timeforEGEM // 60), sep="")
    print("6:", "Время потраченное на по информатике    --", timeforEGEI - timeforEGEI // 60 * 60, (2 - len(str(timeforEGEI - timeforEGEI // 60 * 60))) * " ", "-- минут --", timeforEGEI // 60, verifacation(timeforEGEI // 60), sep="")
    print("7:", "Время потраченное на уборку            --", timeforCLEANING - timeforCLEANING // 60 * 60, (2 - len(str(timeforCLEANING - timeforCLEANING // 60 * 60))) * " ", "-- минут --", timeforCLEANING // 60, verifacation(timeforCLEANING // 60), sep="")
    print("8:", "Время потраченное на ТОЙФЛ             --", timeforTOYFL - timeforTOYFL // 60 * 60, (2 - len(str(timeforTOYFL - timeforTOYFL // 60 * 60))) * " ", "-- минут --", timeforTOYFL // 60, verifacation(timeforTOYFL // 60), sep="")
    print("9:", "Время потраченное на ЧТЕНИЕ            --", timeforREADING - timeforREADING // 60 * 60, (2 - len(str(timeforREADING - timeforREADING // 60 * 60))) * " ", "-- минут --", timeforREADING // 60, verifacation(timeforREADING // 60), sep="")

#-------------------------------------------------------
file = open("input.txt", 'r')

spisokvaultyTODAY = []
spisokvaultyTOTAL = []
cnt = 0

for line in file:
    spisok = line.split()
    if spisok[0][0] != "#":
        cnt += 1
        if cnt <= 9:
            spisokvaultyTODAY.append(int(spisok[-1]))
        else:
            spisokvaultyTOTAL.append(int(spisok[-1]))

file.close()
#-------------------------------------------------------
for i in range(9):
    spisokvaultyTOTAL[i] += spisokvaultyTODAY[i]
#-------------------------------------------------------
file = open("input.txt", 'w')


#-------------------
timeforSPORT = 10
timeforC = 0
timeforPYTHON = 70
timeforEGER = 0
timeforEGEM = 0
timeforEGEI = 0
timeforCLEANING = 0
timeforTOYFL = 80
timeforREADING = 20
#-------------------

#TODAY THAT YOU MADE IN MINUTE
#-------------------
TODAYtimeforSPORT = 0
TODAYtimeforC = 0
TODAYtimeforPYTHON = 0
TODAYtimeforEGER = 0
TODAYtimeforEGEM = 0
TODAYtimeforEGEI = 0
TODAYtimeforCLEANING = 0
TODAYtimeforTOYFL = 0
TODAYtimeforREADING = 0
#-------------------

#TOTAL THAT YOU MADE
#-------------------
timeforSPORT += TODAYtimeforSPORT
timeforC += TODAYtimeforC
timeforPYTHON += TODAYtimeforPYTHON
timeforEGER += TODAYtimeforEGER
timeforEGEM += TODAYtimeforEGEM
timeforEGEI += TODAYtimeforEGEI
timeforCLEANING += TODAYtimeforCLEANING
timeforTOYFL += TODAYtimeforTOYFL
timeforREADING += TODAYtimeforREADING
#-------------------

print(spisokvaultyTOTAL)

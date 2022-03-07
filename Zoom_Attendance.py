import pyautogui as pag, keyboard, sys
import datetime, time
import re
import os


zoom_chat_window = 'C:/Users/USER/Desktop/02.python/mini/Py_Project/Zoom_Attendance/img/new_mess.PNG'
zoom_path = "C:/Users/USER/Documents/Zoom" # default zoom chat save path
img_path = "C:/Users/USER/Desktop/02.python/mini/Py_Project/Zoom_Attendance/img/"
chat_file = "meeting_saved_chat.txt" # default chat file name
str = time.strftime('%H%M%S') # 00시00분00초가 한줄로 연결된 현재 시간 문자열
commandDict = {'!사용법': '##### 7팀 미니챗봇 사용법 #####\n\
명령1) !사용법 - 챗봇을 사용하는 방법을 확인할 수 있습니다.\n\
명령2) !이용광 - ???\n\
명령3) !드라이브 - 강사님의 드라이브 주소를 확인할 수 있습니다.\n\
명령4) !쉬는시간 - 설정된 쉬는시간에 대한 정보를 받아옵니다.\n\
명령5) @쉬는시간 MM(분) - ex)@쉬는시간 20 \n\
현재시간에서 인자로 준 (분)시간 후로 쉬는시간알림을 설정합니다. 쉬는시간이끝날경우 알림을 확인할 수 있습니다.' , 
'!이용광' : '이요옹과앙 그는 신인가!', 
'!드라이브' : 'https://drive.google.com/drive/folders/1zVW-o0dBvgwth7ADu-SGbrCcD4NghqRt',
'!쉬는시간' : '00:00:00',
'!박태준' : '1995년 어느 산부인과에서 태어난 그는 주로 롤체에서 사기를 치는 것을 선호한다. 그는 3렙에 5코를 뽑는다.. 박태준 그는 신인가..'}
afterTime = datetime.datetime.strptime('23:59:59',"%H:%M:%S")


def break_time(break_time):
    # 현재 시간
    global commandDict
    global afterTime
    
    realTime = datetime.datetime.strptime(time.strftime('%H:%M:%S'),"%H:%M:%S")
    
    afterTime = realTime + datetime.timedelta(minutes=int(break_time))
    print('break_time call', afterTime.time(), "까지 놀아보자아아잇")
    commandDict['!쉬는시간'] = f'{afterTime.time()}'
            
def command_func(command):
    if command[0:5] == '@쉬는시간':
        n_list = command.split("@쉬는시간")
        
        if n_list[1] == '':
            location = pag.locateCenterOnScreen(zoom_chat_window)
            pag.click(location)
            keyboard.write('형식에 맞지 않습니다.')
            keyboard.press('enter')
                
        elif int(n_list[1]) > 40:
            location = pag.locateCenterOnScreen(zoom_chat_window)
            pag.click(location)
            keyboard.write('너무 많이 쉬네요! 저는 공부가 하고싶습니다! -태준')
            keyboard.press('enter')
            
        else:           
            break_time(n_list[1])
            
    elif command in commandDict.keys():
        location = pag.locateCenterOnScreen(zoom_chat_window)
        pag.click(location)
        keyboard.write(commandDict[command])
        keyboard.press('enter')

def checkTime(chatTime):
    
    # 00시00분00초가 한줄로 연결된 현재 시간 문자열
    realTime = datetime.datetime.strptime(time.strftime('%H:%M:%S'),"%H:%M:%S")
    inTime = datetime.datetime.strptime(chatTime,"%H:%M:%S")
    timeDiff = abs(realTime - inTime)
    
    if timeDiff.seconds > 10:
        return False
    
    else:
        return True

def search_zoom_path():
    filename = os.listdir(zoom_path)
    global chat_path
    chat_path = zoom_path +"/"+filename[len(filename) - 1] +"/"+chat_file
    
def get_png_location():
    global afterTime
    rer = datetime.datetime.strptime(time.strftime('%H:%M:%S'),"%H:%M:%S")
    
    if rer.time() >= afterTime.time():
        pag.click(pag.locateCenterOnScreen(zoom_chat_window))
        keyboard.write('쉬는시간이 끝났어요~~~ 집중합시다~~')
        keyboard.press('enter')
        commandDict['!쉬는시간'] = '23:59:59'

        # 대화 파일을 저장 하고 파일을 불러온다.
        location1 = pag.locateOnScreen(f'{img_path}save_img.PNG')
        
        if location1 == None:
            location_mac = pag.locateOnScreen(f'{img_path}save_img_mac.PNG')
            
            if location_mac == None:
                print('줌 화면 대화창을 찾지 못했습니다.')
            
            else:
                location = pag.locateOnScreen(f'{img_path}save_img_mac.PNG')
                
        else:
            location = pag.locateOnScreen(f'{img_path}save_img.PNG')
        pag.click(location)
        print('저장 전 버튼 클릭')
        time.sleep(2)
        location = pag.locateCenterOnScreen(f'{img_path}save_img_button.PNG')
        
        if location == None:
            location = pag.locateCenterOnScreen(f'{img_path}save_img_button_mac.PNG')
            
            if location == None:
                print('저장버튼을 찾지 못했습니다.')
            
        pag.click(location)
        print('저장버튼 클릭')
        search_zoom_path() # 채팅 저장파일 경로 변수에 저장하는 함수.
        inText = []
        with open (chat_path, 'r', encoding='utf-8') as f:
            allText = f.readlines()
            count = 0
            for i in allText[::-1]:       
                if count % 2 == 1 and checkTime(i.split(' ')[0]) == False:
                    del inText[len(inText)-1]
                    break
                
                elif count % 2 == 0:
                    clnText = re.sub('\t|\n|\s', '', i)
                    inText.append(clnText)
                count += 1
        for i in inText[::-1]:
            command_func(i)
            
if __name__ == '__main__':
    while(1):
        get_png_location()
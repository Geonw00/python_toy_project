import pyautogui as pag, keyboard, sys
import datetime, time
import os
zoom_chat_window = 'C:/Users/USER/Desktop/02.python/mini/Py_Project/Zoom_Attendance/new_mess.PNG'
zoom_path = "C:/Users/USER/Documents/Zoom" # default zoom chat save path
chat_file = "meeting_saved_chat" # default chat file name
str = time.strftime('%H%M%S')# 00시00분00초가 한줄로 연결된 현재 시간 문자열

def help_func():
    location = pag.locateCenterOnScreen(zoom_chat_window)
    pag.click(location)
    keyboard.write('##### 7팀 미니챗봇 사용법 #####\n\
        !사용법 - 챗봇을 사용하는 방법을 확인할 수 있습니다.\n\
        !이용광 - ???\n\
        !드라이브 - 강사님의 드라이브 주소를 확인할 수 있습니다.\n\
        !쉬는시간 - 설정된 쉬는시간에 대한 정보를 받아옵니다.\n\
        @쉬는시간 [HH:MM] - HH:MM 로 쉬는시간을 설정합니다. 쉬는시간이끝날경우 알림을 확인할 수 있습니다.')
    keyboard.press('enter')
    
def command_func(command):
    if command == "!사용법":
        help_func()
    elif command == "!이용광":
        print("용광 call")
        location = pag.locateCenterOnScreen(zoom_chat_window)
        pag.click(location)
        keyboard.write('이요옹과앙 그는 신인가!')
        keyboard.press('enter')
    elif command == "!드라이브":
        location = pag.locateCenterOnScreen(zoom_chat_window)
        pag.click(location)
        keyboard.write('https://drive.google.com/drive/folders/1zVW-o0dBvgwth7ADu-SGbrCcD4NghqRt')
        keyboard.press('enter')
    # elif command == "!쉬는시간":
        
    # else:
    #     print('else')

def checkTime(chatTime):
    # 00시00분00초가 한줄로 연결된 현재 시간 문자열
    realTime = datetime.datetime.strptime(time.strftime('%H:%M:%S'),"%H:%M:%S")
    inTime = datetime.datetime.strptime(chatTime,"%H:%M:%S")
    timeDiff = abs(realTime - inTime)
    if timeDiff > 10:
        return False
    else:
        return True

def search_zoom_path():
    filename = os.listdir(zoom_path)
    print("zoom path ls : ", filename)
    global chat_path
    chat_path = zoom_path +"/"+filename[len(filename) - 1] +"/"+chat_file
    print(chat_path)
    
def get_png_location():
    global count
    count = 1
    while 1:
        ###대화 파일을 저장 하고 파일을 불러온다.###
        pag.screenshot('C:/Users/USER/Desktop/02.python/mini/Py_Project/Zoom_Attendance/save_img2.PNG')
        location = pag.locateCenterOnScreen('C:/Users/USER/Desktop/02.python/mini/Py_Project/Zoom_Attendance/save_img.PNG')

        pag.click(location)
        print('저장 전 버튼 클릭')
        
        location = pag.locateCenterOnScreen('C:/Users/USER/Desktop/02.python/mini/Py_Project/Zoom_Attendance/save_img_button.PNG')
        pag.click(location)
        print('저장버튼 클릭')
        search_zoom_path() # 채팅 저장파일 경로 변수에 저장하는 함수.

        with open (chat_path, 'r', encoding='utf-8') as f:
            allText = f.readlines()
            inText = []
            count = 0
            for i in allText[::-1]:
         
                if count % 2 == 1 and checkTime(i.split(' ')[0]) == False:
                    inText.remove(len(inText))
                    break
        
                else:
                    inText.append(i)
                    
                count += 1

def click_and_answer(location, command):
    
    pag.click(location)
    time.sleep(1)

    keyboard.write('네')
    keyboard.press('enter')

    print(f"Script Success!\n총 시도 횟수: {count}")

if __name__ == '__main__':
    command_func('!이용광')
    #search_zoom_path()
    #get_png_location()
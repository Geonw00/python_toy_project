import pyautogui as pag, keyboard, sys
import datetime, time
import re
import os
import random

zoom_chat_window = 'C:/Users/USER/Desktop/02.python/mini/Py_Project/Zoom_Attendance/img/new_mess.PNG'
zoom_path = "C:/Users/USER/Documents/Zoom" # default zoom chat save path
img_path = "C:/Users/USER/Desktop/02.python/mini/Py_Project/Zoom_Attendance/img/"
chat_file = "meeting_saved_chat.txt" # default chat file name
str = time.strftime('%H%M%S') # 00시00분00초가 한줄로 연결된 현재 시간 문자열
hilist=['반가워요~!!','좋은 하루 입니다!', '안녕하세요 ?']
eduDict= {'08' : '[RPA]미니프로젝트 발표!','10' : '[Python]Web Scraping', '11' : '[Python]Web Scraping', '14' : '[Python]Numpy / Pandas', '15' : '[Python]Numpy / Pandas', '16':'[Python]확률과 확률분포','17':'[Python]회귀분석','18':'[머신러닝]머신러닝 개요',\
'21':'[머신러닝]데이터 전처리, 데이터셋 나누기','22':'[머신러닝]분류 알고리즘','23':'[머신러닝]분류 알고리즘','24':'[머신러닝]경사하강법과 최적화','25':'[머신러닝]회귀 알고리즘','28':'[머신러닝]비지도학습','29':'[딥러닝]딥러닝 개요','30':'[딥러닝]MLP','31':'[딥러닝]과적합 방지를 위한 Dropout, BatchNormalization 등 기법',\
'01':'[딥러닝]CNN','02':'[딥러닝]Transfer Learning 개요','04':'[딥러닝]Tensorflow 모델구현의 다양한 방법 – functional, subclass방식','05':'[딥러닝]RNN'}
commandDict = {'!사용법': '##### 7팀 미니챗봇 사용법 #####\n\
명령1) !사용법 - 챗봇을 사용하는 방법을 확인할 수 있습니다.\n\
명령2) !드라이브 - 강사님의 드라이브 주소를 확인할 수 있습니다.\n\
명령3) !쉬는시간 - 설정된 쉬는시간에 대한 정보를 받아옵니다.\n\
명령4) !안녕 - 챗봇에게 인사해보세요.\n\
명령5) !수업내용 - 오늘의 수업 정보를 받아옵니다.\n\
명령6) @쉬는시간 MM(분) - ex)@쉬는시간 20 \n\
현재시간에서 인자로 준 (분)시간 후로 쉬는시간알림을 설정합니다. 쉬는시간이끝날경우 알림을 확인할 수 있습니다.' , 
'!이용광' : '이용광 그는 신인가?!', 
'!드라이브' : 'https://drive.google.com/drive/folders/1zVW-o0dBvgwth7ADu-SGbrCcD4NghqRt',
'!쉬는시간' : '00:00:00',
'!박태준' : '박태준! 박태준! 박태준! 박태준! 박태준! 박태준!',
'!안녕' : 'default value',
'!수업내용' : 'default value'}
afterTime = datetime.datetime.strptime('23:59:59',"%H:%M:%S")
strtest = """
＼＿＿＿＿＿＿＿＿＿＿／
　　ｏ
　　 。
　　　｡
　　∧＿∧
　 (*　･ω･)
＿(__つ/￣￣￣/_
　　＼/　　　/

"""

def break_time(break_time):
    # 현재 시간
    global commandDict
    global afterTime
    
    realTime = datetime.datetime.strptime(time.strftime('%H:%M:%S'),"%H:%M:%S")
    
    afterTime = realTime + datetime.timedelta(minutes=int(break_time))
    print('break_time call', afterTime.time(), "까지 놀아보자아아잇")
    pag.click(pag.locateCenterOnScreen(zoom_chat_window))
    keyboard.write(f"""{afterTime.time()}까지 놀아보자아아~!!\n{strtest}""")
    keyboard.press('enter')
    commandDict['!쉬는시간'] = f'{afterTime.time()}'
            
def command_func(command):
    if command[0:5] == '@쉬는시간':
        n_list = command.split("@쉬는시간")
        
        if n_list[1] == '':
            location = pag.locateCenterOnScreen(zoom_chat_window)
            pag.click(location)
            keyboard.write('형식에 맞지 않습니다.')
            keyboard.press('enter')
                
        elif int(n_list[1]) > 120:
            location = pag.locateCenterOnScreen(zoom_chat_window)
            pag.click(location)
            keyboard.write('2시간 이상 쉬는시간을 설정할 수 없습니다.')
            keyboard.press('enter')
            
        else:           
            break_time(n_list[1])
            
    elif command in commandDict.keys():
        if command == '!안녕':
            commandDict[command] = random.choice(hilist)
        location = pag.locateCenterOnScreen(zoom_chat_window)
        pag.click(location)
        keyboard.write(commandDict[command])
        keyboard.press('enter')


def checkTime(chatTime):
    
    # 00시00분00초가 한줄로 연결된 현재 시간 문자열
    realTime = datetime.datetime.strptime(time.strftime('%H:%M:%S'),"%H:%M:%S")
    inTime = datetime.datetime.strptime(chatTime,"%H:%M:%S")
    timeDiff = abs(realTime - inTime)
    
    # 현재시간과 15초 이상 차이날 경우 False 반환
    if timeDiff.seconds > 15:
        return False
    
    else:
        return True

def search_zoom_path():
    filename = os.listdir(zoom_path)
    global chat_path
    chat_path = zoom_path +"/"+filename[len(filename) - 1] +"/"+chat_file
    
def get_png_location():
    print('Start')
    global afterTime
    rer = datetime.datetime.strptime(time.strftime('%H:%M:%S'),"%H:%M:%S")
    
    if rer.time() >= afterTime.time():
        pag.click(pag.locateCenterOnScreen(zoom_chat_window))
        keyboard.write('''쉬는시간이 끝났습니다!!.\n\
            ┏━━━━━━━┓
            ┃	      ┃
            ┃　┏━┓      ┃
            ┗━┛　┃      ┃
            　　┏━┛    ┃
            　　┃   ┏━┛
            　　┗━┛
            　　┏━┓
            　　┃  ┃
            　　┗━┛
            　　　〇
            　　　ｏ 벌써?
            　　　　(・д・)
            ''')
        keyboard.press('enter')
        commandDict['!쉬는시간'] = '23:59:59'
        afterTime = datetime.datetime.strptime('23:59:59',"%H:%M:%S")

    # 대화 파일을 저장 하고 파일을 불러온다.
    location1 = pag.locateOnScreen(f'{img_path}save_img.PNG')
    
    if location1 == None:
        print('줌 화면 대화창을 찾지 못했습니다.')
        return
            
    else:
        location = pag.locateOnScreen(f'{img_path}save_img.PNG')
    pag.click(location)
    print('저장 전 버튼 클릭')
    location = pag.locateCenterOnScreen(f'{img_path}save_img_button.PNG')
    
    if location == None:
        print('저장버튼을 찾지 못했습니다.')
        return
        
    pag.click(location)
    print('저장버튼 클릭')
    search_zoom_path() # 채팅 저장파일 경로 변수에 저장하는 함수.
    inText = []
    with open (chat_path, 'r', encoding='utf-8') as f:
        allText = f.readlines() 
        # 10:12:40 발신자 XXX 수신자 모두에게:
        # 채팅내용
        # 위와 같은 형식 반복
        for i in allText[::-1]:       
            if re.match('\d{2}:\d{2}:\d{2}\s발신자\s\w+\s\w+\s\w+:', i) != None and checkTime(i.split(' ')[0]) == False:
                if len(inText) != 0:
                    del inText[len(inText)-1]
                break

            elif re.match('\d{2}:\d{2}:\d{2}\s발신자\s\w+\s\w+\s\w+:', i) == None:
                clnText = re.sub('\t|\n|\s', '', i) # '\t채팅내용\n' => '채팅내용'
                if clnText.startswith('@') or clnText.startswith('!'):
                    inText.append(clnText)
    
    if len(inText) > 10:
        pag.click(pag.locateCenterOnScreen(zoom_chat_window))
        keyboard.write('명령이 너무 많습니다. 😮‍💨')
        keyboard.press('enter')
    else:    
        for i in inText[::-1]:
            command_func(i)
            
if __name__ == '__main__':
    nowDate = time.strftime('%d')
    commandDict['!수업내용'] = eduDict[nowDate]
    while(1):
        get_png_location()
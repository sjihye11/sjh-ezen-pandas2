# 두 번째 파일입니다. 파일명 보면 숫자 6이라고 되어있는데, 에러가 6개라는 뜻이야.
import os
import pandas as pd
# 이제 에러 사라짐.


def list_load(_path, _end): 
    # 매개변수 설정
    # _path : 파일의 경로
    # _end : 파일의 확장자
    
    # _path의 마지막 문자열이 '/'가 아니라면?
    # if not(_path.endswith('/')): 이렇게 해도 되고
    if _path[-1] !='/':
        _path = _path + '/'
        #근데 if not(_path.endswith('/')):라고 안 써도 됨. 파일 경로에서는 //도 잘 인식함.
    
    # 특정 경로의 파일 리스트 생성
    file_list = os.listdir(_path)
    
    # 특정 확장자로 이루어진 파일 리스트 생성
    file_list2 = []
    
    for file in file_list:
        if file.endswith(_end):
            file_list2.append(file)
        
    # 비어있는 데이터프레임 생성
    result = pd.DataFrame()
    
    # 반복문 생성
    for file in file_list2:
        # _end가 'csv'인 경우
        if _end == 'csv':
            df = pd.read_csv(_path + file)
        elif _end == 'json':
            df = pd.read_json(_path + file)
        # elif (_end == 'xls') | (_end == 'xlsx'):   #|는 or라는 뜻
        elif _end in ['xls', 'xlsx']:
            df = pd.read_excel(_path+file)
        else:
            return "지원하지 않는 확장자입니다."
    
        #유니언 결합
        result = pd.concat([result, df], axis = 0, ignore_index = True) 
        
    return result
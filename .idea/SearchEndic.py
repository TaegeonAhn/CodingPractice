import os

file_path_list =[]

def FileSearch(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                Search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.dic':
                    full_filename = full_filename.replace("\\", "/")
                    file_path_list.append(full_filename)
    except PermissionError:
        pass

FileSearch('D:/00.MIGRATION/02.Dictionary/engdic')

eng_dic = {}

for file_path in file_path_list:

    with open(file_path, 'r') as file:
        read_line = file.readlines()

    for r_line in read_line:

        dic_line = r_line.split(':')

        if len(dic_line) < 2:
            continue

        dic_key = dic_line[0].strip() # 키 값 공백 제거
        dic_value = dic_line[1]

        if dic_key in eng_dic:
            continue

        else:
            eng_dic[dic_key] = dic_value

input_data = input("검색할 영어 단어를 입력해주세요. : ") #.lower 소문자 변경
diff_number = int(input("다른 글자 몇 개까지 허용할까요? 숫자로만 입력해주세요. : ")) #사용자의 입력 값을 인트로 제한함.

search_result_list = []

for eng_key in eng_dic:

    length_diff = len(eng_key) - len(input_data)

    if abs(length_diff) > diff_number: #차이 나는 숫자보다 크거나 작으면 바로 continue
        continue

    if length_diff > 0: #차이나는 숫자만큼만 길이가 다른 key 값만 비교

        not_match_count = diff_number #이미 길이가 차이나므로 diff_number 설정
        for match_count in range(len(input_data)):

            if input_data[match_count] == eng_key[match_count]: #모든 글자 비교 <대소문자 구분 함>
                pass

            else:
                not_match_count += 1

    elif length_diff == 0:

        not_match_count = 0 #길이 차이가 안나므로 0 시작
        for match_count in range(len(input_data)):

            if input_data[match_count] == eng_key[match_count]:
                pass

            else:
                not_match_count += 1

    elif length_diff < 0:

        not_match_count = diff_number
        for match_count in range(len(eng_key)):

            if input_data[match_count] == eng_key[match_count]:
                pass

            else:
                not_match_count += 1

    if not_match_count == diff_number:
        search_result_list.append(eng_key)

if len(search_result_list) < 1:
    print("검색된 결과가 없습니다.")

else:
    for search_data in search_result_list:
        print(f'{search_data} : {eng_dic[search_data]}')






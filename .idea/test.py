
file_reader = open('D:/00.MIGRATION/01.JsonEditTest/uuid_test.csv', 'r', encoding='utf-8')
csv_reader =  csv.reader(file_reader)

json_path = 'D:/01.JsonEditTest/test.json'

with open(json_path,'r',encoding='utf-8') as json_file:
    read_lines = json_file.readlines()

result_json = []
for r_line in read_lines:

    r_line = r_line.replace('이름', 'Name')
    result_json.append(r_line)

with open('D:/00.MIGRATION/01.JsonEditTest/test.json','w',encoding='utf-8') as json_write:

    for w_line in result_json:
        json_write.write(w_line)



for r_line in read_lines:

    for key, value in uuid_dic.items():
        if key is None:
            continue

        r_line = r_line.replace(key, value)


    result_lines.append(r_line)

with open('D:/00.MIGRATION/01.JsonEditTest/test.json','w',encoding='utf-8') as json_write:

    for w_line in result_lines:
        json_write.write(w_line)

{
     "이름": "테스트",
     "나이": 32,
     "성별": "남",
     "주소": "서울특별시 마포구 대현동",
     "특기": ["축구", "도술"],
 }
{
     "이름": "테스트",
     "나이": 29,
     "성별": "여",
     "주소": "서울특별시 마포구 대현동",
     "특기": ["독서", "도술"],
 }


test_dic={}

i = 0
for line in csv_reader:

    for index in range(2,len(line),2):

        if index < len(line) -2:

            if line[index] in uuid_dic:
                continue

            if len(line[index]) <30:
                continue

            else:
                test_dic[line[index]] = line[index+1]

    i += 2
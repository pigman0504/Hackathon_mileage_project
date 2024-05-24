import csv

# 학생 데이터를 파일에서 읽어오는 함수
def load_data(file_name):
    data = []
    try:
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"{file_name} not found. Starting with an empty dataset.")
        # 초기 데이터 추가
        data = [
    ["9-1", "9101", "강*율", "0"],
    ["9-1", "9102", "강*윤", "0"],
    ["9-1", "9103", "강*인", "0"],
    ["9-1", "9104", "고*우", "0"],
    ["9-1", "9105", "곽*기", "0"],
    ["9-1", "9106", "구*정", "0"],
    ["9-1", "9107", "김*라", "0"],
    ["9-1", "9108", "김*", "0"],
    ["9-1", "9109", "김*민", "0"],
    ["9-1", "9110", "김*성", "0"],
    ["9-1", "9111", "김*서", "0"],
    ["9-1", "9112", "박*빈", "0"],
    ["9-1", "9113", "박*온", "0"],
    ["9-1", "9114", "박*수", "0"],
    ["9-1", "9115", "박*연", "0"],
    ["9-1", "9116", "백*린", "0"],
    ["9-1", "9117", "서*서", "0"],
    ["9-1", "9118", "선*아", "0"],
    ["9-1", "9119", "신*희", "0"],
    ["9-1", "9120", "유*인", "0"],
    ["9-1", "9121", "윤*현", "0"],
    ["9-1", "9122", "이*빈", "0"],
    ["9-1", "9123", "이*율", "0"],
    ["9-1", "9124", "이*민", "0"],
    ["9-1", "9125", "이*유", "0"],
    ["9-1", "9126", "이*리", "0"],
    ["9-1", "9127", "정*진", "0"],
    ["9-1", "9128", "정*민", "0"],
    ["9-1", "9129", "진*우", "0"],
    ["9-1", "9130", "최*원", "0"],
    ["9-1", "9131", "홍*", "0"],
    ["9-1", "9132", "황*연", "0"],
    ["9-1", "9133", "황*서", "0"],
    ["9-2", "9201", "강*재", "0"],
    ["9-2", "9202", "강*석", "0"],
    ["9-2", "9203", "강*후", "0"],
    ["9-2", "9204", "강*나", "0"],
    ["9-2", "9205", "고*우", "0"],
    ["9-2", "9206", "구*명", "0"],
    ["9-2", "9207", "김*준", "0"],
    ["9-2", "9208", "김*화", "0"],
    ["9-2", "9209", "김*진", "0"],
    ["9-2", "9210", "김*영", "0"],
    ["9-2", "9211", "김*은", "0"],
    ["9-2", "9212", "김*서", "0"],
    ["9-2", "9213", "김*린", "0"],
    ["9-2", "9214", "김*원", "0"],
    ["9-2", "9215", "문*민", "0"],
    ["9-2", "9216", "민*홍", "0"],
    ["9-2", "9217", "박*상", "0"],
    ["9-2", "9218", "손*민", "0"],
    ["9-2", "9219", "손*준", "0"],
    ["9-2", "9220", "오*령", "0"],
    ["9-2", "9221", "이*규", "0"],
    ["9-2", "9222", "이*진", "0"],
    ["9-2", "9223", "이*경", "0"],
    ["9-2", "9224", "이*서", "0"],
    ["9-2", "9225", "정*우", "0"],
    ["9-2", "9226", "조*영", "0"],
    ["9-2", "9227", "최*명", "0"],
    ["9-2", "9228", "최*석", "0"],
    ["9-2", "9229", "한*라", "0"],
    ["9-2", "9230", "한*서", "0"],
    ["9-2", "9231", "한*진", "0"],
    ["9-2", "9232", "홍*민", "0"],
    ["9-2", "9233", "황*하", "0"],
    ["9-3", "9301", "구*훈", "0"],
    ["9-3", "9302", "김*리", "0"],
    ["9-3", "9303", "김*준", "0"],
    ["9-3", "9304", "김*채", "0"],
    ["9-3", "9305", "김*현", "0"],
    ["9-3", "9306", "김*인", "0"],
    ["9-3", "9307", "김*현", "0"],
    ["9-3", "9308", "김*우", "0"],
    ["9-3", "9309", "김*윤", "0"],
    ["9-3", "9310", "박*민", "0"],
    ["9-3", "9311", "박*현", "0"],
    ["9-3", "9312", "박*현", "0"],
    ["9-3", "9313", "박*우", "0"],
    ["9-3", "9314", "박*진", "0"],
    ["9-3", "9315", "박*수", "0"],
    ["9-3", "9316", "백*라", "0"],
    ["9-3", "9317", "신*진", "0"],
    ["9-3", "9318", "안*중", "0"],
    ["9-3", "9319", "오*욱", "0"],
    ["9-3", "9320", "오*원", "0"],
    ["9-3", "9321", "유*", "0"],
    ["9-3", "9322", "윤*아", "0"],
    ["9-3", "9323", "윤*언", "0"],
    ["9-3", "9324", "이*원", "0"],
    ["9-3", "9325", "이*서", "0"],
    ["9-3", "9326", "이*진", "0"],
    ["9-3", "9327", "이*주", "0"],
    ["9-3", "9328", "장*기", "0"],
    ["9-3", "9329", "정*진", "0"],
    ["9-3", "9330", "정*우", "0"],
    ["9-3", "9331", "조*철", "0"],
    ["9-3", "9332", "차*빈", "0"],
    ["9-3", "9333", "천*현", "0"],
    ["9-4", "9401", "강*영", "0"],
    ["9-4", "9402", "강*서", "0"],
    ["9-4", "9403", "권*철", "0"],
    ["9-4", "9404", "김*우", "0"],
    ["9-4", "9405", "김*하", "0"],
    ["9-4", "9406", "김*경", "0"],
    ["9-4", "9407", "김*린", "0"],
    ["9-4", "9408", "김*석", "0"],
    ["9-4", "9409", "김*후", "0"],
    ["9-4", "9410", "김*준", "0"],
    ["9-4", "9411", "라*명", "0"],
    ["9-4", "9412", "류*훈", "0"],
    ["9-4", "9413", "민*영", "0"],
    ["9-4", "9414", "박*준", "0"],
    ["9-4", "9415", "박*온", "0"],
    ["9-4", "9416", "박*담", "0"],
    ["9-4", "9417", "배*서", "0"],
    ["9-4", "9418", "변*린", "0"],
    ["9-4", "9419", "손*연", "0"],
    ["9-4", "9420", "송*희", "0"],
    ["9-4", "9421", "이*나", "0"],
    ["9-4", "9422", "이*주", "0"],
    ["9-4", "9423", "임*온", "0"],
    ["9-4", "9424", "임*민", "0"],
    ["9-4", "9425", "장*인", "0"],
    ["9-4", "9426", "정*진", "0"],
    ["9-4", "9427", "조*림", "0"],
    ["9-4", "9428", "최*우", "0"],
    ["9-4", "9429", "추*미", "0"],
    ["9-4", "9430", "하*린", "0"],
    ["9-4", "9431", "현*연", "0"],
    ["9-4", "9432", "홍*민", "0"],
    ["9-4", "9433", "황*환", "0"],
    ["9-5", "9501", "강*재", "0"],
    ["9-5", "9502", "곽*하", "0"],
    ["9-5", "9503", "김*진", "0"],
    ["9-5", "9504", "김*민", "0"],
    ["9-5", "9505", "김*성", "0"],
    ["9-5", "9506", "김*승", "0"],
    ["9-5", "9507", "김*원", "0"],
    ["9-5", "9508", "김*우", "0"],
    ["9-5", "9509", "나*빈", "0"],
    ["9-5", "9510", "도*림", "0"],
    ["9-5", "9511", "문*민", "0"],
    ["9-5", "9512", "문*찬", "0"],
    ["9-5", "9513", "박*준", "0"],
    ["9-5", "9514", "박*윤", "0"],
    ["9-5", "9515", "반*영", "0"],
    ["9-5", "9516", "배*주", "0"],
    ["9-5", "9517", "심*진", "0"],
    ["9-5", "9518", "안*연", "0"],
    ["9-5", "9519", "양*민", "0"],
    ["9-5", "9520", "오*호", "0"],
    ["9-5", "9521", "오*헌", "0"],
    ["9-5", "9522", "오*영", "0"],
    ["9-5", "9523", "유*수", "0"],
    ["9-5", "9524", "이*은", "0"],
    ["9-5", "9525", "이*남", "0"],
    ["9-5", "9526", "장*수", "0"],
    ["9-5", "9527", "장*나", "0"],
    ["9-5", "9528", "전*준", "0"],
    ["9-5", "9529", "전*현", "0"],
    ["9-5", "9530", "채*은", "0"],
    ["9-5", "9531", "최*우", "0"],
    ["9-5", "9532", "홍*나", "0"],
    ["9-5", "9533", "황*준", "0"]
]
    return data

# 학생 데이터를 파일에 저장하는 함수
def save_data(file_name, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

# 학생 데이터 파일 이름
file_name = 'stu_data.csv'

# 프로그램 시작 시 데이터 로드
stu_data = load_data(file_name)

def is_integer(number):
    try:
        number = int(number)
        return True
    except ValueError:
        return False





def get_stu_price(category):
    stu_num_list = []
    count = 0
    print("[", category, "]")
    for i in range(len(stu_data)):
        if stu_data[i][0] == category:
            count += 1
            stu_num_list.append(stu_data[i][1])
            print(count, stu_data[i][1], stu_data[i][2], stu_data[i][3])
    number = input("Number : ")
    while not is_integer(number) or int(number) < 1 or int(number) > count:
        count = 0
        print("Type Error !!")
        print()
        for j in range(len(stu_data)):
            if stu_data[j][0] == category:
                count += 1
                print(count, stu_data[j][1], stu_data[j][2], stu_data[j][3])
        number = input("Number : ")
    return stu_num_list[int(number) - 1]






def order():
    mileage_list = []
    print("1 : 9-1반")
    print("2 : 9-2반")
    print("3 : 9-3반")
    print("4 : 9-4반")
    print("5 : 9-5반")
    print("9 : 적립 취소")
    mileage = input("Number : ")
    print()

    if mileage == '1':
        reicve_price = get_stu_price("9-1")
        mileage_list = reicve_price
    elif mileage == '2':
        reicve_price = get_stu_price("9-2")
        mileage_list = reicve_price
    elif mileage == '3':
        reicve_price = get_stu_price("9-3")
        mileage_list = reicve_price
    elif mileage == '4':
        reicve_price = get_stu_price("9-4")
        mileage_list = reicve_price
    elif mileage == '5':
        reicve_price = get_stu_price("9-5")
        mileage_list = reicve_price
    elif mileage == '9':
        print("적립 취소 실행")
        mileage_list = -1
    else:
        print("Type Error !!")
    print()
    
    return mileage_list






def cal_order(recive_order):
    sum = 0
    if recive_order != -1:
        if recive_order != []:
            for i in range(len(stu_data)):
                if stu_data[i][1] == recive_order:
                    print(stu_data[i][1], stu_data[i][2], "님의 현재 마일리지 :", stu_data[i][3])
                    point = int(input("적립 마일리지 : "))
                    sum = point + int(stu_data[i][3])
                    stu_data[i][3] = str(sum)
            return str(sum)
    else:
        return sum







def add_mileage():
    number = " "
    while number != '2':
        print("1 : 마일리지 추가")
        print("2 : 프로그램 종료")
        number = input("Number : ")
        print()
        if number == '1':
            recive_order = order()
            recive_cal = cal_order(recive_order)
            if recive_cal != 0:
                print("적립된 마일리지 :", recive_cal)
                print()
        elif number == '2':
            print("Program End !!") 
            save_data(file_name, stu_data)
        else:
            print("Type Error !!")
            print()






def school_rank():
    int_box = stu_data[0][3]
    str_box = stu_data[0]
    for i in range(1,len(stu_data)):
        if int(int_box) < int(stu_data[i][3]):
            int_box = stu_data[i][3]
            str_box = stu_data[i]
    print("전체 1등 :",str_box)
     
    
        





def get_first_data(category):
    str_box = ""
    int_box = ""
    amount_list = []
    count = 0
    for i in range(0,len(stu_data)):
        if category == stu_data[i][0]:
            amount_list.append(stu_data[i])
            count = count + 1

    int_box = amount_list[0][3]
    str_box = amount_list[0]
    for j in range(1,count):
        if int_box < amount_list[j][3]:
            int_box = amount_list[j][3]
            str_box = amount_list[j]
        
    return str_box


    




def class_rank():
    recive = get_first_data("9-1")
    print("9-1반 1등",recive)
    print()
    recive = get_first_data("9-2")
    print("9-2반 1등",recive)
    print()
    recive = get_first_data("9-3")
    print("9-3반 1등",recive)
    print()
    recive = get_first_data("9-4")
    print("9-4반 1등",recive)
    print()
    recive = get_first_data("9-5")
    print("9-5반 1등",recive)







    


number = " "
while number != '9':
    print("1 : 마일리지 적립")
    print("2 : 마일리지 랭킹보드")
    print('9 : 종료')
    number = input("Number : ")
    print()
    if number == '1':
        add_mileage()
        print()

    elif number == '2':
        school_rank()
        print()
        class_rank()
        print()

    elif number == '9':
        print("Program End !!")

    else:
        print("Type Error !!")


def Nhap_tu(s):
    while True:
        try:
            tu = input('Nhập %s'%s)
            if all(item==' ' or item.isalpha() for item in tu):
                return tu
            else:
                print('Đây không phải là từ.Yêu cầu nhập lại')
        except Exception as err:
            print(err)

def Nhapso():
    while True:
        try:
            n = eval(input('Chọn chức năng cần thực hiện(0-4): '))
        except Exception as err:
            print(err)
        else:
            if (type(n) is not int) or (not 0<=n<=4):
                print('Đây không phải là số nguyên dương 0-4.Yêu cầu nhập lại')
            else:
                return n

# dictionary = {key:value}
def them_tu(dic):
    print('\t1.- Thêm từ')
    word = Nhap_tu('từ mới: ')
    mean = Nhap_tu('nghĩa: ')
    dic[word] = mean
    print('Từ mới đã được thêm: [%s : %s]'%(word,dic[word]))

def Tim_tu(dic):
    print('\t2.- Tìm từ')
    word = Nhap_tu('từ cần tìm: ')
    if word in dic:
        print('Tìm thấy: [%s : %s]'%(word,dic[word]))
    else:
        print('Không tìm thấy từ %s trong từ điển'%word)

def xoa_tu(dic):
    print('\t3.- Xóa từ:')
    word = Nhap_tu('từ cần xóa:')
    if word in dic:
        print('Từ cần xóa: [{0} : {1}]'.format(word,dic[word]))
        dic.pop(word)
    else:
        print('không tìm thấy từ %s cần xóa'%word)

def xem_tat_ca(dic):
    print('\t4.- Xem tất cả')
    if len(dic) == 0:
        print('Hiện tại từ điển của bạn không có từ nào.Bạn cần nhập thêm từ mới')
    else:
        print('Từ điển của bạn:',end=' ')
        for w,m in dic.items():
            print('[%s : %s]'%(w,dic[w]),end=' ')
        print()

def menu():
    print('-'*40)
    print('CHƯƠNG TRÌNH TẠO TỪ ĐIỂN'.center(40,'*'))
    print('-'*40)
    print('\t1.- Thêm từ')
    print('\t2.- Tìm từ')
    print('\t3.- Xóa từ')
    print('\t4.- Xem tất cả')
    print('\t0.- Nhấn 0 để kết thúc chương trình')

def main():
    dic = {}
    while True:
        choice = Nhapso()
        if choice==0:
            print('Chương trình tạo từ điển kết thúc')
            break
        elif choice==1:
            them_tu(dic)
        elif choice==2:
            Tim_tu(dic)
        elif choice==3:
            xoa_tu(dic)
        elif choice==4:
            xem_tat_ca(dic)

#---------------------Main-----------------------------
menu()
main()



import os
import time
import hashlib

class Kiosk_reservation_Package:
    def __init__(self):
        self.user_info = []
        self.load_saved_data()  # 클래스가 초기화될 때 저장된 데이터를 로드합니다.

    def load_saved_data(self):
        try:
            with open("reservation.txt", "r", encoding="utf8") as reservation_load_file:
                lines = reservation_load_file.readlines()
                if len(lines) % 2 != 0:
                    return

                for i in range(0, len(lines), 2):
                    if i + 1 < len(lines):
                        name_line = lines[i].strip().split(': ')
                        phone_line = lines[i+1].strip().split(': ')
                        if len(name_line) == 2 and len(phone_line) == 2:
                            name = name_line[1]
                            phone = phone_line[1]
                            user_info = {"name": name, "phoneNumber": phone}
                            self.user_info.append(user_info)
                        else:
                            pass
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")

    def save_data_to_file(self):
        with open("reservation.txt", "w", encoding="utf8") as reservation_save_file:
            for user_info in self.user_info:
                reservation_save_file.write(f"이름: {user_info['name']}\n휴대폰 번호: {user_info['phoneNumber']}\n")


    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    def hash_phoneNumber(self, phoneNumber):
        #SHA-256암호화 적용
        hash_phoneNumber = hashlib.sha256(phoneNumber.encode()).hexdigest()
        return hash_phoneNumber
    
    def reservation_save_file(self, user_info):
        header = "이름\t전화번호\n"
        with open("reservation.txt", "a", encoding="utf8") as reservation_save_file:
            if not os.path.exists("reservation.txt"):
                reservation_save_file.write(header)
            print(f"예약자 이름: {user_info['name']}\n예약자 휴대폰번호: {user_info['phoneNumber']}\n", 
                  file=reservation_save_file)

    def reservation_load_file(self):
        print("\n파일을 불러옵니다.")
        self.load_saved_data()  # load_saved_data를 호출하여 user_info 리스트를 업데이트합니다.
        try:
            if not self.user_info:
                print("예약한 정보가 없습니다.")
            else:
                print("\n[안내] 예약자가 예약한 정보입니다.\n")
                for idx, user_info in enumerate(self.user_info, start=1):
                    print(f"예약 번호: {idx}\n이름: {user_info['name']}\n전화번호: {user_info['phoneNumber']}\n")
                    
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")

    # def reservation_load_file(self):
    #     print("\n파일을 불러옵니다.")
    #     try:
    #         with open("reservation.txt", "r", encoding="utf8") as reservation_load_file:
    #             for line in reservation_load_file:
    #                 print(line, end="")
                    
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")

    def reservation(self):
        print("\n[안내] 키오스크 예약 화면입니다.\n")
        print("[1. 숙소 예약]\n[2. 뒤로가기]")
        r_user_input = input("입력:")

        if r_user_input == "1":
            print("\n[안내] 숙소를 예약하겠습니다.\n")
            while True:
                name = input("\n[안내] 예약할 예약자님의 이름을 입력해주세요.\n입력: ")
                phoneNumber = input("\n[안내] 예약자님의 전화번호를 입력해주세요.\n입력: ")
                self.clear_screen()

                print("\n[안내] 입력하신 정보를 확인해주세요.\n")
                print(f"이름: {name}\n전화번호: {phoneNumber}\n")
                info = input("[안내] 입력하신 정보가 맞으면 Y를, 다르면 N을 입력해주세요:")
                
                if info == "Y" or info == "y":
                    print("예약이 완료되었습니다. 메인화면으로 이동합니다.")
                    user_info = {"name": name, "phoneNumber": phoneNumber}
                    self.user_info.append(user_info)
                    self.reservation_save_file(user_info)
                    time.sleep(3)
                    break
                elif info == "N" or info == "n":
                    print("예약을 다시 시도합니다. 잠시만 기다려주십시오.")
                    time.sleep(3)
                    self.clear_screen()
                else:
                    print("잘못 입력하였습니다. 처음부터 다시 입력해주세요.")
            return name, phoneNumber
            
        elif r_user_input == "2":
            print("\n뒤로가기\n")

        else:
            print("else")
    
    def display_user_info(self):
        if not self.user_info:
            print("예약한 정보가 없습니다.")
        else:
            print("\n[안내] 예약자가 예약한 정보입니다.\n")
            for idx, user_info in enumerate(self.user_info, start=1):
                print(f"예약 번호: {idx}\n이름: {user_info['name']}\n전화번호: {user_info['phoneNumber']}\n")

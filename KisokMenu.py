#키오스크 만들어보기
import time
import getpass
from Kiosk_File.kiosk_reservation import *
from Kiosk_File.kiosk_reservation_check import *

reser = Kiosk_reservation_Package()
reser_check = Kisok_reservation_ckeck_Package(reser)

class Kiosk:    
    def __init__(self):
        self.admin_password = "admin"
        self.admin_authenticateed = False

    def process_user_input(self, user_input):
        if user_input == "1": #예약
            print("\n[안내] 예약 화면으로 이동합니다. 잠시만 기다려 주십시오.\n")
            time.sleep(0.5)
            reser.clear_screen() #cmd 화면 지우기
            reser.reservation() #예약 화면 메뉴
            reser.clear_screen()

        elif user_input == "2": #예약 확인
            print("\n[안내] 예약 확인 화면으로 이동합니다. 잠시만 기다려 주십시오.\n")
            time.sleep(2)
            reser.clear_screen()
            reser_check.user_check()  # 인스턴스를 통한 접근
        
        elif user_input == "3": #예약자 명단
            reser.clear_screen()
            if self.admin_authenticateed or self.authenticate_admin():
                reser.display_user_info()
            else:
                print("\n[안내] 비밀번호를 틀렸습니다. 접속할 수 없습니다.")
                print("메뉴로 돌아갑니다.")
                time.sleep(2)
                reser.clear_screen()
        
        elif user_input == "4": #종료
            print("\n[안내] 프로그램을 종료합니다.\n")
            

        elif user_input == "5":
            reser.load_saved_data()

        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

    def authenticate_admin(self):
        print("[안내] 관리자 암호가 필요합니다. 암호를 입력해주세요.")
        admin_password_input = getpass.getpass("입력: ")
        if admin_password_input == self.admin_password:
            self.admin_authenticate = True
            return True
        else:
            return False
        
while True:
    print("\n키오스크 테스트\n")
    print("[1. 예약]\n[2. 예약 확인]\n[3. 예약자 명단]\n[4. 종료]")
    
    kiosk = Kiosk()
    print()
    user_input = input("입력:")
    kiosk.process_user_input(str(user_input))

    #3번 입력 시 프로그램 종료
    if user_input == "4":
        break


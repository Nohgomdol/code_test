from Kiosk_File.kiosk_reservation import Kiosk_reservation_Package
import time

class Kisok_reservation_ckeck_Package:
    def __init__(self, reser_instance):
        self.user_name_found = False
        self.reser = reser_instance
        self.reservation = Kiosk_reservation_Package()
        

    def user_check(self): #예약자 이름 입력
        print("[안내] 휴대폰번호를 입력해주세요.")
        userCheck = input("입력: ")    

        #리스트에 정보가 있고 입력한 정보가 있을 때 출력
        for self.user_info in self.reser.user_info:
            if self.user_info["phoneNumber"] == userCheck:
                self.user_name_found = True
                print("\n[안내] 예약한 정보를 확인중입니다. 잠시만 기다려주십시오.")
                time.sleep(2)                
                print("\n[안내] 예약한 정보를 찾았습니다.\n")
                print("예약 번호: {0}\n예약자: {1}\n휴대폰 번호: {2}".format(
                    self.reser.user_info.index(self.user_info) + 1,
                    self.user_info["name"],
                    self.user_info["phoneNumber"]
                ))
                break
            
        else:
            print("\n[안내] 예약한 정보를 확인중입니다. 잠시만 기다려주십시오.")
            time.sleep(2)
            print("\n[안내] 입력한 예약자를 찾을 수 없습니다. 예약을 부탁드립니다.")

        
    def user_notFound(self):
        if not self.user_name_found:
            print("\n예약 정보가 없습니다.")

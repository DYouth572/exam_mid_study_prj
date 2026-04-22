# BÀI 4: TRÒ CHƠI KÉO - BÚA - BAO (MÁY VS NGƯỜI)

import random


LUA_CHON = {"1": "Kéo", "2": "Búa", "3": "Bao"}

# Luật thắng: key thắng value
LUAT_THANG = {
    "Kéo": "Bao",   # Kéo thắng Bao
    "Búa": "Kéo",   # Búa thắng Kéo
    "Bao": "Búa",   # Bao thắng Búa
}


def xac_dinh_ket_qua(nguoi: str, may: str) -> str:
    """Trả về 'thang', 'thua', hoặc 'hoa'."""
    if nguoi == may:
        return "hoa"
    elif LUAT_THANG[nguoi] == may:
        return "thang"
    else:
        return "thua"


def bai_4_keo_bua_bao():
    
    print("BÀI 4: TRÒ CHƠI KÉO - BÚA - BAO")
    

    # Nhập số hiệp
    while True:
        try:
            so_hiep = int(input("Nhập số hiệp muốn chơi: "))
            if so_hiep <= 0:
                print("  → Số hiệp phải lớn hơn 0.")
                continue
            break
        except ValueError:
            print("  → Vui lòng nhập số nguyên.")

    thang, thua, hoa = 0, 0, 0

    for hiep in range(1, so_hiep + 1):
        print(f"\nHiệp {hiep}/{so_hiep}")
        print("Chọn: 1 = Kéo | 2 = Búa | 3 = Bao")

        while True:
            chon = input("Lựa chọn của bạn: ").strip()
            if chon in LUA_CHON:
                break
            print("Lựa chọn không hợp lệ, nhập 1, 2 hoặc 3.")

        nguoi = LUA_CHON[chon]
        may   = random.choice(list(LUA_CHON.values()))

        print(f"  Bạn chọn : {nguoi}")
        print(f"  Máy chọn : {may}")

        ket_qua = xac_dinh_ket_qua(nguoi, may)
        if ket_qua == "hoa":
            print("  Kết quả  : Hòa!")
            hoa += 1
        elif ket_qua == "thang":
            print("  Kết quả  : Bạn THẮNG :333")
            thang += 1
        else:
            print("  Kết quả  : Bạn THUA =)))))))")
            thua += 1

    # Tổng kết
    print(f"\n{'=' * 40}")
    print("KẾT QUẢ CHUNG CUỘC")
    print(f"  Thắng : {thang}  |  Thua : {thua}  |  Hòa : {hoa}")

    if thang > thua:
        ket_qua_chung = "Người chơi thắng tổng thể!"
    elif thua > thang:
        ket_qua_chung = "Máy thắng tổng thể!"
    else:
        ket_qua_chung = "Tổng thể hòa nhau!"

    print(f"  {ket_qua_chung}")

    # Lưu kết quả ra file
    with open("ket_qua_game.txt", "w", encoding="utf-8") as f:
        f.write("KẾT QUẢ TRÒ CHƠI KÉO - BÚA - BAO\n")
        f.write("-" * 35 + "\n")
        f.write(f"Tổng số hiệp : {so_hiep}\n")
        f.write(f"Thắng        : {thang}\n")
        f.write(f"Thua         : {thua}\n")
        f.write(f"Hòa          : {hoa}\n")
        f.write("-" * 35 + "\n")
        f.write(f"{ket_qua_chung}\n")

    print("Đã lưu kết quả vào 'ket_qua_game.txt'")


if __name__ == "__main__":
    bai_4_keo_bua_bao()
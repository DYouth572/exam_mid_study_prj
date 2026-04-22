# BÀI 3: MÁY TÍNH TIỀN ĐIỆN & BẮT LỖI NHẬP LIỆU


def tinh_tien_dien(kwh: float) -> float:
    """
    Tính tiền điện theo bậc thang:
      - 50 kWh đầu   : 1.600đ/kWh
      - 51 - 100 kWh : 2.000đ/kWh
      - > 100 kWh    : 2.500đ/kWh
    """
    tien = 0.0
    if kwh <= 50:
        tien = kwh * 1600
    elif kwh <= 100:
        tien = 50 * 1600 + (kwh - 50) * 2000
    else:
        tien = 50 * 1600 + 50 * 2000 + (kwh - 100) * 2500
    return tien


def bai_3_tinh_tien_dien():
    
    print("BÀI 3: MÁY TÍNH TIỀN ĐIỆN")
    
    print("Bảng giá điện bậc thang:")
    print("  ≤ 50 kWh      : 1.600 đ/kWh")
    print("  51 – 100 kWh  : 2.000 đ/kWh")
    print("  > 100 kWh     : 2.500 đ/kWh\n")

    while True:
        try:
            kwh = float(input("Nhập số kWh tiêu thụ trong tháng: "))
            if kwh < 0:
                print("Số kWh không được âm, vui lòng nhập lại.\n")
                continue
            tien = tinh_tien_dien(kwh)
            print(f"Số kWh tiêu thụ   : {kwh} kWh")
            print(f"Tiền điện phải trả: {tien:,.0f} đồng")
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ (ví dụ: 75 hoặc 150.5).\n")


if __name__ == "__main__":
    bai_3_tinh_tien_dien()
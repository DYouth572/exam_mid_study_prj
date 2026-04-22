# BÀI 5: PHÂN TÍCH LƯỢNG MƯA & VẼ BIỂU ĐỒ


import matplotlib.pyplot as plt


def bai_5_luong_mua():
    
    print("BÀI 5: PHÂN TÍCH LƯỢNG MƯA & VẼ BIỂU ĐỒ")
    

    # Dữ liệu lượng mưa Quý 1 (mm)
    luong_mua = {
        "Tháng 1": 45.5,
        "Tháng 2": 112.0,
        "Tháng 3": 89.5,
    }

    # Tính tổng và tìm tháng mưa ít nhất
    tong_luong_mua = sum(luong_mua.values())
    thang_it_nhat  = min(luong_mua, key=luong_mua.get)

    print("Dữ liệu lượng mưa Quý 1:")
    for thang, mm in luong_mua.items():
        print(f"  {thang}: {mm} mm")

    print(f"Tổng lượng mưa cả quý : {tong_luong_mua} mm")
    print(f"Tháng mưa ít nhất     : {thang_it_nhat} ({luong_mua[thang_it_nhat]} mm)")

    #Vẽ biểu đồ đường (Line chart) 
    thang_list = list(luong_mua.keys())
    mm_list    = list(luong_mua.values())

    plt.figure(figsize=(8, 5))
    plt.plot(
        thang_list, mm_list,
        marker="o",
        color="#1a73e8",
        linewidth=2.5,
        markersize=8,
        label="Lượng mưa (mm)"
    )

    # Gắn nhãn giá trị lên từng điểm dữ liệu
    for thang, mm in zip(thang_list, mm_list):
        plt.text(thang, mm + 3, f"{mm} mm", ha="center", fontsize=10, color="#333")

    plt.title("Biểu đồ lượng mưa Quý 1", fontsize=14, fontweight="bold")
    plt.xlabel("Tháng", fontsize=12)
    plt.ylabel("Lượng mưa (mm)", fontsize=12)
    plt.ylim(0, max(mm_list) * 1.25)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    plt.savefig("bieu_do_luong_mua.png", dpi=150)
    print("Biểu đồ đã được lưu thành 'bieu_do_luong_mua.png'")
    plt.show()


if __name__ == "__main__":
    bai_5_luong_mua()
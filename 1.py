# BÀI 1: QUẢN LÝ ĐIỂM SỐ SINH VIÊN

def bai_1_quan_ly_diem():

    print("BÀI 1: QUẢN LÝ ĐIỂM SỐ SINH VIÊN")
    

    danh_sach_sv = []  

    print("Nhập tên và điểm sinh viên. Nhập '0' để dừng.\n")

    while True:
        ten = input("Nhập tên sinh viên (0 để dừng): ").strip()
        if ten == "0":
            break
        if not ten:
            print("Tên không được để trống, vui lòng nhập lại.")
            continue

        while True:
            try:
                diem = float(input(f"Nhập điểm của {ten} (0 - 10): "))
                if not (0 <= diem <= 10):
                    print("Điểm phải trong khoảng 0 đến 10, nhập lại.")
                else:
                    break
            except ValueError:
                print("Điểm không hợp lệ, vui lòng nhập số.")

        danh_sach_sv.append({"ten": ten, "diem": diem})
        print(f"Đã thêm: {ten} - {diem}\n")

    if not danh_sach_sv:
        print("Chưa có sinh viên nào được nhập.")
        return

    # Tính điểm trung bình
    tong_diem = sum(sv["diem"] for sv in danh_sach_sv)
    diem_tb = tong_diem / len(danh_sach_sv)

    # Tìm sinh viên có điểm cao nhất
    sv_cao_nhat = max(danh_sach_sv, key=lambda sv: sv["diem"])

    print(f"Điểm trung bình cả lớp: {diem_tb:.2f}")
    print(f"Sinh viên điểm cao nhất: {sv_cao_nhat['ten']} ({sv_cao_nhat['diem']})")

    # Xuất ra file
    with open("diem_thi.txt", "w", encoding="utf-8") as f:
        f.write("DANH SÁCH ĐIỂM THI\n")
        f.write("-" * 30 + "\n")
        for sv in danh_sach_sv:
            f.write(f"{sv['ten']}: {sv['diem']}\n")
        f.write("-" * 30 + "\n")
        f.write(f"Điểm trung bình: {diem_tb:.2f}\n")
        f.write(f"Sinh viên điểm cao nhất: {sv_cao_nhat['ten']} ({sv_cao_nhat['diem']})\n")

    print("Đã xuất danh sách ra file 'diem_thi.txt'")


if __name__ == "__main__":
    bai_1_quan_ly_diem()
# BÀI 2: CHUẨN HÓA MÃ SẢN PHẨM

def chuan_hoa_ma(ma: str) -> str:
    """Xóa khoảng trắng thừa và viết hoa toàn bộ ký tự."""
    return ma.strip().upper()


def bai_2_chuan_hoa_ma_sp():
  
    print("BÀI 2: CHUẨN HÓA MÃ SẢN PHẨM")
    

    # Danh sách mã sản phẩm nhập sai quy cách
    ma_san_pham = [" sp-001 ", "SP-002 ", " sP-003", "  sp-004", "SP-005 "]

    print("Danh sách gốc (chưa chuẩn hóa):")
    for ma in ma_san_pham:
        print(f"  '{ma}'")

    # Chuẩn hóa bằng List Comprehension
    ma_chuan_hoa = [chuan_hoa_ma(ma) for ma in ma_san_pham]

    # Sắp xếp giảm dần theo bảng chữ cái
    ma_chuan_hoa.sort(reverse=True)

    print("\nDanh sách sau khi chuẩn hóa và sắp xếp giảm dần:")
    for ma in ma_chuan_hoa:
        print(f"  '{ma}'")


if __name__ == "__main__":
    bai_2_chuan_hoa_ma_sp()
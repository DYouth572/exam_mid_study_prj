# Đề Kiểm Tra Giữa Kỳ
**Tổng thời gian dự kiến:** 120 phút

---

## Bài 1: Quản lý điểm số sinh viên
**Đề bài:** Viết chương trình cho phép nhập tên và điểm thi của các sinh viên trong một lớp, sau đó lưu trữ dữ liệu vào một danh sách.

* **Yêu cầu:**
    * Xây dựng vòng lặp cho phép người dùng nhập liên tục tên và điểm, dừng lại khi nhập ký tự `0`.
    * Tính điểm trung bình của cả lớp và in ra tên sinh viên có điểm số cao nhất.
    * Xuất danh sách sinh viên cùng điểm số ra một file `diem_thi.txt`.

---

## Bài 2: Chuẩn hóa mã sản phẩm
**Đề bài:** Cho một danh sách chứa các mã sản phẩm nhập sai quy cách (Ví dụ: `" sp-001 "`, `"SP-002 "`, `" sP-003"`).

* **Yêu cầu:**
    * Viết hàm chuẩn hóa: Xóa toàn bộ khoảng trắng thừa và viết hoa tất cả các ký tự (Ví dụ kết quả chuẩn: `SP-001`).
    * Sắp xếp lại danh sách mã sản phẩm theo thứ tự giảm dần của bảng chữ cái.

---

## Bài 3: Máy tính tiền điện & Bắt lỗi nhập liệu
**Đề bài:** Viết ứng dụng tính tiền điện hàng tháng dựa trên số kWh tiêu thụ.

* **Yêu cầu:**
    * Tính tiền theo bậc thang cơ bản:
        * 50 kWh đầu: **1.600đ/kWh**
        * Từ 51 - 100 kWh: **2.000đ/kWh**
        * Từ 101 kWh trở lên: **2.500đ/kWh**
    * Sử dụng khối lệnh `try-except` để đảm bảo chương trình báo lỗi thân thiện (không bị crash) nếu người dùng nhập ký tự chữ thay vì số kWh.
    * Cho phép người dùng tiếp tục nhập lại nếu lần trước nhập sai định dạng.

---

## Bài 4: Trò chơi Kéo - Búa - Bao (Máy vs Người)
**Đề bài:** Viết trò chơi Kéo-Búa-Bao, trong đó máy tính sẽ chọn ngẫu nhiên một trong ba lựa chọn.

* **Yêu cầu:**
    * Cho phép người dùng nhập số hiệp muốn chơi. Sau mỗi hiệp, thông báo kết quả (Thắng, Thua, hoặc Hòa).
    * Sử dụng biến đếm để theo dõi tổng tỉ số (Số trận thắng, thua, hòa của người chơi).
    * Khi kết thúc tất cả các hiệp, lưu tổng kết tỉ số trận đấu vào một file `ket_qua_game.txt`.

---

## Bài 5: Phân tích lượng mưa & Vẽ biểu đồ
**Đề bài:** Cho một Dictionary chứa dữ liệu lượng mưa các tháng trong quý 1: `{'Thang 1': 45.5, 'Thang 2': 112.0, 'Thang 3': 89.5}` (Đơn vị: mm).

* **Yêu cầu:**
    * Viết code tính tổng lượng mưa của cả quý và tìm tháng có lượng mưa ít nhất.
    * Cài đặt và sử dụng thư viện `matplotlib` để vẽ một biểu đồ đường (Line chart) thể hiện sự biến động lượng mưa qua 3 tháng.

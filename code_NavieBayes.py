# import thư viện
import pandas as pd

# đọc dữ liệu từ file
df = pd.read_csv('data_rain.csv')

# ánh xạ tiếng Việt
temp_vn = {'Hot': 'nóng', 'Cold': 'lạnh', 'Cool': 'mát'}
wind_vn = {'Strong': 'to', 'Weak': 'nhẹ'}
moisture_vn = {'High': 'cao', 'Low': 'thấp'}

# tính xác suất P(Rain=Yes) và P(Rain=No)
p_yes = len(df[df['Rain'] == 'Yes']) / len(df)
p_no = len(df[df['Rain'] == 'No']) / len(df)

# xác suất có điều kiện P(x | Rain = Yes)
def p_x_c_yes(t, w, m):
    df_yes = df[df['Rain'] == 'Yes']
    total = len(df_yes)
    if total == 0:
        return 0
    return (
        len(df_yes[df_yes['Temp'] == t]) / total *
        len(df_yes[df_yes['Wind'] == w]) / total *
        len(df_yes[df_yes['Moisture'] == m]) / total
    )

# xác suất có điều kiện P(x | Rain = No)
def p_x_c_no(t, w, m):
    df_no = df[df['Rain'] == 'No']
    total = len(df_no)
    if total == 0:
        return 0
    return (
        len(df_no[df_no['Temp'] == t]) / total *
        len(df_no[df_no['Wind'] == w]) / total *
        len(df_no[df_no['Moisture'] == m]) / total
    )

# hàm in kết quả dự đoán
def decision(t, w, m):
    prob_yes = p_x_c_yes(t, w, m) * p_yes
    prob_no = p_x_c_no(t, w, m) * p_no

    temp_text = temp_vn.get(t, t)
    wind_text = wind_vn.get(w, w)
    moisture_text = moisture_vn.get(m, m)

    print(f"Khả năng có mưa khi trời {temp_text}, gió {wind_text}, độ ẩm {moisture_text}: {prob_yes:.4f}")
    print(f"Khả năng không mưa khi trời {temp_text}, gió {wind_text}, độ ẩm {moisture_text}: {prob_no:.4f}")

    if prob_yes > prob_no:
        print("Dự đoán: Trời sẽ có mưa")
    else:
        print("Dự đoán: Trời sẽ không có mưa")
    print('-----------------------------')

# chương trình chính
def main():
    print("BÀI TOÁN DỰ BÁO THỜI TIẾT SỬ DỤNG NAIVE BAYES")
    print("==============================================")

    # kiểm thử mẫu
    test_cases = [
        ('Hot', 'Strong', 'High'),
        ('Cold', 'Strong', 'High'),
        ('Cool', 'Weak', 'Low')
    ]
    for t, w, m in test_cases:
        decision(t, w, m)

    # phần nhập từ người dùng
    print("Nhập dữ liệu thời tiết để dự đoán:")
    t = input("Nhập nhiệt độ (Hot/Cool/Cold): ").capitalize()
    w = input("Nhập sức gió (Strong/Weak): ").capitalize()
    m = input("Nhập độ ẩm (High/Low): ").capitalize()

    # dự đoán theo dữ liệu người dùng nhập
    decision(t, w, m)

# gọi chương trình
if __name__ == '__main__':
    main()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

# Hàm để đánh giá chất lượng không khí dựa trên chỉ số AQI
def evaluate_aqi(aqi):
    if aqi == 1:
        return 'Tốt', '#00e400', '😊'  # Màu xanh lá cây
    elif aqi == 2:
        return 'Trung bình', '#ffff00', '😐'  # Màu vàng
    elif aqi == 3:
        return 'Không lành mạnh', '#ff7e00', '😷'  # Màu cam
    elif aqi == 4:
        return 'Rất không tốt', '#ff0000', '🤢'  # Màu đỏ
    else:
        return 'Nguy hiểm', '#8f3f97', '☠️'  # Màu tím

# Giao diện người dùng
st.title("Đánh giá chất lượng không khí AQI")

# # Nhập chỉ số AQI
aqi = st.number_input("Nhập chỉ số AQI", min_value=1, max_value=5, step=1)

# Tạo nút Random AQI
if st.button("Random AQI"):
    aqi = random.randint(1, 5)
    st.session_state.aqi = aqi
else:
    aqi = aqi

# Đánh giá và lấy thông tin tương ứng
rating, color, emoji = evaluate_aqi(aqi)

# CSS để tạo hiệu ứng chuyển đổi màu sắc mượt mà
st.markdown(
    """
    <style>
    .aqi-box {
        padding: 20px;
        color: white;
        text-align: center;
        border-radius: 10px;
        transition: background-color 1s ease;
        display: flex;
        align-items: center;
    }
    .aqi-prediction {
        background-color: #333333;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-right: 10px;
    }
    .aqi-content {
        display: flex;
        color: black;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        flex-grow: 1;
    }
    .aqi-content {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }
    .aqi-emoji {
        font-size: 2em;
    }
    </style>
    """, unsafe_allow_html=True
)

# Hiển thị kết quả
st.markdown(
    f"""
    <div class="aqi-box" style="background-color: {color};">
        <div class="aqi-prediction">AQI Prediction {aqi}</div>
        <div class="aqi-content">
            <h4>Đánh giá chất lượng AQI</h4>
            <p>{rating}</p>
        </div>
        <div class="aqi-emoji">{emoji}</div>
    </div>
    """, unsafe_allow_html=True
)


# Lưu trữ giá trị AQI vào session state
if 'aqi_history' not in st.session_state:
    st.session_state.aqi_history = []

st.session_state.aqi_history.append(aqi)

# Hiển thị lịch sử AQI
st.subheader("Lịch sử AQI")
aqi_df = pd.DataFrame(st.session_state.aqi_history, columns=['AQI'])
st.line_chart(aqi_df)

# Thêm mô tả chi tiết về các mức AQI
st.subheader("Thông tin chi tiết về các mức AQI")
st.markdown(
    """
    - **Tốt (0-50)**: Chất lượng không khí đạt yêu cầu và không có nguy cơ sức khỏe.
    - **Trung bình (51-100)**: Chất lượng không khí chấp nhận được; tuy nhiên, đối với một số người nhạy cảm, có thể có những tác động đến sức khỏe nhẹ.
    - **Không lành mạnh cho nhóm nhạy cảm (101-150)**: Người nhạy cảm có thể bị ảnh hưởng sức khỏe; công chúng ít bị ảnh hưởng hơn.
    - **Rất không tốt (151-200)**: Mọi người có thể bắt đầu có tác động đến sức khỏe; các thành viên của nhóm nhạy cảm có thể bị ảnh hưởng nghiêm trọng hơn.
    - **Nguy hiểm (201 trở lên)**: Cảnh báo sức khỏe về tình trạng khẩn cấp. Toàn bộ dân số có khả năng bị ảnh hưởng.
    """
)

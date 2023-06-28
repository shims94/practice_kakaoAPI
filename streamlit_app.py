import streamlit as st

# Streamlit 애플리케이션 구성
st.title("Kakao Map with Streamlit")

# Kakao 지도의 중심 좌표로 서울을 설정
center_coordinates = (37.5665, 126.9780)  # 서울의 위도(latitude)와 경도(longitude)

# Kakao 지도 웹 페이지의 URL
kakao_map_url = f"https://map.kakao.com/?urlLevel=8&lat={center_coordinates[0]}&lng={center_coordinates[1]}"

# Streamlit의 iframe을 사용하여 외부 웹 페이지 표시
st.components.v1.iframe(kakao_map_url, width=800, height=600)
import streamlit as st
import requests

def get_kakao_map(address):
    # Kakao API로부터 지도 이미지 URL 가져오기
    api_url = "https://dapi.kakao.com/v2/local/search/address.json"
    headers = {
        "Authorization": "1fa41218d89ca5171b09edf71c513fda"  # 자신의 Kakao API 키로 대체해야 합니다.
    }
    params = {
        "query": address
    }
    response = requests.get(api_url, headers=headers, params=params)
    result = response.json()
    if "documents" in result:
        documents = result["documents"]
        if documents:
            map_url = documents[0]["x"], documents[0]["y"]
            return map_url
    return None

# Streamlit 애플리케이션 구성
st.title("Kakao Map with Streamlit")
address = st.text_input("Enter an address")
if address:
    map_url = get_kakao_map(address)
    if map_url:
        st.image(map_url)
    else:
        st.warning("No map found for the provided address.")


st.title("화면확인용")
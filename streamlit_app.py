import streamlit as st
import requests

def get_coordinates(address):
    # Kakao API로부터 주소의 좌표 가져오기
    api_url = "https://dapi.kakao.com/v2/local/search/address.json"
    headers = {
        "Authorization": "516617d74f13b5ec8384a39fd879a00e"  # 자신의 Kakao API 키로 대체해야 합니다.
    }
    params = {
        "query": address
    }
    response = requests.get(api_url, headers=headers, params=params)
    result = response.json()
    if "documents" in result:
        documents = result["documents"]
        if documents:
            coordinates = documents[0]["x"], documents[0]["y"]
            return coordinates
    return None

def get_kakao_map(center_coordinates):
    x, y = center_coordinates
    map_url = f"http://dapi.kakao.com/v2/maps/staticmap?center={y},{x}&level=3&width=640&height=480"
    return map_url

# Streamlit 애플리케이션 구성
st.title("Kakao Map with Streamlit")
address = st.text_input("Enter an address")
if address:
    coordinates = get_coordinates(address)
    if coordinates:
        map_url = get_kakao_map(coordinates)
        st.image(map_url)
    else:
        st.warning("No coordinates found for the provided address.")
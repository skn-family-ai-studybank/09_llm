"""Streamlit으로 실행하는 파일

[실행 방법]
1. 터미널 접속
2. 현재 폴더로 이동(cd)
3. streamlit run app.py

[참고 사항]
Streamlit은 사용자가 화면(위젯)을 조작하게되면
해당 파일(app.py)를 다시 실행한다.
"""

import logging # 오류를 파이썬 터미널에 출력하는 라이브러리

import streamlit as st

from rag import (
    SommelierConfigurationError, # 사용자 정의 예외
    ai_sommelier_rag,   # 이미지 -> 와인 추천 체인
    validate_public_image_url # 이미지 url 검사
)

# 개발자가 보기 위한 로그를 출력하는 객체 생성
logger = logging.getLogger(__name__)

# 브라우저 탭 아이콘, 제목 설정, 화면 가운데 정렬
st.set_page_config(
    page_title="AI Wine Sommelier",
    page_icon="🍷",
    layout="centered",
)

# 페이지 제목
st.title("🍷 AI Wine Sommelier")

st.write(
    "음식 이미지 URL을 입력하면 Wine Magazine 리뷰를 검색해 "
    "어울리는 와인을 추천한다"
)

st.info(
    "공개 HTTPS 이미지 URL만 사용한다. "
    "제출한 URL은 음식 분석을 위해 OpenAI에 전달된다."
)

# st.form()은 여러 입력을 하나로 묶어서 제출할 수 있게하는 역할
# st.form_submit_button(): 해당 form의 모든 입력을 제출하는 역할
with st.form(key="image_url_form", clear_on_submit=False):

    image_url_input = st.text_input(
        "음식 이미지 URL",
        placeholder="https://example.com/food.jpg", #힌트
        max_chars=2048,
        help='로그인 없이 직접 접근 가능한 HTTPS 이미지 주소 입력'
    )

    submitted = st.form_submit_button(
        "와인 추천 받기",
        type="primary"
    )


import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("오류: GOOGLE_API_KEY가 설정되지 않았습니다.")
    sys.exit(1)

genai.configure(api_key=api_key)

# 1. 사용할 모델 선택 
model = genai.GenerativeModel('models/gemini-2.5-flash') 

try:
    # 2. 터미널에서 사용자 입력 받기
    user_input = input("설명할 Python 코드를 입력하세요 (종료하려면 'exit' 입력): ")

    if user_input.lower() == 'exit':
        print("프로그램을 종료합니다.")
        sys.exit(0)

    # 3. 프롬프트 구성 
    # "Python 코드 설명기" 기능 구현 
    prompt = f"""
    당신은 전문 Python 개발자입니다. 
    다음 Python 코드의 역할을 한글로 간결하게 설명해주세요.

    [코드]
    {user_input}

    [설명]
    """

    # 4. API 호출
    response = model.generate_content(prompt)

    # 5. 결과 출력 (라이브 데모 시연 부분) 
    print("--- Gemini의 설명 ---")
    print(response.text)
    print("---------------------")

except Exception as e:
    print(f"오류가 발생했습니다: {e}")
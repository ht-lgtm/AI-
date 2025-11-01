import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("오류: GOOGLE_API_KEY가 .env 파일에 설정되지 않았습니다.")
    sys.exit(1)

genai.configure(api_key=api_key)

print("--- 사용 가능한 모델 목록 ---")

try:
    # API 키로 접근 가능한 모든 모델을 나열합니다.
    for m in genai.list_models():
        # 'generateContent' (채팅/텍스트 생성)을 지원하는 모델인지 확인
        if 'generateContent' in m.supported_generation_methods:
            print(f"* {m.name}") # 모델 이름 출력

except Exception as e:
    print(f"모델 목록을 불러오는 중 오류 발생: {e}")
    print("\nGoogle AI Studio 또는 Google Cloud Console에서 API 키가 올바르게 활성화되었는지 확인해 주세요.")

print("--------------------------")
from flask import Flask, render_template, request, jsonify
import requests
import feedparser
import urllib.parse
import json

app = Flask(__name__)

# API 설정 (사용자 키 적용)
GMS_KEY = ""
API_URL = "https://gms.ssafy.io/gmsapi/api.openai.com/v1/chat/completions"

def call_llm(messages):
    """LLM API 호출 공통 함수 - 400 에러 상세 사유 출력 포함"""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {GMS_KEY}'
    }
    
    # ⚠️ 모델명을 gpt-4o 또는 gpt-3.5-turbo로 테스트해보세요.
    # gpt-5-nano가 유효하지 않을 경우 400 에러가 발생합니다.
    payload = {
        "model": "gpt-4o", # 모델명을 확인 후 수정하세요
        "messages": messages,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=15)
        
        if response.status_code != 200:
            # 🔍 터미널에서 아래 출력 내용을 확인하면 400 에러의 진짜 이유가 나옵니다.
            print(f"❌ API 에러 상세 정보: {response.text}")
            
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ LLM Call Error: {e}")
        return {
            "choices": [{
                "message": {
                    "content": f"시스템 오류가 발생했습니다. (사유: {str(e)})"
                }
            }]
        }

def fetch_google_news(query):
    """4.2.2 Google News RSS 기반 기사 수집"""
    encoded_query = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=ko&gl=KR&ceid=KR:ko"
    
    feed = feedparser.parse(url)
    articles = []
    
    for entry in feed.entries[:5]:
        articles.append(f"제목: {entry.title}\n출처: {entry.source.get('title', '알 수 없음')}\n링크: {entry.link}\n")
    
    return "\n".join(articles) if articles else "관련 최신 기사를 찾을 수 없습니다."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.json
    user_messages = user_data.get("messages", [])
    
    if not user_messages:
        return jsonify({"error": "No messages"}), 400

    # 4.2.1 모든 'developer' 역할을 'system'으로 강제 변환 (호환성 확보)
    for msg in user_messages:
        if msg['role'] == 'developer':
            msg['role'] = 'system'

    last_user_content = user_messages[-1]['content']

    # --- 기사 검색 의도 판별 로직 ---
    intent_prompt = [
        {
            "role": "system", 
            "content": "사용자의 질문이 뉴스, 기사, 소식 검색을 요구하면 'NEWS', 아니면 'CHAT'이라고 답하세요. 한 단어로만 대답하세요."
        },
        {"role": "user", "content": last_user_content}
    ]
    
    intent_result = call_llm(intent_prompt)
    intent = "CHAT"
    
    if intent_result and 'choices' in intent_result:
        intent = intent_result['choices'][0]['message']['content'].strip().upper()

    print(f"🔍 판단된 의도: {intent}")

    # --- 4.2.2 기사 검색 및 요약 처리 ---
    if "NEWS" in intent:
        print("📰 기사 검색을 수행합니다...")
        news_context = fetch_google_news(last_user_content)
        
        # 기사 정보를 요약 정리하도록 지시 추가
        news_instruction = f"\n\n[참고 뉴스]\n{news_context}\n\n위 뉴스를 바탕으로 상세히 요약 정리해줘. 링크 나열은 금지해."
        user_messages[-1]['content'] += news_instruction

    # 최종 상세 답변 생성
    final_result = call_llm(user_messages)

    print("--- 응답 전송 완료 ---")
    return jsonify(final_result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
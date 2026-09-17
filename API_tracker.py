from http.server import BaseHTTPRequestHandler
import json
import os
import requests

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        name = data.get('name')
        birth = data.get('birth')
        api_key = os.environ.get('OPENAI_API_KEY')

        if not api_key:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'API key not configured'}).encode())
            return

        prompt = f"이름이 {name}이고 생년월일이 {birth}인 사람이 지금 어디서 무엇을 하고 있을지 아주 위트 있고 상상력 풍부하게 2문장으로 알려줘. 마치 점쟁이나 첨단 위성 추적기처럼 말해줘."

        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": prompt}]
                }
            )
            res_data = response.json()
            ai_message = res_data['choices'][0]['message']['content']

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': ai_message}).encode())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
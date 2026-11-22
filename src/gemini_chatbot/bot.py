import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Google AI Studio 무료 티어 지원 모델
MODEL_NAME = "gemini-3.1-flash-lite"

class GeminiChatBot:
    """메모리(이력 보존) 없는 단일 턴 질의응답 챗봇"""

    def __init__(self, model: str = MODEL_NAME):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY 환경변수가 설정되지 않았습니다.\n"
                ".env 파일에 'GEMINI_API_KEY=your_key' 형태로 입력해주세요.\n"
                "API 키 발급: https://aistudio.google.com/apikey"
            )
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def send_message(self, message: str) -> str:
        """이전 대화 맥락 없이 독립적으로 응답을 생성합니다."""
        interaction = self.client.interactions.create(
            model=self.model,
            input=message,
        )
        return interaction.output_text or ""

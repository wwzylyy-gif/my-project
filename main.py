from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)
def run_agent(task):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "你是一位专业AI研究助手，请输出结构化分析。"
            },
            {
                "role": "user",
                "content": task
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    task = input("请输入研究主题：")
    result = run_agent(task)

    print("\n====================")
    print(result)
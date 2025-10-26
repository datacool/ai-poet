from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from dotenv import load_dotenv
#from pathlib import Path 
#import os 
import streamlit as st 

#env_path = Path('../.env')
#load_dotenv(dotenv_path=env_path)

#ChatOpenAI 초기화
llm = init_chat_model(model="gpt-4o-mini", model_provider="openai")

#Prompt 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

#문자열 출력 파서
output_parser = StrOutputParser()

#LLM 체인 구성
chain = prompt | llm | output_parser

#제목
st.title("인공지능 시인")

#시 주제 입력 필드
content = st.text_input("시의 주제를 제시해주세요", "AI와 인간")
st.write("시의 주제는", content)

#시 작성 요청하기
if st.button("시 작성 요청하기"):
    with st.spinner("I'm generating the poetry, Please wait for it.."):
        result = chain.invoke({"input" : content + "에 대한 시를 써줘"})
        st.write(result)


#"""'''content = "코딩"
#result = chain.invoke({"input": content+"에 대한 시를 작성해줘"})
#print(result)

#st.title('This is a title.')
#st.title('_Streamlit_ is :blue[cool] :sunglasses:')
#'''"""

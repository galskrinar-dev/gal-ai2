import streamlit as st
from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="GAL AI", page_icon="🚀")

st.title("🚀 GAL AI - Napredni Slovenski Agent")
st.write("Vpiši vprašanje in moj agent bo raziskal odgovor zate.")

vprasanje = st.text_input("Tvoje vprašanje:", placeholder="Npr. Kakšni so trendi v fiziki leta 2026?")

if st.button("Analiziraj"):
    with st.spinner("GAL AI razmišlja..."):
        # Tukaj se povežemo z Geminijem (ključ bomo vnesli v nastavitvah oblaka)
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
        
        gal_agent = Agent(
            role='GAL AI Svetovalec',
            goal=f'Podaj globok in preverjen odgovor na: {vprasanje}',
            backstory='Si najnaprednejši slovenski AI agent podjetja GAL.',
            llm=llm
        )
        
        task = Task(description=vprasanje, agent=gal_agent, expected_output="Popoln strokovni odgovor.")
        crew = Crew(agents=[gal_agent], tasks=[task])
        
        result = crew.kickoff()
        st.success("Analiza končana!")
        st.markdown(f"### Odgovor GAL AI:\n{result}")

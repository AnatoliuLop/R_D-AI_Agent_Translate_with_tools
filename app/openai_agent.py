# app/openai_agent.py
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from app.grammar_tool import explain_grammar
from app.style_tool import improve_style
from app.llm_client import llm  # ✅ імпорт звідси, без циклу


# Tool 1 — граматика
grammar_tool = Tool.from_function(
    func=explain_grammar,
    name="ExplainGrammar",
    description="Пояснює граматику англійського речення"
)

# Tool 2 — покращення стилю
style_tool = Tool.from_function(
    func=improve_style,
    name="ImproveStyle",
    description="Робить речення формальнішим"
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=OpenAIFunctionsAgent.from_llm_and_tools(llm=llm, tools=[grammar_tool, style_tool]),
    tools=[grammar_tool, style_tool],
    verbose=True
)

__all__ = ["llm", "explain_grammar", "improve_style"]

from llamafile_langchain.core import LlamafileLLM

def test_basic_call():
    llm = LlamafileLLM(model_path="echo")  # Use 'echo' for dry test
    response = llm.invoke("Hello world")
    assert "Hello world" in response

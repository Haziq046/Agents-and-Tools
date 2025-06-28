from agents import ChatAgent

def test_chat_response_contains_summary():
    ag = ChatAgent("Tester")
    out = ag.act("Python is awesome but my IDE crashed. Bad day!")
    assert "Summary" in out

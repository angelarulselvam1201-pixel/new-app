import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Scientific Calculator")

st.write("Enter any mathematical expression. Supports advanced functions like:")
st.markdown("""
- **sin, cos, tan**
- **log, ln**
- **sqrt**
- **factorial (!)**
- **pi, e**
- **power (^ or **)**
- Parentheses
""")

# Allowed names mapping for eval
allowed = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,       # log(x, base) supported
    "ln": math.log,        # same as natural log
    "sqrt": math.sqrt,
    "factorial": math.factorial,
    "pi": math.pi,
    "e": math.e,
    "pow": pow
}

expression = st.text_input("Enter expression:", value="sin(pi/2) + sqrt(16) + 5^2")

def safe_eval(expr):
    try:
        expr = expr.replace("^", "**")
        return eval(expr, {"__builtins__": None}, allowed)
    except Exception as e:
        return f"Error: {e}"

if st.button("Calculate"):
    result = safe_eval(expression)
    if isinstance(result, (int, float)):
        st.success(f"Result: {result}")
    else:
        st.error(result)

# History
if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Add to History"):
    res = safe_eval(expression)
    if isinstance(res, (int, float)):
        st.session_state.history.append(f"{expression} = {res}")
        st.info("Added to history.")
    else:
        st.error("Invalid expression, not added.")

if st.session_state.history:
    st.subheader("History")
    for item in reversed(st.session_state.history[-20:]):
        st.write(item)

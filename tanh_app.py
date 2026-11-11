
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Activation Function")

st.title("Hyperbolic Tangent (Tanh) Activation Function")

st.write("""
The Tanh function converts an input value
into an output between -1 and 1.
""")

st.latex(r"f(x) = \tanh(x)")

# Input slider
x_value = st.slider(
    "Choose an input value",
    -10.0, 10.0, 0.0, 0.5
)

# Calculate output
y_value = np.tanh(x_value)

st.metric("Tanh Output", f"{y_value:.4f}")

# Create graph
x = np.linspace(-10, 10, 400)
y = np.tanh(x)

fig, ax = plt.subplots()

ax.plot(x, y, label="Tanh")
ax.scatter(x_value, y_value, color="red",
           label="Selected Input")

ax.set_title("Tanh Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output f(x)")
ax.set_ylim(-1.1, 1.1)
ax.grid(True)
ax.legend()

st.pyplot(fig)

st.subheader("Explanation")

st.write("1. The output is always between -1 and 1.")
st.write("2. When the input is 0, the output is 0.")
st.write("3. Tanh produces both negative and positive output values.")
# %%
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'vscode'
import numpy as np

import streamlit as sd
# %%
fig = px.line(np.arange(10))
# fig.show()
sd.plotly_chart(fig)
# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col, trunc, lit
import plotly.express as px

DATABASE='snowpark_playground'
SCHEMA = 'time_series'
TABLE = 'stocks_import'

AC = 'ASSET_CLASS'
PEN = 'PRIMARY_EXCHANGE_NAME'
VN = "VARIABLE_NAME"

# Get the current credentials
session = get_active_session()


# reference the table -> nothing gets executed here
df_stocks=session.table(f"{DATABASE}.{SCHEMA}.{TABLE}")

st.title("Let's analyze stocks :balloon:")

# st.markdown("### Stocks data")
# # lazy evaluation -> the df gets evaluated here
# #st.write(df_stocks.sample(n=100))
# st.write(df_stocks.limit(1000))

# st.markdown("### Filter stocks")

# asset_class, exchange, price_type = st.columns(3)
# with asset_class:
#     selected_asset_class = st.selectbox("Asset Class",index=4,options=df_stocks.select(AC).distinct().sort(AC, ascending=True))
# with exchange:
#     selected_pen=st.selectbox("Exchange", df_stocks.select(PEN).distinct().sort(PEN, ascending=True))
# with price_type:
#     selected_pt = st.selectbox("Price Type", df_stocks.select(VN).distinct().sort(VN, ascending=True))

# df_stats = df_stocks.filter( (col(AC)== selected_asset_class) & (col(PEN)==selected_pen) & 
#                             (col(VN) == selected_pt))
# st.dataframe(df_stats.select('TICKER','DATE', 'VALUE').limit(100))


# # df_stocks.select('ticker', trunc('date',lit('QUARTER')).as_('quarter')).limit(10).collect()
# df_quarter_avg=df_stocks.select('ticker','value',trunc('date',lit('QUARTER')).as_('quarter')).group_by('ticker','quarter').avg('value').order_by('ticker', 'quarter')
# data = df_quarter_avg.filter("ticker in ('AAPL', 'GOOG', 'NVDA')")


# df_quarter_avg=df_stocks.select('ticker','value',trunc('date',lit('QUARTER')).as_('quarter'), 'variable').filter("variable = 'post-market_close'").group_by('ticker','quarter').avg('value').order_by('ticker', 'quarter')
# data = df_quarter_avg.filter("ticker in ('AAPL', 'GOOG', 'NVDA')")
# fig = px.bar(data, x="QUARTER", y="AVG(VALUE)", 
#                  color="TICKER", barmode="group")
# fig


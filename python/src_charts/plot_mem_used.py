import pandas as pd
from tabulate import tabulate
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import logging
import plotly.express as px

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test")


def plot_icycle():
    # ----------
    df = px.data.tips()
    print(df.to_markdown())
    fig = px.icicle(df, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill')
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    fig.show()

    # -----------
    df_tmp = cr_df_mem()
    df = df_tmp.filter(['host', 'process', 'pct'], axis=1)
    df.reset_index(inplace=True)
    print(df.to_markdown())
    fig = px.icicle(df, path=[px.Constant("all"), 'host', 'process'], values='pct')
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    fig.show()

def cr_df_mem():
    period = 100
    date_today = datetime.now()
    ts = pd.date_range(date_today, date_today + timedelta(period), freq='D')
    logger.debug("days = {}".format(ts))
    np.random.seed(seed=1111)

    host = np.random.randint(15, high=20, size=len(ts))
    process = np.random.randint(10, high=50, size=len(ts))
    used_mem = np.random.randint(10, high=60, size=len(ts))
    allocated_mem = np.random.randint(30, high=50, size=len(ts))
    df = pd.DataFrame({'host': host, 'process': process, 'used_mem': used_mem, 'allocated_mem': allocated_mem})
    df.set_index('process', inplace=True)
    df['pct'] = 100 * df['allocated_mem'] / df.groupby(['host'])['allocated_mem'].transform('sum')
    df.sort_values(by=['host', 'process'], inplace=True)
    df.columns.name = "metric"
    #print(df.to_markdown())
    return df


# -------------------
# main
# -------------------
logger.info("start")
plot_icycle()
logger.info("end")


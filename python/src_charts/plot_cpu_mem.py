import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import logging
import plotly.express as px

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test")


def cr_plotly_ts():
    # Using plotly.express
    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG")
    fig.show()


def cr_plotly_ts2():
    df = px.data.stocks(indexed=True) - 1
    logger.info(df)
    fig = px.bar(df, x=df.index, y="GOOG")
    fig.show()


def cr_plotly_ts3():
    df = cr_df_cpu_mem()
    logger.info("cols in df : {}".format(df.columns.to_list()))
    fig = px.bar(df, x=df.index, y="cpu")
    fig.show()


def cr_plotly_area():
    df = cr_df_cpu_mem()
    logger.info("cols in df : {}".format(df.columns.to_list()))
    fig = px.area(df, facet_col="metric", facet_col_wrap=1)
    fig.show()


def cr_plotly_bar():
    df = cr_app_latency()
    logger.info("cols in df : {}".format(df.columns.to_list()))
    fig = px.bar(df, facet_col="metric", facet_col_wrap=1)
    fig.show()


def cr_plotly_grouped_bar():
    df = cr_df_cpu_mem()
    fig = px.line(df, x=df.index, y=df.columns.to_list())
    fig = px.bar(df, x=df.index, y=df.columns.to_list(), barmode='group')

    # Show plot
    fig.show()

def cr_plotly_bar_and_line():
    df = cr_df_cpu_mem()

    # set up plotly figure
    fig = make_subplots(1, 2)

    # add first bar trace at row = 1, col = 1
    col = 'cpu'
    fig.add_trace(go.Bar(x=df.index, y=df[col], name=col, marker_color='green', opacity=0.4, ), row=1, col=1)

    # add first scatter trace at row = 1, col = 1
    col = 'mem'
    fig.add_trace(go.Scatter(x=df.index, y=df[col], line=dict(color='red'), name=col), row=1, col=1)

    # add first bar trace at row = 1, col = 2
    col = 'gc_pause'
    fig.add_trace(go.Bar(x=df.index, y=df[col], name=col, marker_color='green', opacity=0.4, ), row=1, col=2)
    fig.show()

def cr_plotly_bar_dot():
    df = cr_df_cpu_mem()

    # set up plotly figure
    fig = make_subplots(1, 1)

    # add first bar trace at row = 1, col = 1
    col = 'cpu'
    fig.add_trace(go.Bar(x=df.index, y=df[col], name=col, marker_color='green', opacity=0.4), row=1, col=1)

    # add first scatter trace at row = 1, col = 1
    col = 'mem'
    fig.add_trace(go.Scatter(x=df.index, y=df[col], marker=dict(color='red'), mode="markers", name=col), row=1, col=1)

    # add first scatter trace at row = 1, col = 1
    col = 'gc_pause'
    fig.add_trace(go.Scatter(x=df.index, y=df[col], line=dict(color='blue'),  name=col), row=1, col=1)

    fig.show()

def cr_plotly_overlaid_area():
    df = cr_df_cpu_mem()

    fig = go.Figure()
    col='cpu'
    fig.add_trace(go.Scatter(x=df.index, y=df[col], fill='tozeroy',
                         mode='none' # override default markers+lines
                         ))
    col = 'mem'
    fig.add_trace(go.Scatter(x=df.index, y=df[col], fill='tonexty',
                         mode= 'none'))

    fig.show()


def cr_df_cpu_mem():
    period = 100
    date_today = datetime.now()
    ts = pd.date_range(date_today, date_today + timedelta(period), freq='D')
    logger.debug("days = {}".format(ts))
    np.random.seed(seed=1111)

    cpu = np.random.randint(1, high=100, size=len(ts))
    mem = np.random.randint(1, high=100, size=len(ts))
    gc_pause = np.random.randint(1, high=100, size=len(ts))
    df = pd.DataFrame({'ts': ts, 'cpu': cpu, 'mem': mem, 'gc_pause': gc_pause})

    df = df.set_index('ts')
    df.columns.name = "metric"
    logger.info(df)
    return df

def cr_app_latency():
    period = 100
    date_today = datetime.now()
    ts = pd.date_range(date_today, date_today + timedelta(period), freq='D')
    logger.debug("days = {}".format(ts))
    np.random.seed(seed=1111)

    qlib_svc = np.random.randint(1, high=100, size=len(ts))
    qls_pricer = np.random.randint(1, high=100, size=len(ts))
    nrs_cascade = np.random.randint(1, high=100, size=len(ts))
    nrs = np.random.randint(1, high=100, size=len(ts))
    snapper = np.random.randint(1, high=100, size=len(ts))
    df = pd.DataFrame({'ts': ts,
                       'qlib-svc-latency': qlib_svc,
                       'qls-pricer-latency': qls_pricer,
                       'nrs-cascade-latency': nrs_cascade,
                       'nrs-latency': nrs,
                       'snapper-latency': snapper,
                       })

    df = df.set_index('ts')
    df.columns.name = "metric"
    logger.info(df)
    return df

# -------------------
# main
# -------------------
logger.info("start")
# cr_df_cpu_mem()
# cr_plotly_ts()
# cr_plotly_ts2()
# cr_plotly_ts3()
# cr_plotly_ts4()
# cr_plotly_ts5()
#cr_plotly_grouped_bar()
#cr_plotly_area() # Good
#cr_plotly_bar_and_line()
cr_plotly_bar()
#cr_plotly_bar_dot()
#cr_plotly_overlaid_area()
logger.info("end")

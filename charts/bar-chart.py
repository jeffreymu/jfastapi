import pyecharts
from pyecharts import options as opts

bar = (
    pyecharts.charts.Bar()
        .add_xaxis(["Gene1", "Gene2", "Gene3", "Gene4", "Gene5", "Gene6", "Gene7"])
        .add_yaxis("CTCF", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("RAD21", [57, 134, 137, 129, 145, 60, 49])
        .set_colors(['#00A383', '#FF6400'])
        .set_global_opts(title_opts=opts.TitleOpts(title="Correlation"))

)

bar.render("bar-demo-01.html")
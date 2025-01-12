from pywebio.output import put_html
import random

from pyecharts import options as opts
from pyecharts.charts import HeatMap
from pyecharts.faker import Faker

value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
c = (
    HeatMap()
    .add_xaxis(Faker.clock)
    .add_yaxis("series0", Faker.week, value)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="HeatMap-基本示例"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    
)

c.width = "100%"
put_html(c.render_notebook())

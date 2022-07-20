from dashing import HSplit, VSplit, Text, HGauge


ui = HSplit(
        VSplit(
            Text(' ', border_color=3, title='Total System Process: '),
            Text(' ', border_color=3),
        ),
        VSplit(
            HGauge(border_color=2, title='Total CPU usage'),
            HGauge(border_color=2, title='CORE-1'),
            HGauge(border_color=2, title='CORE-2'),
            HGauge(border_color=2, title='CORE-3'),
            HGauge(border_color=2, title='CORE-4'),
            border_color=2,
            title='CPU Section'
        ),
        VSplit(
            Text(' ', border_color=3),
            Text(' ', border_color=3),
        ),
)

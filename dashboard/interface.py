from dashing import HSplit, VSplit, Text, HGauge


ui = HSplit(
        VSplit(
            Text(' ', title='Total System Process: ', border_color=3, color=7),
            HSplit(
                VSplit(
                    Text(' ', border_color=5, color=7),
                    HSplit(
                        HGauge(title='RAM', border_color=5, color=4),
                        HGauge(title='SWAP', border_color=5, color=4),
                    ),
                    title='Memory Section',
                    border_color=5
                ),
            ),
        ),
        VSplit(
            HGauge(border_color=2, title='Total CPU usage'),
            HGauge(border_color=2, title='CORE-1'),
            HGauge(border_color=2, title='CORE-2'),
            HGauge(border_color=2, title='CORE-3'),
            HGauge(border_color=2, title='CORE-4'),
            title='CPU Section',
            border_color=2,
        ),
)

from dashing import HSplit, VSplit, Text, HGauge, VGauge


ui = HSplit(
        VSplit(
            Text(' ', title='Total System Process: ', border_color=3),
            HSplit(
                VSplit(
                    Text(' ', title='Memory Infos', border_color=5),
                    HSplit(
                        VGauge(title='RAM', border_color=5),
                        VGauge(title='SWAP', border_color=5),
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
            border_color=2,
            title='CPU Section'
        ),
        VSplit(
            Text(' ', border_color=3),
            Text(' ', border_color=3),
        ),
)

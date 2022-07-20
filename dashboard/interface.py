from dashing import HSplit, VSplit, Text


ui = HSplit(
        VSplit(
            Text(' ', border_color=3, title='Total System Process: '),
            Text(' ', border_color=3),
        ),
        VSplit(
            Text(' '),
            border_color=2,
            title='CPU Section'
        ),
        VSplit(
            Text(' ', border_color=3),
            Text(' ', border_color=3),
        ),
)

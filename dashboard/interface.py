from dashing import HSplit, VSplit, Text


ui = HSplit(
    VSplit(
        Text(' ', title='teste'),
        title='Process List',
        border_color=4,

    ),
    border_color=3,
    title='Process Analyzer',
)

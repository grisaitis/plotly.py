import _plotly_utils.basevalidators


class AspectratioValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='aspectratio', parent_name='layout.scene', **kwargs
    ):
        super(AspectratioValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Aspectratio',
            data_docs="""
            x

            y

            z
""",
            **kwargs
        )
import numpy as np

import traits.api as traits
import traitsui.api as ui
import chaco.api as chaco
from enable.api import ComponentEditor


class PlotController(ui.Controller):
    view = ui.View(ui.Item('plot', editor=ComponentEditor(), show_label=False),
                   height=300, width=300, resizable=True)

    def object_close_signal_changed(self, info):
        info.ui.dispose()


class BasicPlot(traits.HasTraits):
    close_signal = traits.Event()
    plot = traits.Instance(chaco.Plot)


class LinePlot(BasicPlot):

    def __init__(self, plotdata):
        self.plot = chaco.Plot(plotdata)
        self.plot.plot(('x', 'y'))


class BarPlot(BasicPlot):

    def __init__(self, plotdata):
        self.plot = chaco.Plot(plotdata)
        self.plot.candle_plot(('x', 'ymin', 'ymax'))


available_plot_types = dict(line=LinePlot, bar=BarPlot)

class PlotSelector(traits.HasTraits):

    plot_type = traits.Enum(['line', 'bar'])
    traits_view = ui.View('plot_type', style='custom')

    def __init__(self, x, y):
        ymin = y - 1
        ymax = y + 1
        self.plotdata = chaco.ArrayPlotData(x=x, y=y, ymin=ymin, ymax=ymax)
        self.figure = None

    def _plot_type_changed(self):
        plot_class = available_plot_types[self.plot_type]
        if self.figure is not None:
            self.figure.close_signal = True
        self.figure = plot_class(self.plotdata)
        controller = PlotController(model=self.figure)
        controller.edit_traits()


N = 20
x = np.arange(N)
y = x + np.random.normal(size=N)
plot_selector = PlotSelector(x, y)
plot_selector.configure_traits()

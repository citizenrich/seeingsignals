#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: twodimension_usrp_b210s
# Author: citizenrich
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import uhd
import time
from gnuradio import video_sdl
from gnuradio.qtgui import Range, RangeWidget
import math
import numpy as np
import threading

from gnuradio import qtgui

class twodimension_usrp_b210s(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "twodimension_usrp_b210s")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("twodimension_usrp_b210s")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "twodimension_usrp_b210s")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.maxtheta = maxtheta = 150
        self.columns = columns = 100
        self.shiftarrL = shiftarrL = np.radians(np.linspace(start=maxtheta, stop=0, num=int(columns/2), endpoint=False))
        self.left = left = np.pad(shiftarrL, (0, int(columns/2)), 'constant')
        self.variable_function_probe_0_0 = variable_function_probe_0_0 = 0
        self.variable_function_probe_0 = variable_function_probe_0 = 1
        self.right = right = np.flip(left, axis=0)
        self.variable_qtgui_label_0_0_0_0 = variable_qtgui_label_0_0_0_0 = variable_function_probe_0_0
        self.variable_qtgui_label_0_0_0 = variable_qtgui_label_0_0_0 = variable_function_probe_0
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0 = left
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = right
        self.threshold = threshold = -60
        self.scale = scale = 20000
        self.samp_rate = samp_rate = 100e3
        self.minmag = minmag = 0
        self.maxmag = maxmag = .0035
        self.keep = keep = 50
        self.gain = gain = 20
        self.freq = freq = 422e6
        self.displayscale = displayscale = 5

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Time rasters')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Steering vectors')
        self.top_grid_layout.addWidget(self.tab)
        self._scale_range = Range(0, 60000, 1000, 20000, 200)
        self._scale_win = RangeWidget(self._scale_range, self.set_scale, 'scale', "counter_slider", float)
        self.top_grid_layout.addWidget(self._scale_win)
        self.blocks_probe_signal_x_0_0 = blocks.probe_signal_f()
        self.blocks_probe_signal_x_0 = blocks.probe_signal_f()
        self.video_sdl_sink_1_1_0 = video_sdl.sink_s(0, columns, columns, 0, columns*displayscale, columns*displayscale)
        self._variable_qtgui_label_0_0_0_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_0_0_0_formatter = None
        else:
            self._variable_qtgui_label_0_0_0_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_0_0_0_tool_bar.addWidget(Qt.QLabel('Probe Signal Min' + ": "))
        self._variable_qtgui_label_0_0_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_0_0_formatter(self.variable_qtgui_label_0_0_0_0)))
        self._variable_qtgui_label_0_0_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_0_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_0_0_0_tool_bar)
        self._variable_qtgui_label_0_0_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_0_0_formatter = None
        else:
            self._variable_qtgui_label_0_0_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_0_0_tool_bar.addWidget(Qt.QLabel('Probe Signal Max' + ": "))
        self._variable_qtgui_label_0_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_0_formatter(self.variable_qtgui_label_0_0_0)))
        self._variable_qtgui_label_0_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_0_0_tool_bar)
        self._variable_qtgui_label_0_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_0_formatter = None
        else:
            self._variable_qtgui_label_0_0_formatter = lambda x: repr(x)

        self._variable_qtgui_label_0_0_tool_bar.addWidget(Qt.QLabel('variable_qtgui_label_0_0' + ": "))
        self._variable_qtgui_label_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_formatter(self.variable_qtgui_label_0_0)))
        self._variable_qtgui_label_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_label)
        self.tab_layout_1.addWidget(self._variable_qtgui_label_0_0_tool_bar)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_formatter = None
        else:
            self._variable_qtgui_label_0_formatter = lambda x: repr(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('variable_qtgui_label_0' + ": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.tab_layout_1.addWidget(self._variable_qtgui_label_0_tool_bar)
        def _variable_function_probe_0_0_probe():
            while True:

                val = self.blocks_probe_signal_x_0_0.level()
                try:
                    self.set_variable_function_probe_0_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (1))
        _variable_function_probe_0_0_thread = threading.Thread(target=_variable_function_probe_0_0_probe)
        _variable_function_probe_0_0_thread.daemon = True
        _variable_function_probe_0_0_thread.start()

        def _variable_function_probe_0_probe():
            while True:

                val = self.blocks_probe_signal_x_0.level()
                try:
                    self.set_variable_function_probe_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (1))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()

        self.uhd_usrp_source_0_0 = uhd.usrp_source(
            ",".join(("", "type=b200, name=origb210")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
        )
        self.uhd_usrp_source_0_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0_0.set_gain(gain, 0)
        self.uhd_usrp_source_0_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0_0.set_center_freq(freq, 1)
        self.uhd_usrp_source_0_0.set_gain(gain, 1)
        self.uhd_usrp_source_0_0.set_antenna('RX2', 1)
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "type=b200, name=newb210")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
        )
        self.uhd_usrp_source_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_center_freq(freq, 1)
        self.uhd_usrp_source_0.set_gain(gain, 1)
        self.uhd_usrp_source_0.set_antenna('RX2', 1)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec())
        self._threshold_range = Range(-160, -10, 5, -60, 200)
        self._threshold_win = RangeWidget(self._threshold_range, self.set_threshold, 'squelch threshold', "counter_slider", int)
        self.top_grid_layout.addWidget(self._threshold_win)
        self.qtgui_time_raster_sink_x_0_0 = qtgui.time_raster_sink_f(
            samp_rate/keep,
            columns,
            columns,
            [],
            [],
            "Elevation",
            1
        )

        self.qtgui_time_raster_sink_x_0_0.set_update_time(0.01)
        self.qtgui_time_raster_sink_x_0_0.set_intensity_range(minmag, maxmag)
        self.qtgui_time_raster_sink_x_0_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [0, 1, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_time_raster_sink_x_0_0_win)
        self.qtgui_time_raster_sink_x_0 = qtgui.time_raster_sink_f(
            samp_rate/keep,
            columns,
            columns,
            [],
            [],
            "Azimuth",
            1
        )

        self.qtgui_time_raster_sink_x_0.set_update_time(0.01)
        self.qtgui_time_raster_sink_x_0.set_intensity_range(minmag, maxmag)
        self.qtgui_time_raster_sink_x_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [0, 1, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_time_raster_sink_x_0_win)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, columns)
        self.blocks_vector_source_x_0_0_0_1 = blocks.vector_source_f(left, True, 1, [])
        self.blocks_vector_source_x_0_0_0_0_0 = blocks.vector_source_f(right, True, 1, [])
        self.blocks_vector_source_x_0_0_0_0 = blocks.vector_source_f(right, True, 1, [])
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_f(left, True, 1, [])
        self.blocks_sub_xx_0_0_1 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_0_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_float*1, int(samp_rate/keep))
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, columns)
        self.blocks_repeat_0_0_0_0_2 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_repeat_0_0_0_0_1_0 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_repeat_0_0_0_0_1 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_repeat_0_0_0_0_0_1_0 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_repeat_0_0_0_0_0_1 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_repeat_0_0_0_0_0_0 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_repeat_0_0_0_0_0 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_repeat_0_0_0_0 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_gr_complex*columns, columns)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, columns)
        self.blocks_min_xx_0 = blocks.min_ff(int(samp_rate/keep),1)
        self.blocks_max_xx_0 = blocks.max_ff(int(samp_rate/keep), 1)
        self.blocks_magphase_to_complex_0_0_0_0_1 = blocks.magphase_to_complex(1)
        self.blocks_magphase_to_complex_0_0_0_0_0_0 = blocks.magphase_to_complex(1)
        self.blocks_magphase_to_complex_0_0_0_0_0 = blocks.magphase_to_complex(1)
        self.blocks_magphase_to_complex_0_0_0_0 = blocks.magphase_to_complex(1)
        self.blocks_keep_one_in_n_0_2 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, keep)
        self.blocks_keep_one_in_n_0_1 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, keep)
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, keep)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, keep)
        self.blocks_float_to_short_0_1_0 = blocks.float_to_short(1, scale)
        self.blocks_complex_to_magphase_0_0_0_1 = blocks.complex_to_magphase(1)
        self.blocks_complex_to_magphase_0_0_0_0_0 = blocks.complex_to_magphase(1)
        self.blocks_complex_to_magphase_0_0_0_0 = blocks.complex_to_magphase(1)
        self.blocks_complex_to_magphase_0_0_0 = blocks.complex_to_magphase(1)
        self.blocks_complex_to_mag_squared_0_1 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_pwr_squelch_xx_0_1 = analog.pwr_squelch_cc(-60, 1e-4, 0, False)
        self.analog_pwr_squelch_xx_0_0_0 = analog.pwr_squelch_cc(-60, 1e-4, 0, False)
        self.analog_pwr_squelch_xx_0_0 = analog.pwr_squelch_cc(-60, 1e-4, 0, False)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-60, 1e-4, 0, False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0_0_0, 0), (self.blocks_keep_one_in_n_0_1, 0))
        self.connect((self.analog_pwr_squelch_xx_0_1, 0), (self.blocks_keep_one_in_n_0_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_complex_to_mag_squared_0_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_time_raster_sink_x_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.qtgui_time_raster_sink_x_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_1, 0), (self.blocks_float_to_short_0_1_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_1, 0), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0, 0), (self.blocks_repeat_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0, 1), (self.blocks_repeat_0_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0_0, 1), (self.blocks_repeat_0_0_0_0_0_1, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0_0, 0), (self.blocks_repeat_0_0_0_0_1, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0_0_0, 1), (self.blocks_repeat_0_0_0_0_0_1_0, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0_0_0, 0), (self.blocks_repeat_0_0_0_0_1_0, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0_1, 1), (self.blocks_repeat_0_0_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0_1, 0), (self.blocks_repeat_0_0_0_0_2, 0))
        self.connect((self.blocks_float_to_short_0_1_0, 0), (self.video_sdl_sink_1_1_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_complex_to_magphase_0_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.blocks_complex_to_magphase_0_0_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_1, 0), (self.blocks_complex_to_magphase_0_0_0_1, 0))
        self.connect((self.blocks_keep_one_in_n_0_2, 0), (self.blocks_complex_to_magphase_0_0_0_0_0, 0))
        self.connect((self.blocks_magphase_to_complex_0_0_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_magphase_to_complex_0_0_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_magphase_to_complex_0_0_0_0_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_magphase_to_complex_0_0_0_0_1, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.blocks_probe_signal_x_0, 0))
        self.connect((self.blocks_min_xx_0, 0), (self.blocks_probe_signal_x_0_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_repeat_0_0_0_0, 0), (self.blocks_magphase_to_complex_0_0_0_0, 0))
        self.connect((self.blocks_repeat_0_0_0_0_0, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_repeat_0_0_0_0_0_0, 0), (self.blocks_sub_xx_0_0_1, 0))
        self.connect((self.blocks_repeat_0_0_0_0_0_1, 0), (self.blocks_sub_xx_0_0_0, 0))
        self.connect((self.blocks_repeat_0_0_0_0_0_1_0, 0), (self.blocks_sub_xx_0_0_0_0, 0))
        self.connect((self.blocks_repeat_0_0_0_0_1, 0), (self.blocks_magphase_to_complex_0_0_0_0_0, 0))
        self.connect((self.blocks_repeat_0_0_0_0_1_0, 0), (self.blocks_magphase_to_complex_0_0_0_0_0_0, 0))
        self.connect((self.blocks_repeat_0_0_0_0_2, 0), (self.blocks_magphase_to_complex_0_0_0_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_repeat_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.blocks_max_xx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.blocks_min_xx_0, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.blocks_magphase_to_complex_0_0_0_0, 1))
        self.connect((self.blocks_sub_xx_0_0_0, 0), (self.blocks_magphase_to_complex_0_0_0_0_0, 1))
        self.connect((self.blocks_sub_xx_0_0_0_0, 0), (self.blocks_magphase_to_complex_0_0_0_0_0_0, 1))
        self.connect((self.blocks_sub_xx_0_0_1, 0), (self.blocks_magphase_to_complex_0_0_0_0_1, 1))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_vector_source_x_0_0_0_0, 0), (self.blocks_sub_xx_0_0_0, 1))
        self.connect((self.blocks_vector_source_x_0_0_0_0_0, 0), (self.blocks_sub_xx_0_0_0_0, 1))
        self.connect((self.blocks_vector_source_x_0_0_0_1, 0), (self.blocks_sub_xx_0_0_1, 1))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.uhd_usrp_source_0, 1), (self.analog_pwr_squelch_xx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.analog_pwr_squelch_xx_0_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.analog_pwr_squelch_xx_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 1), (self.analog_pwr_squelch_xx_0_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "twodimension_usrp_b210s")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_maxtheta(self):
        return self.maxtheta

    def set_maxtheta(self, maxtheta):
        self.maxtheta = maxtheta
        self.set_shiftarrL(np.radians(np.linspace(start=self.maxtheta, stop=0, num=int(self.columns/2), endpoint=False)))

    def get_columns(self):
        return self.columns

    def set_columns(self, columns):
        self.columns = columns
        self.set_left(np.pad(self.shiftarrL, (0, int(self.columns/2)), 'constant'))
        self.set_shiftarrL(np.radians(np.linspace(start=self.maxtheta, stop=0, num=int(self.columns/2), endpoint=False)))
        self.blocks_repeat_0.set_interpolation(self.columns)
        self.blocks_repeat_0_0.set_interpolation(self.columns)
        self.blocks_repeat_0_0_0_0.set_interpolation(self.columns)
        self.blocks_repeat_0_0_0_0_0.set_interpolation(self.columns)
        self.blocks_repeat_0_0_0_0_0_0.set_interpolation(self.columns)
        self.blocks_repeat_0_0_0_0_0_1.set_interpolation(self.columns)
        self.blocks_repeat_0_0_0_0_0_1_0.set_interpolation(self.columns)
        self.blocks_repeat_0_0_0_0_1.set_interpolation(self.columns)
        self.blocks_repeat_0_0_0_0_1_0.set_interpolation(self.columns)
        self.blocks_repeat_0_0_0_0_2.set_interpolation(self.columns)
        self.qtgui_time_raster_sink_x_0.set_num_rows(self.columns)
        self.qtgui_time_raster_sink_x_0.set_num_cols(self.columns)
        self.qtgui_time_raster_sink_x_0_0.set_num_rows(self.columns)
        self.qtgui_time_raster_sink_x_0_0.set_num_cols(self.columns)

    def get_shiftarrL(self):
        return self.shiftarrL

    def set_shiftarrL(self, shiftarrL):
        self.shiftarrL = shiftarrL
        self.set_left(np.pad(self.shiftarrL, (0, int(self.columns/2)), 'constant'))

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left
        self.set_right(np.flip(self.left, axis=0))
        self.set_variable_qtgui_label_0_0(self._variable_qtgui_label_0_0_formatter(self.left))
        self.blocks_vector_source_x_0_0_0.set_data(self.left, [])
        self.blocks_vector_source_x_0_0_0_1.set_data(self.left, [])

    def get_variable_function_probe_0_0(self):
        return self.variable_function_probe_0_0

    def set_variable_function_probe_0_0(self, variable_function_probe_0_0):
        self.variable_function_probe_0_0 = variable_function_probe_0_0
        self.set_variable_qtgui_label_0_0_0_0(self._variable_qtgui_label_0_0_0_0_formatter(self.variable_function_probe_0_0))

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0
        self.set_variable_qtgui_label_0_0_0(self._variable_qtgui_label_0_0_0_formatter(self.variable_function_probe_0))

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.right))
        self.blocks_vector_source_x_0_0_0_0.set_data(self.right, [])
        self.blocks_vector_source_x_0_0_0_0_0.set_data(self.right, [])

    def get_variable_qtgui_label_0_0_0_0(self):
        return self.variable_qtgui_label_0_0_0_0

    def set_variable_qtgui_label_0_0_0_0(self, variable_qtgui_label_0_0_0_0):
        self.variable_qtgui_label_0_0_0_0 = variable_qtgui_label_0_0_0_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_0_0_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_0_0_0))

    def get_variable_qtgui_label_0_0_0(self):
        return self.variable_qtgui_label_0_0_0

    def set_variable_qtgui_label_0_0_0(self, variable_qtgui_label_0_0_0):
        self.variable_qtgui_label_0_0_0 = variable_qtgui_label_0_0_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_0_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_0_0))

    def get_variable_qtgui_label_0_0(self):
        return self.variable_qtgui_label_0_0

    def set_variable_qtgui_label_0_0(self, variable_qtgui_label_0_0):
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_0))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold

    def get_scale(self):
        return self.scale

    def set_scale(self, scale):
        self.scale = scale
        self.blocks_float_to_short_0_1_0.set_scale(self.scale)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)

    def get_minmag(self):
        return self.minmag

    def set_minmag(self, minmag):
        self.minmag = minmag

    def get_maxmag(self):
        return self.maxmag

    def set_maxmag(self, maxmag):
        self.maxmag = maxmag

    def get_keep(self):
        return self.keep

    def set_keep(self, keep):
        self.keep = keep
        self.blocks_keep_one_in_n_0.set_n(self.keep)
        self.blocks_keep_one_in_n_0_0.set_n(self.keep)
        self.blocks_keep_one_in_n_0_1.set_n(self.keep)
        self.blocks_keep_one_in_n_0_2.set_n(self.keep)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0.set_gain(self.gain, 0)
        self.uhd_usrp_source_0.set_gain(self.gain, 1)
        self.uhd_usrp_source_0_0.set_gain(self.gain, 0)
        self.uhd_usrp_source_0_0.set_gain(self.gain, 1)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.freq, 1)
        self.uhd_usrp_source_0_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0_0.set_center_freq(self.freq, 1)

    def get_displayscale(self):
        return self.displayscale

    def set_displayscale(self, displayscale):
        self.displayscale = displayscale





def main(top_block_cls=twodimension_usrp_b210s, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print("Error: failed to enable real-time scheduling.")

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()

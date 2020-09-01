#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: onedimension_simulation
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
from gnuradio import video_sdl
from gnuradio.qtgui import Range, RangeWidget
import math
import numpy as np
import time
import threading

from gnuradio import qtgui

class onedimension_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "onedimension_simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("onedimension_simulation")
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

        self.settings = Qt.QSettings("GNU Radio", "onedimension_simulation")

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
        self.variable_function_probe_0_0 = variable_function_probe_0_0 = 0
        self.variable_function_probe_0 = variable_function_probe_0 = 1
        self.left = left = np.pad(shiftarrL, (0, int(columns/2)), 'constant')
        self.degreesTXR = degreesTXR = 0
        self.degreesTXL = degreesTXL = 0
        self.variable_qtgui_label_0_0_0 = variable_qtgui_label_0_0_0 = variable_function_probe_0_0
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0 = variable_function_probe_0
        self.scale = scale = 55
        self.samp_rate = samp_rate = 64000
        self.rows = rows = 100
        self.right = right = np.flip(left, axis=0)
        self.angle_radiansStartR = angle_radiansStartR = (math.pi/180) * degreesTXR
        self.angle_radiansStartL = angle_radiansStartL = (math.pi/180) * degreesTXL

        ##################################################
        # Blocks
        ##################################################
        self._scale_range = Range(0, 100, 5, 55, 200)
        self._scale_win = RangeWidget(self._scale_range, self.set_scale, 'scale', "counter_slider", float)
        self.top_grid_layout.addWidget(self._scale_win)
        self.blocks_probe_signal_x_0_0 = blocks.probe_signal_f()
        self.blocks_probe_signal_x_0 = blocks.probe_signal_f()
        self.video_sdl_sink_1 = video_sdl.sink_s(0, columns, rows, 0, columns*6, rows*6)
        self._variable_qtgui_label_0_0_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_0_0_formatter = None
        else:
            self._variable_qtgui_label_0_0_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_0_0_tool_bar.addWidget(Qt.QLabel('Probe Signal Min' + ": "))
        self._variable_qtgui_label_0_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_0_formatter(self.variable_qtgui_label_0_0_0)))
        self._variable_qtgui_label_0_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_0_0_tool_bar)
        self._variable_qtgui_label_0_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_0_formatter = None
        else:
            self._variable_qtgui_label_0_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_0_tool_bar.addWidget(Qt.QLabel('Probe Signal Max' + ": "))
        self._variable_qtgui_label_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_formatter(self.variable_qtgui_label_0_0)))
        self._variable_qtgui_label_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_0_tool_bar)
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

        self.qtgui_time_raster_sink_x_0 = qtgui.time_raster_sink_f(
            samp_rate,
            columns,
            rows,
            [],
            [],
            "",
            1
        )

        self.qtgui_time_raster_sink_x_0.set_update_time(0.01)
        self.qtgui_time_raster_sink_x_0.set_intensity_range(0, 5)
        self.qtgui_time_raster_sink_x_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [1, 1, 0, 0, 0,
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
        self.top_grid_layout.addWidget(self._qtgui_time_raster_sink_x_0_win)
        self._degreesTXR_range = Range(0, maxtheta/2, 5, 0, 200)
        self._degreesTXR_win = RangeWidget(self._degreesTXR_range, self.set_degreesTXR, 'degreesTXR', "counter_slider", float)
        self.top_grid_layout.addWidget(self._degreesTXR_win)
        self._degreesTXL_range = Range(0, maxtheta/2, 5, 0, 200)
        self._degreesTXL_win = RangeWidget(self._degreesTXL_range, self.set_degreesTXL, 'degreesTXL', "counter_slider", float)
        self.top_grid_layout.addWidget(self._degreesTXL_win)
        self.blocks_vector_source_x_0_0_0_0 = blocks.vector_source_f(right, True, 1, [])
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_f(left, True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_sub_xx_0_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_float*1, samp_rate)
        self.blocks_repeat_0_0_0_0_1 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_repeat_0_0_0_0_0_1 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_repeat_0_0_0_0_0 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_repeat_0_0_0_0 = blocks.repeat(gr.sizeof_float*1, columns)
        self.blocks_multiply_const_vxx_0_0_1 = blocks.multiply_const_cc(complex(math.cos(angle_radiansStartR),math.sin(angle_radiansStartR)))
        self.blocks_multiply_const_vxx_0_0_0_0 = blocks.multiply_const_cc(complex(math.cos(angle_radiansStartL),math.sin(angle_radiansStartL)))
        self.blocks_min_xx_0 = blocks.min_ff(samp_rate,1)
        self.blocks_max_xx_0 = blocks.max_ff(samp_rate, 1)
        self.blocks_magphase_to_complex_0_0_0_0_0 = blocks.magphase_to_complex(1)
        self.blocks_magphase_to_complex_0_0_0_0 = blocks.magphase_to_complex(1)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, scale)
        self.blocks_complex_to_magphase_0_0_0_0 = blocks.complex_to_magphase(1)
        self.blocks_complex_to_magphase_0_0_0 = blocks.complex_to_magphase(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1e3, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_time_raster_sink_x_0, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0, 0), (self.blocks_repeat_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0, 1), (self.blocks_repeat_0_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0_0, 1), (self.blocks_repeat_0_0_0_0_0_1, 0))
        self.connect((self.blocks_complex_to_magphase_0_0_0_0, 0), (self.blocks_repeat_0_0_0_0_1, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.video_sdl_sink_1, 0))
        self.connect((self.blocks_magphase_to_complex_0_0_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_magphase_to_complex_0_0_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_max_xx_0, 0), (self.blocks_probe_signal_x_0, 0))
        self.connect((self.blocks_min_xx_0, 0), (self.blocks_probe_signal_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0, 0), (self.blocks_complex_to_magphase_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.blocks_complex_to_magphase_0_0_0, 0))
        self.connect((self.blocks_repeat_0_0_0_0, 0), (self.blocks_magphase_to_complex_0_0_0_0, 0))
        self.connect((self.blocks_repeat_0_0_0_0_0, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_repeat_0_0_0_0_0_1, 0), (self.blocks_sub_xx_0_0_0, 0))
        self.connect((self.blocks_repeat_0_0_0_0_1, 0), (self.blocks_magphase_to_complex_0_0_0_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.blocks_max_xx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.blocks_min_xx_0, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.blocks_magphase_to_complex_0_0_0_0, 1))
        self.connect((self.blocks_sub_xx_0_0_0, 0), (self.blocks_magphase_to_complex_0_0_0_0_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0_0_1, 0))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_vector_source_x_0_0_0_0, 0), (self.blocks_sub_xx_0_0_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "onedimension_simulation")
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
        self.blocks_repeat_0_0_0_0.set_interpolation(self.columns)
        self.blocks_repeat_0_0_0_0_0.set_interpolation(self.columns)
        self.blocks_repeat_0_0_0_0_0_1.set_interpolation(self.columns)
        self.blocks_repeat_0_0_0_0_1.set_interpolation(self.columns)
        self.qtgui_time_raster_sink_x_0.set_num_rows(self.columns)

    def get_shiftarrL(self):
        return self.shiftarrL

    def set_shiftarrL(self, shiftarrL):
        self.shiftarrL = shiftarrL
        self.set_left(np.pad(self.shiftarrL, (0, int(self.columns/2)), 'constant'))

    def get_variable_function_probe_0_0(self):
        return self.variable_function_probe_0_0

    def set_variable_function_probe_0_0(self, variable_function_probe_0_0):
        self.variable_function_probe_0_0 = variable_function_probe_0_0
        self.set_variable_qtgui_label_0_0_0(self._variable_qtgui_label_0_0_0_formatter(self.variable_function_probe_0_0))

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0
        self.set_variable_qtgui_label_0_0(self._variable_qtgui_label_0_0_formatter(self.variable_function_probe_0))

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left
        self.set_right(np.flip(self.left, axis=0))
        self.blocks_vector_source_x_0_0_0.set_data(self.left, [])

    def get_degreesTXR(self):
        return self.degreesTXR

    def set_degreesTXR(self, degreesTXR):
        self.degreesTXR = degreesTXR
        self.set_angle_radiansStartR((math.pi/180) * self.degreesTXR)

    def get_degreesTXL(self):
        return self.degreesTXL

    def set_degreesTXL(self, degreesTXL):
        self.degreesTXL = degreesTXL
        self.set_angle_radiansStartL((math.pi/180) * self.degreesTXL)

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

    def get_scale(self):
        return self.scale

    def set_scale(self, scale):
        self.scale = scale
        self.blocks_float_to_short_0.set_scale(self.scale)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rows(self):
        return self.rows

    def set_rows(self, rows):
        self.rows = rows
        self.qtgui_time_raster_sink_x_0.set_num_cols(self.rows)

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right
        self.blocks_vector_source_x_0_0_0_0.set_data(self.right, [])

    def get_angle_radiansStartR(self):
        return self.angle_radiansStartR

    def set_angle_radiansStartR(self, angle_radiansStartR):
        self.angle_radiansStartR = angle_radiansStartR
        self.blocks_multiply_const_vxx_0_0_1.set_k(complex(math.cos(self.angle_radiansStartR),math.sin(self.angle_radiansStartR)))

    def get_angle_radiansStartL(self):
        return self.angle_radiansStartL

    def set_angle_radiansStartL(self, angle_radiansStartL):
        self.angle_radiansStartL = angle_radiansStartL
        self.blocks_multiply_const_vxx_0_0_0_0.set_k(complex(math.cos(self.angle_radiansStartL),math.sin(self.angle_radiansStartL)))





def main(top_block_cls=onedimension_simulation, options=None):
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

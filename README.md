# Seeing Signals

> This is a work-in-progress.

This repository contains the GNU Radio flowgraphs for the GRCon 2020 lightning talk 'Seeing Signals: Real-Time Visualization of A Delay-and-Sum Beamformer'. The flowgraph simulations and demonstrations show how 2D visualization of magnitudes and direction of arrival can be generated from phased arrays using a delay-and-sum beamformer. By using raster plots it’s possible to view both direction of arrival and magnitude for all steering weights simultaneously. This is a simple approach to recieve-only beamforming. 

I suggest that you start with the simulations. They should work in GNU Radio >= 3.8.2 and the main (3.9) branch. If you are using 3.8.1 or earlier, there's a bug with QT message ports so the simulations won't run (you'll see an error in the QT range blocks). Please do consider updating GNU Radio if that's the case. If you're on a Mac, the Video SDL Sink does not work properly. You can get around this by disabling the blocks.

The `grcon` folder includes the presentation slides, flowgraph simulations, flowgraphs for demos with USRP B210s, and screen captures of the flowgraphs. 

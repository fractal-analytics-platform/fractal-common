# Fractal Common

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Fractal is a framework to process high-content imaging data at scale and prepare it for interactive visualization.

![Fractal_Overview](https://fractal-analytics-platform.github.io/assets/fractal_overview.jpg)

Fractal provides distributed workflows that convert TBs of image data into OME-Zarr files. The platform then processes the 3D image data by applying tasks like illumination correction, maximum intensity projection, 3D segmentation using [cellpose](https://cellpose.readthedocs.io/en/latest/) and measurements using [napari workflows](https://github.com/haesleinhuepf/napari-workflows). The pyramidal OME-Zarr files enable interactive visualization in the napari viewer.

This is the **common repository**, containing resources that are shared by the server and client components. Find more information about Fractal in general and the other repositories at the [Fractal home page](https://fractal-analytics-platform.github.io).

**IMPORTANT: This repository must only be used as a git submodule.**

# Contributors and license

Unless otherwise stated in each individual module, all Fractal components are released according to a BSD 3-Clause License, and Copyright is with Friedrich Miescher Institute for Biomedical Research and University of Zurich.

Fractal was conceived in the Liberali Lab at the Friedrich Miescher Institute for Biomedical Research and in the Pelkmans Lab at the University of Zurich (both in Switzerland). The project lead is with [@gusqgm](https://github.com/gusqgm) & [@jluethi](https://github.com/jluethi). The core development is done under contract by [@mfranzon](https://github.com/mfranzon), [@tcompa](https://github.com/tcompa) & [@jacopo-exact](https://github.com/jacopo-exact) from [eXact lab S.r.l.](exact-lab.it).

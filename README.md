# FlyPAD

This repository contains the necessary software to acquire data with the [Harp FlyPAD](https://github.com/fchampalimaud/device.flypad) device.

> [!WARNING]
> This project only supports Windows.

## Installation
1. Download or clone the repository.
2. Run the `Setup.cmd` script.
3. That's it!

## Usage
1. Run the `Run.cmd` to open Bonsai.
2. Change the serial port to the one that corresponds to the Harp FlyPAD (e.g. `COM8`).
3. Click on the `Start` button or press `F5` to start the workflow.
4. That's basically it!

> [!NOTE]
> The output from the Harp FlyPAD is saved in the `output` directory, in which each subdirectory corresponds to a different session (identified by date and time). Each session directory contains all of the device's logs as well as the device metadata.
>
> When Bonsai is closed, a small Python script is executed which converts the raw capacitance data to the file format saved by the old acquisition system. The name of this file is `FlyPAD_33_12bits.bin`.

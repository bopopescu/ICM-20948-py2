#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""ICM-20948: Low power 9-axis MotionTracking device that is ideally suited for Smartphones, Tablets, Wearable Sensors, and IoT applications."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["TDK Invensense"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

class REG:
	SELF_TEST_X_GYRO = 2
	SELF_TEST_Y_GYRO = 3
	SELF_TEST_Z_GYRO = 4
	SELF_TEST_X_ACCEL = 14
	SELF_TEST_Y_ACCEL = 15
	SELF_TEST_Z_ACCEL = 16
	XA_OFFS_H = 20
	XA_OFFS_L = 21
	YA_OFFS_H = 23
	YA_OFFS_L = 24
	ZA_OFFS_H = 26
	ZA_OFFS_L = 27
	TIMEBASE_CORRECTION_PLL = 40
	REG_BANK_SEL = 127

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
	GYRO_SMPLRT_DIV = 0
	GYRO_CONFIG_1 = 1
	GYRO_CONFIG_2 = 2
	XG_OFFS_USRH = 3
	XG_OFFS_USRL = 4
	YG_OFFS_USRH = 5
	YG_OFFS_USRL = 6
	ZG_OFFS_USRH = 7
	ZG_OFFS_USRL = 8
	ODR_ALIGN_EN = 9
	ACCEL_SMPLRT_DIV_1 = 16
	ACCEL_SMPLRT_DIV_2 = 17
	ACCEL_INTEL_CTRL = 18
	ACCEL_WOM_THR = 19
	ACCEL_CONFIG = 20
	ACCEL_CONFIG_2 = 21
	FSYNC_CONFIG = 82
	TEMP_CONFIG = 83
	MOD_CTRL_USR = 84
	REG_BANK_SEL = 127

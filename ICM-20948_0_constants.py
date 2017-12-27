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
	WHO_AM_I = 0
	USER_CTRL = 3
	LP_CONFIG = 5
	PWR_MGMT_1 = 6
	PWR_MGMT_2 = 7
	INT_PIN_CFG = 15
	INT_ENABLE = 16
	INT_ENABLE_1 = 17
	INT_ENABLE_2 = 18
	INT_ENABLE_3 = 19
	I2C_MST_STATUS = 23
	INT_STATUS = 25
	INT_STATUS_1 = 26
	INT_STATUS_2 = 27
	INT_STATUS_3 = 28
	DELAY_TIMEH = 40
	DELAY_TIMEL = 41
	ACCEL_XOUT_H = 45
	ACCEL_XOUT_L = 46
	ACCEL_YOUT_H = 47
	ACCEL_YOUT_L = 48
	ACCEL_ZOUT_H = 49
	ACCEL_ZOUT_L = 50
	GYRO_XOUT_H = 51
	GYRO_XOUT_L = 52
	GYRO_YOUT_H = 53
	GYRO_YOUT_L = 54
	GYRO_ZOUT_H = 55
	GYRO_ZOUT_L = 56
	TEMP_OUT_H = 57
	TEMP_OUT_L = 58
	EXT_SLV_SENS_DATA_00 = 59
	EXT_SLV_SENS_DATA_01 = 60
	EXT_SLV_SENS_DATA_02 = 61
	EXT_SLV_SENS_DATA_03 = 62
	EXT_SLV_SENS_DATA_04 = 63
	EXT_SLV_SENS_DATA_05 = 64
	EXT_SLV_SENS_DATA_06 = 65
	EXT_SLV_SENS_DATA_07 = 66
	EXT_SLV_SENS_DATA_08 = 67
	EXT_SLV_SENS_DATA_09 = 68
	EXT_SLV_SENS_DATA_10 = 69
	EXT_SLV_SENS_DATA_11 = 70
	EXT_SLV_SENS_DATA_12 = 71
	EXT_SLV_SENS_DATA_13 = 72
	EXT_SLV_SENS_DATA_14 = 73
	EXT_SLV_SENS_DATA_15 = 74
	EXT_SLV_SENS_DATA_16 = 75
	EXT_SLV_SENS_DATA_17 = 76
	EXT_SLV_SENS_DATA_18 = 77
	EXT_SLV_SENS_DATA_19 = 78
	EXT_SLV_SENS_DATA_20 = 79
	EXT_SLV_SENS_DATA_21 = 80
	EXT_SLV_SENS_DATA_22 = 81
	EXT_SLV_SENS_DATA_23 = 82
	FIFO_EN_1 = 102
	FIFO_EN_2 = 103
	FIFO_RST = 104
	FIFO_MODE = 105
	FIFO_COUNTH = 112
	FIFO_COUNTL = 113
	FIFO_R_W = 114
	DATA_RDY_STATUS = 116
	FIFO_CFG = 118
	REG_BANK_SEL = 127
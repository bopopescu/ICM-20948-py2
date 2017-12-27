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
	I2C_MST_ODR_CONFIG = 0
	I2C_MST_CTRL = 1
	I2C_MST_DELAY_CTRL = 2
	I2C_SLV0_ADDR = 3
	I2C_SLV0_REG = 4
	I2C_SLV0_CTRL = 5
	I2C_SLV0_DO = 6
	I2C_SLV1_ADDR = 7
	I2C_SLV1_REG = 8
	I2C_SLV1_CTRL = 9
	I2C_SLV1_DO = 10
	I2C_SLV2_ADDR = 11
	I2C_SLV2_REG = 12
	I2C_SLV2_CTRL = 13
	I2C_SLV2_DO = 14
	I2C_SLV3_ADDR = 15
	I2C_SLV3_REG = 16
	I2C_SLV3_CTRL = 17
	I2C_SLV3_DO = 18
	I2C_SLV4_ADDR = 19
	I2C_SLV4_REG = 20
	I2C_SLV4_CTRL = 21
	I2C_SLV4_DO = 22
	I2C_SLV4_DI = 23
	REG_BANK_SEL = 127

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

from ICM_20948_constants import *

# name:        ICM-20948
# description: Low power 9-axis MotionTracking device that is ideally suited for Smartphones, Tablets, Wearable Sensors, and IoT applications.
# manuf:       TDK Invensense
# version:     0.1
# url:         https://www.invensense.com/wp-content/uploads/2016/06/DS-000189-ICM-20948-v1.3.pdf
# date:        2017-10-18


# Derive from this class and implement read and write
class ICM_20948_Base:
	"""Low power 9-axis MotionTracking device that is ideally suited for Smartphones, Tablets, Wearable Sensors, and IoT applications."""
	# Register GYRO_SMPLRT_DIV
	# type USR2, bank 2 
	
	def setGYRO_SMPLRT_DIV(self, val):
		"""Set register GYRO_SMPLRT_DIV"""
		self.write(REG.GYRO_SMPLRT_DIV, val, 8)
	
	def getGYRO_SMPLRT_DIV(self):
		"""Get register GYRO_SMPLRT_DIV"""
		return self.read(REG.GYRO_SMPLRT_DIV, 8)
	
	# Bits GYRO_SMPLRT_DIV
	# Gyro sample rate divider. Divides the internal sample rate to generate the sample
	#           rate that controls sensor data output rate, FIFO sample rate, and DMP sequence rate.
	#           NOTE: This register is only effective when FCHOICE = 1’b1 (FCHOICE_B register bit is 1’b0), and
	#           (0 < DLPF_CFG < 7).
	#           ODR is computed as follows:
	#           1.1 kHz/(1+GYRO_SMPLRT_DIV[7:0]) 
	
	# Register GYRO_CONFIG_1
	# type USR2, bank 2 
	# The gyroscope DLPF is configured by GYRO_DLPFCFG, when GYRO_FCHOICE = 1. The gyroscope data is filtered
	# according to the value of GYRO_DLPFCFG and GYRO_FCHOICE as shown in Table 16. 
	
	
	def setGYRO_CONFIG_1(self, val):
		"""Set register GYRO_CONFIG_1"""
		self.write(REG.GYRO_CONFIG_1, val, 8)
	
	def getGYRO_CONFIG_1(self):
		"""Get register GYRO_CONFIG_1"""
		return self.read(REG.GYRO_CONFIG_1, 8)
	
	# Bits reserved_0
	# Bits GYRO_DLPFCFG
	# Gyro low pass filter configuration as shown in Table 16. 
	# Bits GYRO_FS_SEL
	# Gyro Full Scale Select:
	#           00 = ±250 dps
	#           01= ±500 dps
	#           10 = ±1000 dps
	#           11 = ±2000 dps 
	
	# Bits GYRO_FCHOICE
	# 0 - Bypass gyro DLPF.
	#           1 - Enable gyro DLPF. 
	
	# Register GYRO_CONFIG_2
	# type USR2, bank 2 
	
	def setGYRO_CONFIG_2(self, val):
		"""Set register GYRO_CONFIG_2"""
		self.write(REG.GYRO_CONFIG_2, val, 8)
	
	def getGYRO_CONFIG_2(self):
		"""Get register GYRO_CONFIG_2"""
		return self.read(REG.GYRO_CONFIG_2, 8)
	
	# Bits reserved_0
	# Bits XGYRO_CTEN
	# X Gyro self-test enable. 
	# Bits YGYRO_CTEN
	# Y Gyro self-test enable. 
	# Bits ZGYRO_CTEN
	# Z Gyro self-test enable. 
	# Bits GYRO_AVGCFG
	# Averaging filter configuration settings for low-power mode.
	#           0: 1x averaging.
	#           1: 2x averaging.
	#           2: 4x averaging.
	#           3: 8x averaging.
	#           4: 16x averaging.
	#           5: 32x averaging.
	#           6: 64x averaging.
	#           7: 128x averaging. 
	
	# Register XG_OFFS_USRH
	# type USR2, bank 2 
	
	def setXG_OFFS_USRH(self, val):
		"""Set register XG_OFFS_USRH"""
		self.write(REG.XG_OFFS_USRH, val, 8)
	
	def getXG_OFFS_USRH(self):
		"""Get register XG_OFFS_USRH"""
		return self.read(REG.XG_OFFS_USRH, 8)
	
	# Bits X_OFFS_USER
	# Upper byte of X gyro offset cancellation. 
	# Register XG_OFFS_USRL
	# type USR2, bank 2 
	
	def setXG_OFFS_USRL(self, val):
		"""Set register XG_OFFS_USRL"""
		self.write(REG.XG_OFFS_USRL, val, 8)
	
	def getXG_OFFS_USRL(self):
		"""Get register XG_OFFS_USRL"""
		return self.read(REG.XG_OFFS_USRL, 8)
	
	# Bits X_OFFS_USER
	# Lower byte of X gyro offset cancellation. 
	# Register YG_OFFS_USRH
	# type USR2, bank 2 
	
	def setYG_OFFS_USRH(self, val):
		"""Set register YG_OFFS_USRH"""
		self.write(REG.YG_OFFS_USRH, val, 8)
	
	def getYG_OFFS_USRH(self):
		"""Get register YG_OFFS_USRH"""
		return self.read(REG.YG_OFFS_USRH, 8)
	
	# Bits Y_OFFS_USER
	# Upper byte of Y gyro offset cancellation. 
	# Register YG_OFFS_USRL
	# type USR2, bank 2 
	
	def setYG_OFFS_USRL(self, val):
		"""Set register YG_OFFS_USRL"""
		self.write(REG.YG_OFFS_USRL, val, 8)
	
	def getYG_OFFS_USRL(self):
		"""Get register YG_OFFS_USRL"""
		return self.read(REG.YG_OFFS_USRL, 8)
	
	# Bits Y_OFFS_USER
	# Lower byte of Y gyro offset cancellation. 
	# Register ZG_OFFS_USRH
	# type USR2, bank 2 
	
	def setZG_OFFS_USRH(self, val):
		"""Set register ZG_OFFS_USRH"""
		self.write(REG.ZG_OFFS_USRH, val, 8)
	
	def getZG_OFFS_USRH(self):
		"""Get register ZG_OFFS_USRH"""
		return self.read(REG.ZG_OFFS_USRH, 8)
	
	# Bits Z_OFFS_USER
	# Upper byte of Z gyro offset cancellation. 
	# Register ZG_OFFS_USRL
	# type USR2, bank 2 
	
	def setZG_OFFS_USRL(self, val):
		"""Set register ZG_OFFS_USRL"""
		self.write(REG.ZG_OFFS_USRL, val, 8)
	
	def getZG_OFFS_USRL(self):
		"""Get register ZG_OFFS_USRL"""
		return self.read(REG.ZG_OFFS_USRL, 8)
	
	# Bits Z_OFFS_USER
	# Lower byte of Z gyro offset cancellation. 
	# Register ODR_ALIGN_EN
	# type USR2, bank 2, OTP No 
	
	def setODR_ALIGN_EN(self, val):
		"""Set register ODR_ALIGN_EN"""
		self.write(REG.ODR_ALIGN_EN, val, 8)
	
	def getODR_ALIGN_EN(self):
		"""Get register ODR_ALIGN_EN"""
		return self.read(REG.ODR_ALIGN_EN, 8)
	
	# Bits reserved_0
	# Bits ODR_ALIGN_EN
	# 0: Disables ODR start-time alignment.
	#           1: Enables ODR start-time alignment when any of the following registers is written
	#           (with the same value or with different values):  GYRO_SMPLRT_DIV,
	#           ACCEL_SMPLRT_DIV_1, ACCEL_SMPLRT_DIV_2, I2C_MST_ODR_CONFIG. 
	
	# Register ACCEL_SMPLRT_DIV_1
	# type USR2, bank 2 
	
	def setACCEL_SMPLRT_DIV_1(self, val):
		"""Set register ACCEL_SMPLRT_DIV_1"""
		self.write(REG.ACCEL_SMPLRT_DIV_1, val, 8)
	
	def getACCEL_SMPLRT_DIV_1(self):
		"""Get register ACCEL_SMPLRT_DIV_1"""
		return self.read(REG.ACCEL_SMPLRT_DIV_1, 8)
	
	# Bits reserved_0
	# Bits ACCEL_SMPLRT_DIV
	# MSB for ACCEL sample rate div. 
	# Register ACCEL_SMPLRT_DIV_2
	# type USR2, bank 2 
	
	def setACCEL_SMPLRT_DIV_2(self, val):
		"""Set register ACCEL_SMPLRT_DIV_2"""
		self.write(REG.ACCEL_SMPLRT_DIV_2, val, 8)
	
	def getACCEL_SMPLRT_DIV_2(self):
		"""Get register ACCEL_SMPLRT_DIV_2"""
		return self.read(REG.ACCEL_SMPLRT_DIV_2, 8)
	
	# Bits ACCEL_SMPLRT_DIV
	# LSB for ACCEL sample rate div.
	#           ODR is computed as follows:
	#           1.125 kHz/(1+ACCEL_SMPLRT_DIV[11:0]) 
	
	# Register ACCEL_INTEL_CTRL
	# type USR2, bank 2 
	
	def setACCEL_INTEL_CTRL(self, val):
		"""Set register ACCEL_INTEL_CTRL"""
		self.write(REG.ACCEL_INTEL_CTRL, val, 8)
	
	def getACCEL_INTEL_CTRL(self):
		"""Get register ACCEL_INTEL_CTRL"""
		return self.read(REG.ACCEL_INTEL_CTRL, 8)
	
	# Bits reserved_0
	# Bits ACCEL_INTEL_EN
	# Enable the WOM logic. 
	# Bits ACCEL_INTEL_MODE_INT
	# Selects WOM algorithm.
	#           1 = Compare the current sample with the previous sample.
	#           0 = Initial sample is stored, all future samples are compared to the initial sample. 
	
	# Register ACCEL_WOM_THR
	# type USR2, bank 2 
	
	def setACCEL_WOM_THR(self, val):
		"""Set register ACCEL_WOM_THR"""
		self.write(REG.ACCEL_WOM_THR, val, 8)
	
	def getACCEL_WOM_THR(self):
		"""Get register ACCEL_WOM_THR"""
		return self.read(REG.ACCEL_WOM_THR, 8)
	
	# Bits WOM_THRESHOLD
	# This register holds the threshold value for the Wake on Motion Interrupt for ACCEL
	#           x/y/z axes. LSB = 4 mg. Range is 0 mg to 1020 mg. 
	
	# Register ACCEL_CONFIG
	# type USR2, bank 2 
	# The data rate out of the DLPF filter block can be further reduced by a factor of
	# 1.125 kHz/(1+ACCEL_SMPLRT_DIV[11:0]) where ACCEL_SMPLRT_DIV is a 12-bit integer. 
	
	
	def setACCEL_CONFIG(self, val):
		"""Set register ACCEL_CONFIG"""
		self.write(REG.ACCEL_CONFIG, val, 8)
	
	def getACCEL_CONFIG(self):
		"""Get register ACCEL_CONFIG"""
		return self.read(REG.ACCEL_CONFIG, 8)
	
	# Bits reserved_0
	# Bits ACCEL_DLPFCFG
	# Accelerometer low pass filter configuration as shown in Table 18. 
	# Bits ACCEL_FS_SEL
	# Accelerometer Full Scale Select:
	#           00: ±2g
	#           01: ±4g
	#           10: ±8g
	#           11: ±16g 
	
	# Bits ACCEL_FCHOICE
	# 0: Bypass accel DLPF.
	#           1: Enable accel DLPF. 
	
	# Register ACCEL_CONFIG_2
	# type USR2, bank 2 
	
	def setACCEL_CONFIG_2(self, val):
		"""Set register ACCEL_CONFIG_2"""
		self.write(REG.ACCEL_CONFIG_2, val, 8)
	
	def getACCEL_CONFIG_2(self):
		"""Get register ACCEL_CONFIG_2"""
		return self.read(REG.ACCEL_CONFIG_2, 8)
	
	# Bits reserved_0
	# Bits AX_ST_EN_REG
	# X Accel self-test enable. 
	# Bits AY_ST_EN_REG
	# Y Accel self-test enable. 
	# Bits AZ_ST_EN_REG
	# Z Accel self-test enable. 
	# Bits DEC3_CFG
	# Controls the number of samples averaged in the accelerometer decimator:
	#           0: Average 1 or 4 samples depending on ACCEL_FCHOICE (see Table 19).
	#           1: Average 8 samples.
	#           2: Average 16 samples.
	#           3: Average 32 samples. 
	
	# Register FSYNC_CONFIG
	# type USR2, bank 2 
	
	def setFSYNC_CONFIG(self, val):
		"""Set register FSYNC_CONFIG"""
		self.write(REG.FSYNC_CONFIG, val, 8)
	
	def getFSYNC_CONFIG(self):
		"""Get register FSYNC_CONFIG"""
		return self.read(REG.FSYNC_CONFIG, 8)
	
	# Bits DELAY_TIME_EN
	# 0: Disables delay time measurement between FSYNC event and the first ODR event
	#           (after FSYNC event).
	#           1: Enables delay time measurement between FSYNC event and the first ODR event
	#           (after FSYNC event). 
	
	# Bits reserved_0
	# Bits WOF_DEGLITCH_EN
	# Enable digital deglitching of FSYNC input for Wake on FSYNC. 
	# Bits WOF_EDGE_INT
	# 0: FSYNC is a level interrupt for Wake on FSYNC.
	#           1: FSYNC is an edge interrupt for Wake on FSYNC.
	#           ACTL_FSYNC is used to set the polarity of the interrupt. 
	
	# Bits EXT_SYNC_SET
	# Enables the FSYNC pin data to be sampled.
	#           EXT_SYNC_SET FSYNC bit location.
	#           0: Function disabled.
	#           1: TEMP_OUT_L[0].
	#           2: GYRO_XOUT_L[0].
	#           3: GYRO_YOUT_L[0].
	#           4: GYRO_ZOUT_L[0].
	#           5: ACCEL_XOUT_L[0].
	#           6: ACCEL_YOUT_L[0].
	#           7: ACCEL_ZOUT_L[0]. 
	
	# Register TEMP_CONFIG
	# type USR2, bank 2 
	
	def setTEMP_CONFIG(self, val):
		"""Set register TEMP_CONFIG"""
		self.write(REG.TEMP_CONFIG, val, 8)
	
	def getTEMP_CONFIG(self):
		"""Get register TEMP_CONFIG"""
		return self.read(REG.TEMP_CONFIG, 8)
	
	# Bits TEMP_DLPFCFG
	# Low pass filter configuration for temperature sensor as shown in the table below:
	#           TEMP_DLPCFG<2:0> TEMP SENSOR
	#           NBW (HZ) RATE (KHZ)
	#           0 7932 9
	#           1 217.9 1.125
	#           2 123.5 1.125
	#           3 65.9 1.125
	#           4 34.1 1.125
	#           5 17.3 1.125
	#           6 8.8 Rate (kHz)
	#           7 7932 9 
	
	# Register MOD_CTRL_USR
	# type USR2, bank 2 
	
	def setMOD_CTRL_USR(self, val):
		"""Set register MOD_CTRL_USR"""
		self.write(REG.MOD_CTRL_USR, val, 8)
	
	def getMOD_CTRL_USR(self):
		"""Get register MOD_CTRL_USR"""
		return self.read(REG.MOD_CTRL_USR, 8)
	
	# Bits reserved_0
	# Bits REG_LP_DMP_EN
	# Enable turning on DMP in Low Power Accelerometer mode. 
	# Register REG_BANK_SEL
	# type USR2, bank 2 
	
	def setREG_BANK_SEL(self, val):
		"""Set register REG_BANK_SEL"""
		self.write(REG.REG_BANK_SEL, val, 8)
	
	def getREG_BANK_SEL(self):
		"""Get register REG_BANK_SEL"""
		return self.read(REG.REG_BANK_SEL, 8)
	
	# Bits reserved_0
	# Bits USER_BANK
	# Use the following values in this bit-field to select a USER BANK.
	#           0: Select USER BANK 0.
	#           1: Select USER BANK 1.
	#           2: Select USER BANK 2.
	#           3: Select USER BANK 3. 
	
	# Bits reserved_1

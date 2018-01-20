#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""ICM-20948: Low power 9-axis MotionTracking device that is ideally suited for Smartphones, Tablets, Wearable Sensors, and IoT applications."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["TDK Invensense"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from ICM_20948_constants import *

# name:        ICM-20948
# description: Low power 9-axis MotionTracking device that is ideally suited for Smartphones, Tablets, Wearable Sensors, and IoT applications.
# manuf:       TDK Invensense
# version:     Version 0.1
# url:         https://www.invensense.com/wp-content/uploads/2016/06/DS-000189-ICM-20948-v1.3.pdf
# date:        2017-10-18


# Derive from this class and implement read and write
class ICM_20948_Base:
	"""Low power 9-axis MotionTracking device that is ideally suited for Smartphones, Tablets, Wearable Sensors, and IoT applications."""
	# Register SELF_TEST_X_GYRO
	# type USR1, bank 1 
	
	def setSELF_TEST_X_GYRO(self, val):
		"""Set register SELF_TEST_X_GYRO"""
		self.write(REG.SELF_TEST_X_GYRO, val, 8)
	
	def getSELF_TEST_X_GYRO(self):
		"""Get register SELF_TEST_X_GYRO"""
		return self.read(REG.SELF_TEST_X_GYRO, 8)
	
	# Bits XG_ST_DATA
	# The value in this register indicates the self-test output generated during
	#           manufacturing tests. This value is to be used to check against subsequent self-test
	#           outputs performed by the end user. 
	
	# Register SELF_TEST_Y_GYRO
	# type USR1, bank 1 
	
	def setSELF_TEST_Y_GYRO(self, val):
		"""Set register SELF_TEST_Y_GYRO"""
		self.write(REG.SELF_TEST_Y_GYRO, val, 8)
	
	def getSELF_TEST_Y_GYRO(self):
		"""Get register SELF_TEST_Y_GYRO"""
		return self.read(REG.SELF_TEST_Y_GYRO, 8)
	
	# Bits YG_ST_DATA
	# The value in this register indicates the self-test output generated during
	#           manufacturing tests. This value is to be used to check against subsequent self-test
	#           outputs performed by the end user. 
	
	# Register SELF_TEST_Z_GYRO
	# type USR1, bank 1 
	
	def setSELF_TEST_Z_GYRO(self, val):
		"""Set register SELF_TEST_Z_GYRO"""
		self.write(REG.SELF_TEST_Z_GYRO, val, 8)
	
	def getSELF_TEST_Z_GYRO(self):
		"""Get register SELF_TEST_Z_GYRO"""
		return self.read(REG.SELF_TEST_Z_GYRO, 8)
	
	# Bits ZG_ST_DATA
	# The value in this register indicates the self-test output generated during
	#           manufacturing tests. This value is to be used to check against subsequent self-test
	#           outputs performed by the end user. 
	
	# Register SELF_TEST_X_ACCEL
	# type USR1, bank 1 
	
	def setSELF_TEST_X_ACCEL(self, val):
		"""Set register SELF_TEST_X_ACCEL"""
		self.write(REG.SELF_TEST_X_ACCEL, val, 8)
	
	def getSELF_TEST_X_ACCEL(self):
		"""Get register SELF_TEST_X_ACCEL"""
		return self.read(REG.SELF_TEST_X_ACCEL, 8)
	
	# Bits XA_ST_DATA
	# Contains self-test data for the X Accelerometer. 
	# Register SELF_TEST_Y_ACCEL
	# type USR1, bank 1 
	
	def setSELF_TEST_Y_ACCEL(self, val):
		"""Set register SELF_TEST_Y_ACCEL"""
		self.write(REG.SELF_TEST_Y_ACCEL, val, 8)
	
	def getSELF_TEST_Y_ACCEL(self):
		"""Get register SELF_TEST_Y_ACCEL"""
		return self.read(REG.SELF_TEST_Y_ACCEL, 8)
	
	# Bits YA_ST_DATA
	# Contains self-test data for the Y Accelerometer. 
	# Register SELF_TEST_Z_ACCEL
	# type USR1, bank 1 
	
	def setSELF_TEST_Z_ACCEL(self, val):
		"""Set register SELF_TEST_Z_ACCEL"""
		self.write(REG.SELF_TEST_Z_ACCEL, val, 8)
	
	def getSELF_TEST_Z_ACCEL(self):
		"""Get register SELF_TEST_Z_ACCEL"""
		return self.read(REG.SELF_TEST_Z_ACCEL, 8)
	
	# Bits ZA_ST_DATA
	# Contains self-test data for the Z Accelerometer. 
	# Register XA_OFFS_H
	# type USR1, bank 1 
	
	def setXA_OFFS_H(self, val):
		"""Set register XA_OFFS_H"""
		self.write(REG.XA_OFFS_H, val, 8)
	
	def getXA_OFFS_H(self):
		"""Get register XA_OFFS_H"""
		return self.read(REG.XA_OFFS_H, 8)
	
	# Bits XA_OFFS
	# Upper bits of the X accelerometer offset cancellation. 
	# Register XA_OFFS_L
	# type USR1, bank 1 
	
	def setXA_OFFS_L(self, val):
		"""Set register XA_OFFS_L"""
		self.write(REG.XA_OFFS_L, val, 8)
	
	def getXA_OFFS_L(self):
		"""Get register XA_OFFS_L"""
		return self.read(REG.XA_OFFS_L, 8)
	
	# Bits XA_OFFS
	# Lower bits of the X accelerometer offset cancellation. 
	# Bits reserved_0
	# Register YA_OFFS_H
	# type USR1, bank 1 
	
	def setYA_OFFS_H(self, val):
		"""Set register YA_OFFS_H"""
		self.write(REG.YA_OFFS_H, val, 8)
	
	def getYA_OFFS_H(self):
		"""Get register YA_OFFS_H"""
		return self.read(REG.YA_OFFS_H, 8)
	
	# Bits YA_OFFS
	# Upper bits of the Y accelerometer offset cancellation. 
	# Register YA_OFFS_L
	# type USR1, bank 1 
	
	def setYA_OFFS_L(self, val):
		"""Set register YA_OFFS_L"""
		self.write(REG.YA_OFFS_L, val, 8)
	
	def getYA_OFFS_L(self):
		"""Get register YA_OFFS_L"""
		return self.read(REG.YA_OFFS_L, 8)
	
	# Bits YA_OFFS
	# Lower bits of the Y accelerometer offset cancellation. 
	# Bits reserved_0
	# Register ZA_OFFS_H
	# type USR1, bank 1 
	
	def setZA_OFFS_H(self, val):
		"""Set register ZA_OFFS_H"""
		self.write(REG.ZA_OFFS_H, val, 8)
	
	def getZA_OFFS_H(self):
		"""Get register ZA_OFFS_H"""
		return self.read(REG.ZA_OFFS_H, 8)
	
	# Bits ZA_OFFS
	# Upper bits of the Z accelerometer offset cancellation. 
	# Register ZA_OFFS_L
	# type USR1, bank 1 
	
	def setZA_OFFS_L(self, val):
		"""Set register ZA_OFFS_L"""
		self.write(REG.ZA_OFFS_L, val, 8)
	
	def getZA_OFFS_L(self):
		"""Get register ZA_OFFS_L"""
		return self.read(REG.ZA_OFFS_L, 8)
	
	# Bits ZA_OFFS
	# Lower bits of the Z accelerometer offset cancellation. 
	# Bits reserved_0
	# Register TIMEBASE_CORRECTION_PLL
	# type USR1, bank 1 
	
	def setTIMEBASE_CORRECTION_PLL(self, val):
		"""Set register TIMEBASE_CORRECTION_PLL"""
		self.write(REG.TIMEBASE_CORRECTION_PLL, val, 8)
	
	def getTIMEBASE_CORRECTION_PLL(self):
		"""Get register TIMEBASE_CORRECTION_PLL"""
		return self.read(REG.TIMEBASE_CORRECTION_PLL, 8)
	
	# Bits TBC_PLL
	# System PLL clock period error (signed, [-10%, +10%]). 
	# Register REG_BANK_SEL
	# type -, bank 1 
	
	def setREG_BANK_SEL(self, val):
		"""Set register REG_BANK_SEL"""
		self.write(REG.REG_BANK_SEL, val, 8)
	
	def getREG_BANK_SEL(self):
		"""Get register REG_BANK_SEL"""
		return self.read(REG.REG_BANK_SEL, 8)
	
	# Bits reserved_0
	# Bits USER_BANK
	# Use the values in this bit-field to select a USER BANK. 
	# Bits reserved_1

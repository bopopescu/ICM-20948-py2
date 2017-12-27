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
	# Register I2C_MST_ODR_CONFIG
	# type USR3, bank 3 
	
	def setI2C_MST_ODR_CONFIG(self, val):
		"""Set register I2C_MST_ODR_CONFIG"""
		self.write(REG.I2C_MST_ODR_CONFIG, val, 8)
	
	def getI2C_MST_ODR_CONFIG(self):
		"""Get register I2C_MST_ODR_CONFIG"""
		return self.read(REG.I2C_MST_ODR_CONFIG, 8)
	
	# Bits reserved_0
	# Bits I2C_MST_ODR_CONFIG
	# ODR configuration for external sensor when gyroscope and accelerometer are
	#           disabled.  ODR is computed as follows:
	#           1.1 kHz/(2^((odr_config[3:0])) )
	#           When gyroscope is enabled, all sensors (including I2C_MASTER) use the gyroscope
	#           ODR. If gyroscope is disabled, then all sensors (including I2C_MASTER) use the
	#           accelerometer ODR. 
	
	# Register I2C_MST_CTRL
	# type USR3, bank 3 
	
	def setI2C_MST_CTRL(self, val):
		"""Set register I2C_MST_CTRL"""
		self.write(REG.I2C_MST_CTRL, val, 8)
	
	def getI2C_MST_CTRL(self):
		"""Get register I2C_MST_CTRL"""
		return self.read(REG.I2C_MST_CTRL, 8)
	
	# Bits MULT_MST_EN
	# Enables multi-master capability. When disabled, clocking to the I2C_MST_IF can be
	#           disabled when not in use and the logic to detect lost arbitration is disabled. 
	
	# Bits reserved_0
	# Bits I2C_MST_P_NSR
	# This bit controls the I2C Master’s transition from one slave read to the next slave
	#           read.
	#           0 - There is a restart between reads.
	#           1 - There is a stop between reads. 
	
	# Bits I2C_MST_CLK
	# Sets I2C master clock frequency as shown in Table 23. 
	# Register I2C_MST_DELAY_CTRL
	# type USR3, bank 3 
	
	def setI2C_MST_DELAY_CTRL(self, val):
		"""Set register I2C_MST_DELAY_CTRL"""
		self.write(REG.I2C_MST_DELAY_CTRL, val, 8)
	
	def getI2C_MST_DELAY_CTRL(self):
		"""Get register I2C_MST_DELAY_CTRL"""
		return self.read(REG.I2C_MST_DELAY_CTRL, 8)
	
	# Bits DELAY_ES_SHADOW
	# Delays shadowing of external sensor data until all data is received. 
	# Bits reserved_0
	# Bits I2C_SLV4_DELAY_EN
	# When enabled, slave 4 will only be accessed 1/(1+I2C_SLC4_DLY) samples as
	#           determined by I2C_MST_ODR_CONFIG. 
	
	# Bits I2C_SLV3_DELAY_EN
	# When enabled, slave 3 will only be accessed 1/(1+I2C_SLC4_DLY) samples as
	#           determined by I2C_MST_ODR_CONFIG. 
	
	# Bits I2C_SLV2_DELAY_EN
	# When enabled, slave 2 will only be accessed 1/(1+I2C_SLC4_DLY) samples as
	#           determined by I2C_MST_ODR_CONFIG. 
	
	# Bits I2C_SLV1_DELAY_EN
	# When enabled, slave 1 will only be accessed 1/(1+I2C_SLC4_DLY) samples as
	#           determined by I2C_MST_ODR_CONFIG. 
	
	# Bits I2C_SLV0_DELAY_EN
	# When enabled, slave 0 will only be accessed 1/(1+I2C_SLC4_DLY) samples as
	#           determined by I2C_MST_ODR_CONFIG. 
	
	# Register I2C_SLV0_ADDR
	# type USR3, bank 3 
	
	def setI2C_SLV0_ADDR(self, val):
		"""Set register I2C_SLV0_ADDR"""
		self.write(REG.I2C_SLV0_ADDR, val, 8)
	
	def getI2C_SLV0_ADDR(self):
		"""Get register I2C_SLV0_ADDR"""
		return self.read(REG.I2C_SLV0_ADDR, 8)
	
	# Bits I2C_SLV0_RNW
	# 1 - Transfer is a read.
	#           0 - Transfer is a write. 
	
	# Bits I2C_ID_0
	# Physical address of I2C slave 0. 
	# Register I2C_SLV0_REG
	# type USR3, bank 3 
	
	def setI2C_SLV0_REG(self, val):
		"""Set register I2C_SLV0_REG"""
		self.write(REG.I2C_SLV0_REG, val, 8)
	
	def getI2C_SLV0_REG(self):
		"""Get register I2C_SLV0_REG"""
		return self.read(REG.I2C_SLV0_REG, 8)
	
	# Bits I2C_SLV0_REG
	# I2C slave 0 register address from where to begin data transfer. 
	# Register I2C_SLV0_CTRL
	# type USR3, bank 3 
	
	def setI2C_SLV0_CTRL(self, val):
		"""Set register I2C_SLV0_CTRL"""
		self.write(REG.I2C_SLV0_CTRL, val, 8)
	
	def getI2C_SLV0_CTRL(self):
		"""Get register I2C_SLV0_CTRL"""
		return self.read(REG.I2C_SLV0_CTRL, 8)
	
	# Bits I2C_SLV0_EN
	# 1 - Enable reading data from this slave at the sample rate and storing data at the first
	#           available EXT_SENS_DATA register, which is always EXT_SENS_DATA_00 for I2C slave 0.
	#           0 - Function is disabled for this slave. 
	
	# Bits I2C_SLV0_BYTE_SW
	# 1 - Swap bytes when reading both the low and high byte of a word. Note there is
	#           nothing to swap after reading the first byte if I2C_SLV0_REG[0] = 1, or if the last byte
	#           read has a register address lsb = 0.
	#           For example, if I2C_SLV0_REG = 0x1, and I2C_SLV0_LENG = 0x4:
	#           1) The first byte read from address 0x1 will be stored at EXT_SENS_DATA_00,
	#           2) the second and third bytes will be read and swapped, so the data read from address
	#           0x2 will be stored at EXT_SENS_DATA_02, and the data read from address 0x3 will be
	#           stored at EXT_SENS_DATA_01,
	#           3) The last byte read from address 0x4 will be stored at EXT_SENS_DATA_03.
	#           0 - No swapping occurs; bytes are written in order read. 
	
	# Bits I2C_SLV0_REG_DIS
	# When set, the transaction does not write a register value, it will only read data, or write
	#           data. 
	
	# Bits I2C_SLV0_GRP
	# External sensor data typically comes in as groups of two bytes. This bit is used to
	#           determine if the groups are from the slave’s register address 0 and 1, 2 and 3, etc.., or if
	#           the groups are address 1 and 2, 3 and 4, etc.
	#           0 indicates slave register addresses 0 and 1 are grouped together (odd numbered
	#           register ends the group). 1 indicates slave register addresses 1 and 2 are grouped
	#           together (even numbered register ends the group). This allows byte swapping of
	#           registers that are grouped starting at any address. 
	
	# Bits I2C_SLV0_LENG
	# Number of bytes to be read from I2C slave 0. 
	# Register I2C_SLV0_DO
	# type USR3, bank 3 
	
	def setI2C_SLV0_DO(self, val):
		"""Set register I2C_SLV0_DO"""
		self.write(REG.I2C_SLV0_DO, val, 8)
	
	def getI2C_SLV0_DO(self):
		"""Get register I2C_SLV0_DO"""
		return self.read(REG.I2C_SLV0_DO, 8)
	
	# Bits I2C_SLV0_DO
	# Data out when slave 0 is set to write. 
	# Register I2C_SLV1_ADDR
	# type USR3, bank 3 
	
	def setI2C_SLV1_ADDR(self, val):
		"""Set register I2C_SLV1_ADDR"""
		self.write(REG.I2C_SLV1_ADDR, val, 8)
	
	def getI2C_SLV1_ADDR(self):
		"""Get register I2C_SLV1_ADDR"""
		return self.read(REG.I2C_SLV1_ADDR, 8)
	
	# Bits I2C_SLV1_RNW
	# 1 - Transfer is a read.
	#           0 - Transfer is a write. 
	
	# Bits I2C_ID_1
	# Physical address of I2C slave 1. 
	# Register I2C_SLV1_REG
	# type USR3, bank 3 
	
	def setI2C_SLV1_REG(self, val):
		"""Set register I2C_SLV1_REG"""
		self.write(REG.I2C_SLV1_REG, val, 8)
	
	def getI2C_SLV1_REG(self):
		"""Get register I2C_SLV1_REG"""
		return self.read(REG.I2C_SLV1_REG, 8)
	
	# Bits I2C_SLV1_REG
	# I2C slave 1 register address from where to begin data transfer. 
	# Register I2C_SLV1_CTRL
	# type USR3, bank 3 
	
	def setI2C_SLV1_CTRL(self, val):
		"""Set register I2C_SLV1_CTRL"""
		self.write(REG.I2C_SLV1_CTRL, val, 8)
	
	def getI2C_SLV1_CTRL(self):
		"""Get register I2C_SLV1_CTRL"""
		return self.read(REG.I2C_SLV1_CTRL, 8)
	
	# Bits I2C_SLV1_EN
	# 1 - Enable reading data from this slave at the sample rate and storing data at the first
	#           available EXT_SENS_DATA register as determined by I2C_SLV0_EN and
	#           I2C_SLV0_LENG.
	#           0 - Function is disabled for this slave. 
	
	# Bits I2C_SLV1_BYTE_SW
	# 1 - Swap bytes when reading both the low and high byte of a word. Note there is
	#           nothing to swap after reading the first byte if I2C_SLV1_REG[0] = 1, or if the last byte
	#           read has a register address lsb = 0.
	#           For example, if I2C_SLV0_EN = 0x1, and I2C_SLV0_LENG = 0x3 (to show swap has to
	#           do with I2C slave address not EXT_SENS_DATA address), and if I2C_SLV1_REG = 0x1,
	#           and I2C_SLV1_LENG = 0x4:
	#           1) The first byte read from address 0x1 will be stored at EXT_SENS_DATA_03 (slave
	#           0’s data will be in EXT_SENS_DATA_00, EXT_SENS_DATA_01, and
	#           EXT_SENS_DATA_02),
	#           2) the second and third bytes will be read and swapped, so the data read from
	#           address 0x2 will be stored at EXT_SENS_DATA_04, and the data read from address
	#           0x3 will be stored at EXT_SENS_DATA_05,
	#           3) The last byte read from address 0x4 will be stored at EXT_SENS_DATA_06.
	#           0 - No swapping occurs, bytes are written in order read. 
	
	# Bits I2C_SLV1_REG_DIS
	# When set, the transaction does not write a register value, it will only read data, or
	#           write data. 
	
	# Bits I2C_SLV1_GRP
	# External sensor data typically comes in as groups of two bytes. This bit is used to
	#           determine if the groups are from the slave’s register address 0 and 1, 2 and 3, etc..,
	#           or if the groups are address 1 and 2, 3 and 4, etc.
	#           0 indicates slave register addresses 0 and 1 are grouped together (odd numbered
	#           register ends the group). 1 indicates slave register addresses 1 and 2 are grouped
	#           together (even numbered register ends the group). This allows byte swapping of
	#           registers that are grouped starting at any address. 
	
	# Bits I2C_SLV1_LENG
	# Number of bytes to be read from I2C slave 1. 
	# Register I2C_SLV1_DO
	# type USR3, bank 3 
	
	def setI2C_SLV1_DO(self, val):
		"""Set register I2C_SLV1_DO"""
		self.write(REG.I2C_SLV1_DO, val, 8)
	
	def getI2C_SLV1_DO(self):
		"""Get register I2C_SLV1_DO"""
		return self.read(REG.I2C_SLV1_DO, 8)
	
	# Bits I2C_SLV1_DO
	# Data out when slave 1 is set to write. 
	# Register I2C_SLV2_ADDR
	# type USR3, bank 3 
	
	def setI2C_SLV2_ADDR(self, val):
		"""Set register I2C_SLV2_ADDR"""
		self.write(REG.I2C_SLV2_ADDR, val, 8)
	
	def getI2C_SLV2_ADDR(self):
		"""Get register I2C_SLV2_ADDR"""
		return self.read(REG.I2C_SLV2_ADDR, 8)
	
	# Bits I2C_SLV2_RNW
	# 1 - Transfer is a read.
	#           0 - Transfer is a write. 
	
	# Bits I2C_ID_2
	# Physical address of I2C slave 2. 
	# Register I2C_SLV2_REG
	# type USR3, bank 3 
	
	def setI2C_SLV2_REG(self, val):
		"""Set register I2C_SLV2_REG"""
		self.write(REG.I2C_SLV2_REG, val, 8)
	
	def getI2C_SLV2_REG(self):
		"""Get register I2C_SLV2_REG"""
		return self.read(REG.I2C_SLV2_REG, 8)
	
	# Bits I2C_SLV2_REG
	# I2C slave 2 register address from where to begin data transfer. 
	# Register I2C_SLV2_CTRL
	# type USR3, bank 3 
	
	def setI2C_SLV2_CTRL(self, val):
		"""Set register I2C_SLV2_CTRL"""
		self.write(REG.I2C_SLV2_CTRL, val, 8)
	
	def getI2C_SLV2_CTRL(self):
		"""Get register I2C_SLV2_CTRL"""
		return self.read(REG.I2C_SLV2_CTRL, 8)
	
	# Bits I2C_SLV2_EN
	# 1 - Enable reading data from this slave at the sample rate and storing data at the first
	#           available EXT_SENS_DATA register as determined by I2C_SLV0_EN, I2C_SLV0_LENG,
	#           I2C_SLV1_EN and I2C_SLV1_LENG.
	#           0 - Function is disabled for this slave. 
	
	# Bits I2C_SLV2_BYTE_SW
	# 1 - Swap bytes when reading both the low and high byte of a word. Note there is
	#           nothing to swap after reading the first byte if I2C_SLV2_REG[0] = 1, or if the last byte
	#           read has a register address lsb = 0.
	#           See I2C_SLV1_CTRL for an example.
	#           0 - No swapping occurs, bytes are written in order read. 
	
	# Bits I2C_SLV2_REG_DIS
	# When set, the transaction does not write a register value, it will only read data, or
	#           write data. 
	
	# Bits I2C_SLV2_GRP
	# External sensor data typically comes in as groups of two bytes. This bit is used to
	#           determine if the groups are from the slave’s register address 0 and 1, 2 and 3, etc..,
	#           or if the groups are address 1 and 2, 3 and 4, etc.
	#           0 indicates slave register addresses 0 and 1 are grouped together (odd numbered
	#           register ends the group). 1 indicates slave register addresses 1 and 2 are grouped
	#           together (even numbered register ends the group). This allows byte swapping of
	#           registers that are grouped starting at any address. 
	
	# Bits I2C_SLV2_LENG
	# Number of bytes to be read from I2C slave 2. 
	# Register I2C_SLV2_DO
	# type USR3, bank 3 
	
	def setI2C_SLV2_DO(self, val):
		"""Set register I2C_SLV2_DO"""
		self.write(REG.I2C_SLV2_DO, val, 8)
	
	def getI2C_SLV2_DO(self):
		"""Get register I2C_SLV2_DO"""
		return self.read(REG.I2C_SLV2_DO, 8)
	
	# Bits I2C_SLV2_DO
	# Data out when slave 2 is set to write. 
	# Register I2C_SLV3_ADDR
	# type USR3, bank 3 
	
	def setI2C_SLV3_ADDR(self, val):
		"""Set register I2C_SLV3_ADDR"""
		self.write(REG.I2C_SLV3_ADDR, val, 8)
	
	def getI2C_SLV3_ADDR(self):
		"""Get register I2C_SLV3_ADDR"""
		return self.read(REG.I2C_SLV3_ADDR, 8)
	
	# Bits I2C_SLV3_RNW
	# 1 - Transfer is a read.
	#           0 - Transfer is a write. 
	
	# Bits I2C_ID_3
	# Physical address of I2C slave 3. 
	# Register I2C_SLV3_REG
	# type USR3, bank 3 
	
	def setI2C_SLV3_REG(self, val):
		"""Set register I2C_SLV3_REG"""
		self.write(REG.I2C_SLV3_REG, val, 8)
	
	def getI2C_SLV3_REG(self):
		"""Get register I2C_SLV3_REG"""
		return self.read(REG.I2C_SLV3_REG, 8)
	
	# Bits I2C_SLV3_REG
	# I2C slave 3 register address from where to begin data transfer. 
	# Register I2C_SLV3_CTRL
	# type USR3, bank 3 
	
	def setI2C_SLV3_CTRL(self, val):
		"""Set register I2C_SLV3_CTRL"""
		self.write(REG.I2C_SLV3_CTRL, val, 8)
	
	def getI2C_SLV3_CTRL(self):
		"""Get register I2C_SLV3_CTRL"""
		return self.read(REG.I2C_SLV3_CTRL, 8)
	
	# Bits I2C_SLV3_EN
	# 1 - Enable reading data from this slave at the sample rate and storing data at the first
	#           available EXT_SENS_DATA register as determined by I2C_SLV0_EN, I2C_SLV0_LENG,
	#           I2C_SLV1_EN, I2C_SLV1_LENG, I2C_SLV2_EN and I2C_SLV2_LENG.
	#           0 - Function is disabled for this slave. 
	
	# Bits I2C_SLV3_BYTE_SW
	# 1 - Swap bytes when reading both the low and high byte of a word.  Note there is
	#           nothing to swap after reading the first byte if I2C_SLV3_REG[0] = 1, or if the last byte
	#           read has a register address lsb = 0.
	#           See I2C_SLV1_CTRL for an example.
	#           0 - No swapping occurs, bytes are written in order read. 
	
	# Bits I2C_SLV3_REG_DIS
	# When set, the transaction does not write a register value, it will only read data, or
	#           write data. 
	
	# Bits I2C_SLV3_GRP
	# External sensor data typically comes in as groups of two bytes. This bit is used to
	#           determine if the groups are from the slave’s register address 0 and 1, 2 and 3, etc..,
	#           or if the groups are address 1 and 2, 3 and 4, etc.
	#           0 indicates slave register addresses 0 and 1 are grouped together (odd numbered
	#           register ends the group). 1 indicates slave register addresses 1 and 2 are grouped
	#           together (even numbered register ends the group). This allows byte swapping of
	#           registers that are grouped starting at any address. 
	
	# Bits I2C_SLV3_LENG
	# Number of bytes to be read from I2C slave 3. 
	# Register I2C_SLV3_DO
	# type USR3, bank 3 
	
	def setI2C_SLV3_DO(self, val):
		"""Set register I2C_SLV3_DO"""
		self.write(REG.I2C_SLV3_DO, val, 8)
	
	def getI2C_SLV3_DO(self):
		"""Get register I2C_SLV3_DO"""
		return self.read(REG.I2C_SLV3_DO, 8)
	
	# Bits I2C_SLV3_DO
	# Data out when slave 3 is set to write. 
	# Register I2C_SLV4_ADDR
	# type USR3, bank 3 
	# The I2C Slave 4 interface can be used to perform only single byte read and write transactions. 
	
	
	def setI2C_SLV4_ADDR(self, val):
		"""Set register I2C_SLV4_ADDR"""
		self.write(REG.I2C_SLV4_ADDR, val, 8)
	
	def getI2C_SLV4_ADDR(self):
		"""Get register I2C_SLV4_ADDR"""
		return self.read(REG.I2C_SLV4_ADDR, 8)
	
	# Bits I2C_SLV4_RNW
	# 1 - Transfer is a read.
	#           0 - Transfer is a write. 
	
	# Bits I2C_ID_4
	# Physical address of I2C slave 4. 
	# Register I2C_SLV4_REG
	# type USR3, bank 3 
	
	def setI2C_SLV4_REG(self, val):
		"""Set register I2C_SLV4_REG"""
		self.write(REG.I2C_SLV4_REG, val, 8)
	
	def getI2C_SLV4_REG(self):
		"""Get register I2C_SLV4_REG"""
		return self.read(REG.I2C_SLV4_REG, 8)
	
	# Bits I2C_SLV4_REG
	# I2C slave 4 register address from where to begin data transfer. 
	# Register I2C_SLV4_CTRL
	# type USR3, bank 3 
	
	def setI2C_SLV4_CTRL(self, val):
		"""Set register I2C_SLV4_CTRL"""
		self.write(REG.I2C_SLV4_CTRL, val, 8)
	
	def getI2C_SLV4_CTRL(self):
		"""Get register I2C_SLV4_CTRL"""
		return self.read(REG.I2C_SLV4_CTRL, 8)
	
	# Bits I2C_SLV4_EN
	# 1 - Enable data transfer with this slave at the sample rate. If read command, store
	#           data in I2C_SLV4_DI register, if write command, write data stored in I2C_SLV4_DO
	#           register. Bit is cleared when a single transfer is complete. Be sure to write
	#           I2C_SLV4_DO first.
	#           0 - Function is disabled for this slave. 
	
	# Bits I2C_SLV4_INT_EN
	# 1 - Enables the completion of the I2C slave 4 data transfer to cause an interrupt.
	#           0 - Completion of the I2C slave 4 data transfer will not cause an interrupt. 
	
	# Bits I2C_SLV4_REG_DIS
	# When set, the transaction does not write a register value, it will only read data, or
	#           write data. 
	
	# Bits I2C_SLV4_DLY
	# When enabled via the I2C_MST_DELAY_CTRL, those slaves will only be enabled
	#           every1/(1+I2C_SLV4_DLY) samples as determined by I2C_MST_ODR_CONFIG. 
	
	# Register I2C_SLV4_DO
	# type USR3, bank 3 
	
	def setI2C_SLV4_DO(self, val):
		"""Set register I2C_SLV4_DO"""
		self.write(REG.I2C_SLV4_DO, val, 8)
	
	def getI2C_SLV4_DO(self):
		"""Get register I2C_SLV4_DO"""
		return self.read(REG.I2C_SLV4_DO, 8)
	
	# Bits I2C_SLV4_DO
	# Data out when slave 4 is set to write. 
	# Register I2C_SLV4_DI
	# type USR3, bank 3 
	
	def setI2C_SLV4_DI(self, val):
		"""Set register I2C_SLV4_DI"""
		self.write(REG.I2C_SLV4_DI, val, 8)
	
	def getI2C_SLV4_DI(self):
		"""Get register I2C_SLV4_DI"""
		return self.read(REG.I2C_SLV4_DI, 8)
	
	# Bits I2C_SLV4_DI
	# Data read from I2C Slave 4. 
	# Register REG_BANK_SEL
	# type , bank 3 
	
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

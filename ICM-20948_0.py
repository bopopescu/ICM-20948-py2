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
	# Register WHO_AM_I
	# type USR0, bank 0 
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register to indicate to user which device is being accessed.
	#           The value for ICM-20948 is 0xEA. 
	
	# Register USER_CTRL
	# type USR0, bank 0 
	
	def setUSER_CTRL(self, val):
		"""Set register USER_CTRL"""
		self.write(REG.USER_CTRL, val, 8)
	
	def getUSER_CTRL(self):
		"""Get register USER_CTRL"""
		return self.read(REG.USER_CTRL, 8)
	
	# Bits DMP_EN
	# Bits FIFO_EN
	# To disable FIFO writes by DMA, use FIFO_EN register. To disable possible FIFO writes
	#           from DMP, disable the DMP. 
	
	# Bits I2C_MST_EN
	# Bits I2C_IF_DIS
	# Bits DMP_RST
	# Bits SRAM_RST
	# Bits I2C_MST_RST
	# 1 - Reset I2C Master module. Reset is asynchronous. This bit auto clears after one
	#           clock cycle of the internal 20 MHz clock.
	#           NOTE: This bit should only be set when the I2C master has hung. If this bit is set during an active
	#           I2C master transaction, the I2C slave will hang, which will require the host to reset the slave. 
	
	# Bits reserved_0
	# Register LP_CONFIG
	# type USR0, bank 0 
	
	def setLP_CONFIG(self, val):
		"""Set register LP_CONFIG"""
		self.write(REG.LP_CONFIG, val, 8)
	
	def getLP_CONFIG(self):
		"""Get register LP_CONFIG"""
		return self.read(REG.LP_CONFIG, 8)
	
	# Bits reserved_0
	# Bits I2C_MST_CYCLE
	# 1 - Operate I2C master in duty cycled mode. ODR is determined by
	#           I2C_MST_ODR_CONFIG register.
	#           0 - Disable I2C master duty cycled mode. 
	
	# Bits ACCEL_CYCLE
	# 1 - Operate ACCEL in duty cycled mode. ODR is determined by ACCEL_SMPLRT_DIV
	#           register.
	#           0 - Disable ACCEL duty cycled mode. 
	
	# Bits GYRO_CYCLE
	# 1 - Operate GYRO in duty cycled mode. ODR is determined by GYRO_SMPLRT_DIV
	#           register.
	#           0 - Disable GYRO duty cycled mode. 
	
	# Bits reserved_1
	# Register PWR_MGMT_1
	# type USR0, bank 0 
	
	def setPWR_MGMT_1(self, val):
		"""Set register PWR_MGMT_1"""
		self.write(REG.PWR_MGMT_1, val, 8)
	
	def getPWR_MGMT_1(self):
		"""Get register PWR_MGMT_1"""
		return self.read(REG.PWR_MGMT_1, 8)
	
	# Bits DEVICE_RESET
	# 1 - Reset the internal registers and restores the default settings. Write a 1 to set the
	#           reset, the bit will auto clear. 
	
	# Bits SLEEP
	# When set, the chip is set to sleep mode (in sleep mode all analog is powered off).
	#           Clearing the bit wakes the chip from sleep mode. 
	
	# Bits LP_EN
	# The LP_EN only affects the digital circuitry, it helps to reduce the digital current when
	#           sensors are in LP mode. Please note that the sensors themselves are set in LP mode
	#           by the LP_CONFIG register settings. Sensors in LP mode, and use of LP_EN bit
	#           together help to reduce overall current. The bit settings are:
	#           1: Turn on low power feature.
	#           0: Turn off low power feature.
	#           LP_EN has no effect when the sensors are in low-noise mode. 
	
	# Bits reserved_0
	# Bits TEMP_DIS
	# When set to 1, this bit disables the temperature sensor. 
	# Bits CLKSEL
	# Code: Clock Source
	#           0: Internal 20 MHz oscillator
	#           1-5: Auto selects the best available clock source - PLL if ready, else use the Internal oscillator
	#           6: Internal 20 MHz oscillator
	#           7: Stops the clock and keeps timing generator in reset
	#           NOTE: CLKSEL[2:0] should be set to 1~5 to achieve full gyroscope performance. 
	
	# Register PWR_MGMT_2
	# type USR0, bank 0 
	
	def setPWR_MGMT_2(self, val):
		"""Set register PWR_MGMT_2"""
		self.write(REG.PWR_MGMT_2, val, 8)
	
	def getPWR_MGMT_2(self):
		"""Get register PWR_MGMT_2"""
		return self.read(REG.PWR_MGMT_2, 8)
	
	# Bits reserved_0
	# Bits DISABLE_ACCEL
	# Only the following values are applicable:
	#           111 - Accelerometer (all axes) disabled.
	#           000 - Accelerometer (all axes) on. 
	
	# Bits DISABLE_GYRO
	# Only the following values are applicable:
	#           111 - Gyroscope (all axes) disabled.
	#           000 - Gyroscope (all axes) on. 
	
	# Register INT_PIN_CFG
	# type USR0, bank 0 
	
	def setINT_PIN_CFG(self, val):
		"""Set register INT_PIN_CFG"""
		self.write(REG.INT_PIN_CFG, val, 8)
	
	def getINT_PIN_CFG(self):
		"""Get register INT_PIN_CFG"""
		return self.read(REG.INT_PIN_CFG, 8)
	
	# Bits INT1_ACTL
	# 1 - The logic level for INT1 pin is active low.
	#           0 - The logic level for INT1 pin is active high. 
	
	# Bits INT1_OPEN
	# 1 - INT1 pin is configured as open drain.
	#           0 - INT1 pin is configured as push-pull. 
	
	# Bits INT1_LATCH_EN
	# 1 - INT1 pin level held until interrupt status is cleared.
	#           0 - INT1 pin indicates interrupt pulse is width 50 µs. 
	
	# Bits INT_ANYRD_2CLEAR
	# 1 - Interrupt status in INT_STATUS is cleared (set to 0) if any read operation is
	#           performed.
	#           0 - Interrupt status in INT_STATUS is cleared (set to 0) only by reading INT_STATUS
	#           register.
	#           This bit only affects the interrupt status bits that are contained in the register
	#           INT_STATUS, and the corresponding hardware interrupt.
	#           This bit does not affect the interrupt status bits that are contained in registers
	#           INT_STATUS_1, INT_STATUS_2, INT_STATUS_3, and the corresponding hardware
	#           interrupt. 
	
	# Bits ACTL_FSYNC
	# 1 - The logic level for the FSYNC pin as an interrupt to the ICM-20948 is active low.
	#           0 - The logic level for the FSYNC pin as an interrupt to the ICM-20948 is active high. 
	
	# Bits FSYNC_INT_MODE_EN
	# 1 - This enables the FSYNC pin to be used as an interrupt. A transition to the active
	#           level described by the ACTL_FSYNC bit will cause an interrupt. The status of the
	#           interrupt is read in the I2C Master Status register PASS_THROUGH bit.
	#           0 - This disables the FSYNC pin from causing an interrupt. 
	
	# Bits BYPASS_EN
	# When asserted, the I2C_MASTER interface pins (ES_CL and ES_DA) will go into
	#           ‘bypass mode’ when the I2C master interface is disabled. 
	
	# Bits reserved_0
	# Register INT_ENABLE
	# type USR0, bank 0 
	
	def setINT_ENABLE(self, val):
		"""Set register INT_ENABLE"""
		self.write(REG.INT_ENABLE, val, 8)
	
	def getINT_ENABLE(self):
		"""Get register INT_ENABLE"""
		return self.read(REG.INT_ENABLE, 8)
	
	# Bits REG_WOF_EN
	# 1 - Enable wake on FSYNC interrupt.
	#           0 - Function is disabled. 
	
	# Bits reserved_0
	# Bits WOM_INT_EN
	# 1 - Enable interrupt for wake on motion to propagate to interrupt pin 1.
	#           0 - Function is disabled. 
	
	# Bits PLL_RDY_EN
	# 1 - Enable PLL RDY interrupt (PLL RDY means PLL is running and in use as the clock
	#           source for the system) to propagate to interrupt pin 1.
	#           0 - Function is disabled. 
	
	# Bits DMP_INT1_EN
	# 1 - Enable DMP interrupt to propagate to interrupt pin 1.
	#           0 - Function is disabled. 
	
	# Bits I2C_MST_INT_EN
	# 1 - Enable I2C master interrupt to propagate to interrupt pin 1.
	#           0 - Function is disabled. 
	
	# Register INT_ENABLE_1
	# type USR0, bank 0 
	
	def setINT_ENABLE_1(self, val):
		"""Set register INT_ENABLE_1"""
		self.write(REG.INT_ENABLE_1, val, 8)
	
	def getINT_ENABLE_1(self):
		"""Get register INT_ENABLE_1"""
		return self.read(REG.INT_ENABLE_1, 8)
	
	# Bits reserved_0
	# Bits RAW_DATA_0_RDY_EN
	# 1 - Enable raw data ready interrupt from any sensor to propagate to interrupt
	#           pin 1.
	#           0 - Function is disabled. 
	
	# Register INT_ENABLE_2
	# type USR0, bank 0 
	
	def setINT_ENABLE_2(self, val):
		"""Set register INT_ENABLE_2"""
		self.write(REG.INT_ENABLE_2, val, 8)
	
	def getINT_ENABLE_2(self):
		"""Get register INT_ENABLE_2"""
		return self.read(REG.INT_ENABLE_2, 8)
	
	# Bits reserved_0
	# Bits FIFO_OVERFLOW_EN
	# 1 - Enable interrupt for FIFO overflow to propagate to interrupt pin 1.
	#           0 - Function is disabled. 
	
	# Register INT_ENABLE_3
	# type USR0, bank 0 
	
	def setINT_ENABLE_3(self, val):
		"""Set register INT_ENABLE_3"""
		self.write(REG.INT_ENABLE_3, val, 8)
	
	def getINT_ENABLE_3(self):
		"""Get register INT_ENABLE_3"""
		return self.read(REG.INT_ENABLE_3, 8)
	
	# Bits reserved_0
	# Bits FIFO_WM_EN
	# 1 - Enable interrupt for FIFO watermark to propagate to interrupt pin 1.
	#           0 - Function is disabled. 
	
	# Register I2C_MST_STATUS
	# type USR0, bank 0 
	
	def setI2C_MST_STATUS(self, val):
		"""Set register I2C_MST_STATUS"""
		self.write(REG.I2C_MST_STATUS, val, 8)
	
	def getI2C_MST_STATUS(self):
		"""Get register I2C_MST_STATUS"""
		return self.read(REG.I2C_MST_STATUS, 8)
	
	# Bits PASS_THROUGH
	# Status of FSYNC interrupt - used as a way to pass an external interrupt through this
	#           chip to the host.  If enabled in the INT_PIN_CFG register by asserting bit
	#           FSYNC_INT_MODE_EN, this will cause an interrupt.  A read of this register clears all
	#           status bits in this register. 
	
	# Bits I2C_SLV4_DONE
	# Asserted when I2C slave 4’s transfer is complete, will cause an interrupt if bit
	#           I2C_MST_INT_EN in the INT_ENABLE register is asserted, and if the
	#           SLV4_DONE_INT_EN bit is asserted in the I2C_SLV4_CTRL register. 
	
	# Bits I2C_LOST_ARB
	# Asserted when I2C slave loses arbitration of the I2C bus, will cause an interrupt if bit
	#           I2C_MST_INT_EN in the INT_ENABLE register is asserted. 
	
	# Bits I2C_SLV4_NACK
	# Asserted when slave 4 receives a NACK, will cause an interrupt if bit I2C_MST_INT_EN
	#           in the INT_ENABLE register is asserted. 
	
	# Bits I2C_SLV3_NACK
	# Asserted when slave 3 receives a NACK, will cause an interrupt if bit I2C_MST_INT_EN
	#           in the INT_ENABLE register is asserted. 
	
	# Bits I2C_SLV2_NACK
	# Asserted when slave 2 receives a NACK, will cause an interrupt if bit I2C_MST_INT_EN
	#           in the INT_ENABLE register is asserted. 
	
	# Bits I2C_SLV1_NACK
	# Asserted when slave 1 receives a NACK, will cause an interrupt if bit I2C_MST_INT_EN
	#           in the INT_ENABLE register is asserted. 
	
	# Bits I2C_SLV0_NACK
	# Asserted when slave 0 receives a NACK, will cause an interrupt if bit I2C_MST_INT_EN
	#           in the INT_ENABLE register is asserted. 
	
	# Register INT_STATUS
	# type USR0, bank 0 
	
	def setINT_STATUS(self, val):
		"""Set register INT_STATUS"""
		self.write(REG.INT_STATUS, val, 8)
	
	def getINT_STATUS(self):
		"""Get register INT_STATUS"""
		return self.read(REG.INT_STATUS, 8)
	
	# Bits reserved_0
	# Bits WOM_INT
	# 1 - Wake on motion interrupt occurred. 
	# Bits PLL_RDY_INT
	# 1 - Indicates that the PLL has been enabled and is ready (delay of 4 ms ensures lock). 
	# Bits DMP_INT1
	# 1 - Indicates the DMP has generated INT1 interrupt. 
	# Bits I2C_MST_INT
	# 1 - Indicates I2C master has generated an interrupt. 
	# Register INT_STATUS_1
	# type USR0, bank 0 
	
	def setINT_STATUS_1(self, val):
		"""Set register INT_STATUS_1"""
		self.write(REG.INT_STATUS_1, val, 8)
	
	def getINT_STATUS_1(self):
		"""Get register INT_STATUS_1"""
		return self.read(REG.INT_STATUS_1, 8)
	
	# Bits reserved_0
	# Bits RAW_DATA_0_RDY_INT
	# 1 - Sensor Register Raw Data, from all sensors, is updated and ready to be read. 
	# Register INT_STATUS_2
	# type USR0, bank 0 
	
	def setINT_STATUS_2(self, val):
		"""Set register INT_STATUS_2"""
		self.write(REG.INT_STATUS_2, val, 8)
	
	def getINT_STATUS_2(self):
		"""Get register INT_STATUS_2"""
		return self.read(REG.INT_STATUS_2, 8)
	
	# Bits reserved_0
	# Bits FIFO_OVERFLOW_INT
	# 1 - FIFO Overflow interrupt occurred. 
	# Register INT_STATUS_3
	# type USR0, bank 0 
	
	def setINT_STATUS_3(self, val):
		"""Set register INT_STATUS_3"""
		self.write(REG.INT_STATUS_3, val, 8)
	
	def getINT_STATUS_3(self):
		"""Get register INT_STATUS_3"""
		return self.read(REG.INT_STATUS_3, 8)
	
	# Bits reserved_0
	# Bits FIFO_WM_INT
	# 1 - Watermark interrupt for FIFO occurred. 
	# Register DELAY_TIMEH
	# type USR0, bank 0 
	
	def setDELAY_TIMEH(self, val):
		"""Set register DELAY_TIMEH"""
		self.write(REG.DELAY_TIMEH, val, 8)
	
	def getDELAY_TIMEH(self):
		"""Get register DELAY_TIMEH"""
		return self.read(REG.DELAY_TIMEH, 8)
	
	# Bits DELAY_TIMEH
	# High-byte of delay time between FSYNC event and the 1st gyro ODR event (after the
	#           FSYNC event).
	#           Reading DELAY_TIMEH will lock DELAY_TIMEH and DELAY_TIMEL from the next
	#           update.  Reading DELAY_TIMEL will unlock DELAY_TIMEH and DELAY_TIMEL to take
	#           the next update due to an FSYNC event. 
	
	# Register DELAY_TIMEL
	# type USR0, bank 0 
	
	def setDELAY_TIMEL(self, val):
		"""Set register DELAY_TIMEL"""
		self.write(REG.DELAY_TIMEL, val, 8)
	
	def getDELAY_TIMEL(self):
		"""Get register DELAY_TIMEL"""
		return self.read(REG.DELAY_TIMEL, 8)
	
	# Bits DELAY_TIMEL
	# Low-byte of delay time between FSYNC event and the 1st gyro ODR event (after the
	#           FSYNC event).
	#           Reading DELAY_TIMEH will lock DELAY_TIMEH and DELAY_TIMEL from the next
	#           update. Reading DELAY_TIMEL will unlock DELAY_TIMEH and DELAY_TIMEL to take
	#           the next update due to an FSYNC event.
	#           Delay time in µs = (DELAY_TIMEH * 256 +  DELAY_TIMEL) * 0.9645 
	
	# Register ACCEL_XOUT_H
	# type USR0, bank 0 
	
	def setACCEL_XOUT_H(self, val):
		"""Set register ACCEL_XOUT_H"""
		self.write(REG.ACCEL_XOUT_H, val, 8)
	
	def getACCEL_XOUT_H(self):
		"""Get register ACCEL_XOUT_H"""
		return self.read(REG.ACCEL_XOUT_H, 8)
	
	# Bits ACCEL_XOUT_H
	# High Byte of Accelerometer X-axis data. 
	# Register ACCEL_XOUT_L
	# type USR0, bank 0 
	
	def setACCEL_XOUT_L(self, val):
		"""Set register ACCEL_XOUT_L"""
		self.write(REG.ACCEL_XOUT_L, val, 8)
	
	def getACCEL_XOUT_L(self):
		"""Get register ACCEL_XOUT_L"""
		return self.read(REG.ACCEL_XOUT_L, 8)
	
	# Bits ACCEL_XOUT_L
	# Low Byte of Accelerometer X-axis data.
	#           To convert the output of the accelerometer to acceleration measurement use the
	#           formula below:
	#           X_acceleration = ACCEL_XOUT/Accel_Sensitivity 
	
	# Register ACCEL_YOUT_H
	# type USR0, bank 0 
	
	def setACCEL_YOUT_H(self, val):
		"""Set register ACCEL_YOUT_H"""
		self.write(REG.ACCEL_YOUT_H, val, 8)
	
	def getACCEL_YOUT_H(self):
		"""Get register ACCEL_YOUT_H"""
		return self.read(REG.ACCEL_YOUT_H, 8)
	
	# Bits ACCEL_YOUT_H
	# High Byte of Accelerometer Y-axis data. 
	# Register ACCEL_YOUT_L
	# type USR0, bank 0 
	
	def setACCEL_YOUT_L(self, val):
		"""Set register ACCEL_YOUT_L"""
		self.write(REG.ACCEL_YOUT_L, val, 8)
	
	def getACCEL_YOUT_L(self):
		"""Get register ACCEL_YOUT_L"""
		return self.read(REG.ACCEL_YOUT_L, 8)
	
	# Bits ACCEL_YOUT_L
	# Low Byte of Accelerometer Y-axis data.
	#           To convert the output of the accelerometer to acceleration measurement use the
	#           formula below:
	#           Y_acceleration = ACCEL_YOUT/Accel_Sensitivity 
	
	# Register ACCEL_ZOUT_H
	# type USR0, bank 0 
	
	def setACCEL_ZOUT_H(self, val):
		"""Set register ACCEL_ZOUT_H"""
		self.write(REG.ACCEL_ZOUT_H, val, 8)
	
	def getACCEL_ZOUT_H(self):
		"""Get register ACCEL_ZOUT_H"""
		return self.read(REG.ACCEL_ZOUT_H, 8)
	
	# Bits ACCEL_ZOUT_H
	# High Byte of Accelerometer Z-axis data. 
	# Register ACCEL_ZOUT_L
	# type USR0, bank 0 
	
	def setACCEL_ZOUT_L(self, val):
		"""Set register ACCEL_ZOUT_L"""
		self.write(REG.ACCEL_ZOUT_L, val, 8)
	
	def getACCEL_ZOUT_L(self):
		"""Get register ACCEL_ZOUT_L"""
		return self.read(REG.ACCEL_ZOUT_L, 8)
	
	# Bits ACCEL_ZOUT_L
	# Low Byte of Accelerometer Z-axis data.
	#           To convert the output of the accelerometer to acceleration measurement use the
	#           formula below:
	#           Z_acceleration = ACCEL_ZOUT/Accel_Sensitivity 
	
	# Register GYRO_XOUT_H
	# type USR0, bank 0 
	
	def setGYRO_XOUT_H(self, val):
		"""Set register GYRO_XOUT_H"""
		self.write(REG.GYRO_XOUT_H, val, 8)
	
	def getGYRO_XOUT_H(self):
		"""Get register GYRO_XOUT_H"""
		return self.read(REG.GYRO_XOUT_H, 8)
	
	# Bits GYRO_XOUT_H
	# High Byte of Gyroscope X-axis data. 
	# Register GYRO_XOUT_L
	# type USR0, bank 0 
	
	def setGYRO_XOUT_L(self, val):
		"""Set register GYRO_XOUT_L"""
		self.write(REG.GYRO_XOUT_L, val, 8)
	
	def getGYRO_XOUT_L(self):
		"""Get register GYRO_XOUT_L"""
		return self.read(REG.GYRO_XOUT_L, 8)
	
	# Bits GYRO_XOUT_L
	# Low Byte of Gyroscope X-axis data.
	#           To convert the output of the gyroscope to angular rate measurement use the
	#           formula below:
	#           X_angular_rate = GYRO_XOUT/Gyro_Sensitivity 
	
	# Register GYRO_YOUT_H
	# type USR0, bank 0 
	
	def setGYRO_YOUT_H(self, val):
		"""Set register GYRO_YOUT_H"""
		self.write(REG.GYRO_YOUT_H, val, 8)
	
	def getGYRO_YOUT_H(self):
		"""Get register GYRO_YOUT_H"""
		return self.read(REG.GYRO_YOUT_H, 8)
	
	# Bits GYRO_YOUT_H
	# High Byte of Gyroscope Y-axis data. 
	# Register GYRO_YOUT_L
	# type USR0, bank 0 
	
	def setGYRO_YOUT_L(self, val):
		"""Set register GYRO_YOUT_L"""
		self.write(REG.GYRO_YOUT_L, val, 8)
	
	def getGYRO_YOUT_L(self):
		"""Get register GYRO_YOUT_L"""
		return self.read(REG.GYRO_YOUT_L, 8)
	
	# Bits GYRO_YOUT_L
	# Low Byte of Gyroscope Y-axis data.
	#           To convert the output of the gyroscope to angular rate measurement use the
	#           formula below:
	#           Y_angular_rate = GYRO_YOUT/Gyro_Sensitivity 
	
	# Register GYRO_ZOUT_H
	# type USR0, bank 0 
	
	def setGYRO_ZOUT_H(self, val):
		"""Set register GYRO_ZOUT_H"""
		self.write(REG.GYRO_ZOUT_H, val, 8)
	
	def getGYRO_ZOUT_H(self):
		"""Get register GYRO_ZOUT_H"""
		return self.read(REG.GYRO_ZOUT_H, 8)
	
	# Bits GYRO_ZOUT_H
	# High Byte of Gyroscope Z-axis data. 
	# Register GYRO_ZOUT_L
	# type USR0, bank 0 
	
	def setGYRO_ZOUT_L(self, val):
		"""Set register GYRO_ZOUT_L"""
		self.write(REG.GYRO_ZOUT_L, val, 8)
	
	def getGYRO_ZOUT_L(self):
		"""Get register GYRO_ZOUT_L"""
		return self.read(REG.GYRO_ZOUT_L, 8)
	
	# Bits GYRO_ZOUT_L
	# Low Byte of Gyroscope Z-axis data.
	#           To convert the output of the gyroscope to angular rate measurement use the
	#           formula below:
	#           Z_angular_rate = GYRO_ZOUT/Gyro_Sensitivity 
	
	# Register TEMP_OUT_H
	# type USR0, bank 0 
	
	def setTEMP_OUT_H(self, val):
		"""Set register TEMP_OUT_H"""
		self.write(REG.TEMP_OUT_H, val, 8)
	
	def getTEMP_OUT_H(self):
		"""Get register TEMP_OUT_H"""
		return self.read(REG.TEMP_OUT_H, 8)
	
	# Bits TEMP_OUT_H
	# High Byte of Temp sensor data. 
	# Register TEMP_OUT_L
	# type USR0, bank 0 
	
	def setTEMP_OUT_L(self, val):
		"""Set register TEMP_OUT_L"""
		self.write(REG.TEMP_OUT_L, val, 8)
	
	def getTEMP_OUT_L(self):
		"""Get register TEMP_OUT_L"""
		return self.read(REG.TEMP_OUT_L, 8)
	
	# Bits TEMP_OUT_L
	# Low Byte of Temp sensor data.
	#           To convert the output of the temperature sensor to degrees C use the following
	#           formula:
	#           TEMP_degC = ((TEMP_OUT - RoomTemp_Offset)/Temp_Sensitivity) + 21degC 
	
	# Register EXT_SLV_SENS_DATA_00
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_00(self, val):
		"""Set register EXT_SLV_SENS_DATA_00"""
		self.write(REG.EXT_SLV_SENS_DATA_00, val, 8)
	
	def getEXT_SLV_SENS_DATA_00(self):
		"""Get register EXT_SLV_SENS_DATA_00"""
		return self.read(REG.EXT_SLV_SENS_DATA_00, 8)
	
	# Bits EXT_SLV_SENS_DATA_00
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_01
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_01(self, val):
		"""Set register EXT_SLV_SENS_DATA_01"""
		self.write(REG.EXT_SLV_SENS_DATA_01, val, 8)
	
	def getEXT_SLV_SENS_DATA_01(self):
		"""Get register EXT_SLV_SENS_DATA_01"""
		return self.read(REG.EXT_SLV_SENS_DATA_01, 8)
	
	# Bits EXT_SLV_SENS_DATA_01
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_02
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_02(self, val):
		"""Set register EXT_SLV_SENS_DATA_02"""
		self.write(REG.EXT_SLV_SENS_DATA_02, val, 8)
	
	def getEXT_SLV_SENS_DATA_02(self):
		"""Get register EXT_SLV_SENS_DATA_02"""
		return self.read(REG.EXT_SLV_SENS_DATA_02, 8)
	
	# Bits EXT_SLV_SENS_DATA_02
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_03
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_03(self, val):
		"""Set register EXT_SLV_SENS_DATA_03"""
		self.write(REG.EXT_SLV_SENS_DATA_03, val, 8)
	
	def getEXT_SLV_SENS_DATA_03(self):
		"""Get register EXT_SLV_SENS_DATA_03"""
		return self.read(REG.EXT_SLV_SENS_DATA_03, 8)
	
	# Bits EXT_SLV_SENS_DATA_03
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_04
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_04(self, val):
		"""Set register EXT_SLV_SENS_DATA_04"""
		self.write(REG.EXT_SLV_SENS_DATA_04, val, 8)
	
	def getEXT_SLV_SENS_DATA_04(self):
		"""Get register EXT_SLV_SENS_DATA_04"""
		return self.read(REG.EXT_SLV_SENS_DATA_04, 8)
	
	# Bits EXT_SLV_SENS_DATA_04
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_05
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_05(self, val):
		"""Set register EXT_SLV_SENS_DATA_05"""
		self.write(REG.EXT_SLV_SENS_DATA_05, val, 8)
	
	def getEXT_SLV_SENS_DATA_05(self):
		"""Get register EXT_SLV_SENS_DATA_05"""
		return self.read(REG.EXT_SLV_SENS_DATA_05, 8)
	
	# Bits EXT_SLV_SENS_DATA_05
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_06
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_06(self, val):
		"""Set register EXT_SLV_SENS_DATA_06"""
		self.write(REG.EXT_SLV_SENS_DATA_06, val, 8)
	
	def getEXT_SLV_SENS_DATA_06(self):
		"""Get register EXT_SLV_SENS_DATA_06"""
		return self.read(REG.EXT_SLV_SENS_DATA_06, 8)
	
	# Bits EXT_SLV_SENS_DATA_06
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_07
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_07(self, val):
		"""Set register EXT_SLV_SENS_DATA_07"""
		self.write(REG.EXT_SLV_SENS_DATA_07, val, 8)
	
	def getEXT_SLV_SENS_DATA_07(self):
		"""Get register EXT_SLV_SENS_DATA_07"""
		return self.read(REG.EXT_SLV_SENS_DATA_07, 8)
	
	# Bits EXT_SLV_SENS_DATA_07
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_08
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_08(self, val):
		"""Set register EXT_SLV_SENS_DATA_08"""
		self.write(REG.EXT_SLV_SENS_DATA_08, val, 8)
	
	def getEXT_SLV_SENS_DATA_08(self):
		"""Get register EXT_SLV_SENS_DATA_08"""
		return self.read(REG.EXT_SLV_SENS_DATA_08, 8)
	
	# Bits EXT_SLV_SENS_DATA_08
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_09
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_09(self, val):
		"""Set register EXT_SLV_SENS_DATA_09"""
		self.write(REG.EXT_SLV_SENS_DATA_09, val, 8)
	
	def getEXT_SLV_SENS_DATA_09(self):
		"""Get register EXT_SLV_SENS_DATA_09"""
		return self.read(REG.EXT_SLV_SENS_DATA_09, 8)
	
	# Bits EXT_SLV_SENS_DATA_09
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_10
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_10(self, val):
		"""Set register EXT_SLV_SENS_DATA_10"""
		self.write(REG.EXT_SLV_SENS_DATA_10, val, 8)
	
	def getEXT_SLV_SENS_DATA_10(self):
		"""Get register EXT_SLV_SENS_DATA_10"""
		return self.read(REG.EXT_SLV_SENS_DATA_10, 8)
	
	# Bits EXT_SLV_SENS_DATA_10
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_11
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_11(self, val):
		"""Set register EXT_SLV_SENS_DATA_11"""
		self.write(REG.EXT_SLV_SENS_DATA_11, val, 8)
	
	def getEXT_SLV_SENS_DATA_11(self):
		"""Get register EXT_SLV_SENS_DATA_11"""
		return self.read(REG.EXT_SLV_SENS_DATA_11, 8)
	
	# Bits EXT_SLV_SENS_DATA_11
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_12
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_12(self, val):
		"""Set register EXT_SLV_SENS_DATA_12"""
		self.write(REG.EXT_SLV_SENS_DATA_12, val, 8)
	
	def getEXT_SLV_SENS_DATA_12(self):
		"""Get register EXT_SLV_SENS_DATA_12"""
		return self.read(REG.EXT_SLV_SENS_DATA_12, 8)
	
	# Bits EXT_SLV_SENS_DATA_12
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_13
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_13(self, val):
		"""Set register EXT_SLV_SENS_DATA_13"""
		self.write(REG.EXT_SLV_SENS_DATA_13, val, 8)
	
	def getEXT_SLV_SENS_DATA_13(self):
		"""Get register EXT_SLV_SENS_DATA_13"""
		return self.read(REG.EXT_SLV_SENS_DATA_13, 8)
	
	# Bits EXT_SLV_SENS_DATA_13
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_14
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_14(self, val):
		"""Set register EXT_SLV_SENS_DATA_14"""
		self.write(REG.EXT_SLV_SENS_DATA_14, val, 8)
	
	def getEXT_SLV_SENS_DATA_14(self):
		"""Get register EXT_SLV_SENS_DATA_14"""
		return self.read(REG.EXT_SLV_SENS_DATA_14, 8)
	
	# Bits EXT_SLV_SENS_DATA_14
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_15
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_15(self, val):
		"""Set register EXT_SLV_SENS_DATA_15"""
		self.write(REG.EXT_SLV_SENS_DATA_15, val, 8)
	
	def getEXT_SLV_SENS_DATA_15(self):
		"""Get register EXT_SLV_SENS_DATA_15"""
		return self.read(REG.EXT_SLV_SENS_DATA_15, 8)
	
	# Bits EXT_SLV_SENS_DATA_15
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_16
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_16(self, val):
		"""Set register EXT_SLV_SENS_DATA_16"""
		self.write(REG.EXT_SLV_SENS_DATA_16, val, 8)
	
	def getEXT_SLV_SENS_DATA_16(self):
		"""Get register EXT_SLV_SENS_DATA_16"""
		return self.read(REG.EXT_SLV_SENS_DATA_16, 8)
	
	# Bits EXT_SLV_SENS_DATA_16
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_17
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_17(self, val):
		"""Set register EXT_SLV_SENS_DATA_17"""
		self.write(REG.EXT_SLV_SENS_DATA_17, val, 8)
	
	def getEXT_SLV_SENS_DATA_17(self):
		"""Get register EXT_SLV_SENS_DATA_17"""
		return self.read(REG.EXT_SLV_SENS_DATA_17, 8)
	
	# Bits EXT_SLV_SENS_DATA_17
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_18
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_18(self, val):
		"""Set register EXT_SLV_SENS_DATA_18"""
		self.write(REG.EXT_SLV_SENS_DATA_18, val, 8)
	
	def getEXT_SLV_SENS_DATA_18(self):
		"""Get register EXT_SLV_SENS_DATA_18"""
		return self.read(REG.EXT_SLV_SENS_DATA_18, 8)
	
	# Bits EXT_SLV_SENS_DATA_18
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_19
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_19(self, val):
		"""Set register EXT_SLV_SENS_DATA_19"""
		self.write(REG.EXT_SLV_SENS_DATA_19, val, 8)
	
	def getEXT_SLV_SENS_DATA_19(self):
		"""Get register EXT_SLV_SENS_DATA_19"""
		return self.read(REG.EXT_SLV_SENS_DATA_19, 8)
	
	# Bits EXT_SLV_SENS_DATA_19
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_20
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_20(self, val):
		"""Set register EXT_SLV_SENS_DATA_20"""
		self.write(REG.EXT_SLV_SENS_DATA_20, val, 8)
	
	def getEXT_SLV_SENS_DATA_20(self):
		"""Get register EXT_SLV_SENS_DATA_20"""
		return self.read(REG.EXT_SLV_SENS_DATA_20, 8)
	
	# Bits EXT_SLV_SENS_DATA_20
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_21
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_21(self, val):
		"""Set register EXT_SLV_SENS_DATA_21"""
		self.write(REG.EXT_SLV_SENS_DATA_21, val, 8)
	
	def getEXT_SLV_SENS_DATA_21(self):
		"""Get register EXT_SLV_SENS_DATA_21"""
		return self.read(REG.EXT_SLV_SENS_DATA_21, 8)
	
	# Bits EXT_SLV_SENS_DATA_21
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_22
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_22(self, val):
		"""Set register EXT_SLV_SENS_DATA_22"""
		self.write(REG.EXT_SLV_SENS_DATA_22, val, 8)
	
	def getEXT_SLV_SENS_DATA_22(self):
		"""Get register EXT_SLV_SENS_DATA_22"""
		return self.read(REG.EXT_SLV_SENS_DATA_22, 8)
	
	# Bits EXT_SLV_SENS_DATA_22
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register EXT_SLV_SENS_DATA_23
	# type USR0, bank 0 
	
	def setEXT_SLV_SENS_DATA_23(self, val):
		"""Set register EXT_SLV_SENS_DATA_23"""
		self.write(REG.EXT_SLV_SENS_DATA_23, val, 8)
	
	def getEXT_SLV_SENS_DATA_23(self):
		"""Get register EXT_SLV_SENS_DATA_23"""
		return self.read(REG.EXT_SLV_SENS_DATA_23, 8)
	
	# Bits EXT_SLV_SENS_DATA_23
	# Sensor data read from external I2C devices via the I2C master interface. The data
	#           stored is controlled by the I2C_SLV(0-4)_ADDR, I2C_SLV(0-4)_REG, and I2C_SLV(0-
	#           4)_CTRL registers. 
	
	# Register FIFO_EN_1
	# type USR0, bank 0 
	
	def setFIFO_EN_1(self, val):
		"""Set register FIFO_EN_1"""
		self.write(REG.FIFO_EN_1, val, 8)
	
	def getFIFO_EN_1(self):
		"""Get register FIFO_EN_1"""
		return self.read(REG.FIFO_EN_1, 8)
	
	# Bits reserved_0
	# Bits SLV_3_FIFO_EN
	# 1 - Write EXT_SENS_DATA registers associated to SLV_3 (as determined by
	#           I2C_SLV2_CTRL, I2C_SLV1_CTRL, and I2C_SL20_CTRL)  to the FIFO at the sample rate;
	#           0 - Function is disabled. 
	
	# Bits SLV_2_FIFO_EN
	# 1 - Write EXT_SENS_DATA registers associated to SLV_2 (as determined by
	#           I2C_SLV0_CTRL, I2C_SLV1_CTRL, and I2C_SL20_CTRL)  to the FIFO at the sample rate;
	#           0 - Function is disabled. 
	
	# Bits SLV_1_FIFO_EN
	# 1 - Write EXT_SENS_DATA registers associated to SLV_1 (as determined by
	#           I2C_SLV0_CTRL and I2C_SLV1_CTRL)  to the FIFO at the sample rate;
	#           0 - Function is disabled. 
	
	# Bits SLV_0_FIFO_EN
	# 1 - Write EXT_SENS_DATA registers associated to SLV_0 (as determined by
	#           I2C_SLV0_CTRL)  to the FIFO at the sample rate;
	#           0 - Function is disabled. 
	
	# Register FIFO_EN_2
	# type USR0, bank 0 
	
	def setFIFO_EN_2(self, val):
		"""Set register FIFO_EN_2"""
		self.write(REG.FIFO_EN_2, val, 8)
	
	def getFIFO_EN_2(self):
		"""Get register FIFO_EN_2"""
		return self.read(REG.FIFO_EN_2, 8)
	
	# Bits reserved_0
	# Bits ACCEL_FIFO_EN
	# 1 - Write ACCEL_XOUT_H, ACCEL_XOUT_L, ACCEL_YOUT_H, ACCEL_YOUT_L,
	#           ACCEL_ZOUT_H, and ACCEL_ZOUT_L to the FIFO at the sample rate;
	#           0 - Function is disabled. 
	
	# Bits GYRO_Z_FIFO_EN
	# 1 - Write GYRO_ZOUT_H and GYRO_ZOUT_L to the FIFO at the sample rate.
	#           0 - Function is disabled. 
	
	# Bits GYRO_Y_FIFO_EN
	# 1 - Write GYRO_YOUT_H and GYRO_YOUT_L to the FIFO at the sample rate.
	#           0 - Function is disabled. 
	
	# Bits GYRO_X_FIFO_EN
	# 1 - Write GYRO_XOUT_H and GYRO_XOUT_L to the FIFO at the sample rate.
	#           0 - Function is disabled. 
	
	# Bits TEMP_FIFO_EN
	# 1 - Write TEMP_OUT_H and TEMP_OUT_L to the FIFO at the sample rate.
	#           0 - Function is disabled. 
	
	# Register FIFO_RST
	# type USR0, bank 0 
	
	def setFIFO_RST(self, val):
		"""Set register FIFO_RST"""
		self.write(REG.FIFO_RST, val, 8)
	
	def getFIFO_RST(self):
		"""Get register FIFO_RST"""
		return self.read(REG.FIFO_RST, 8)
	
	# Bits reserved_0
	# Bits FIFO_RESET
	# S/W FIFO reset.  Assert and hold to set FIFO size to 0. Assert and de-assert to reset
	#           FIFO. 
	
	# Register FIFO_MODE
	# type USR0, bank 0 
	
	def setFIFO_MODE(self, val):
		"""Set register FIFO_MODE"""
		self.write(REG.FIFO_MODE, val, 8)
	
	def getFIFO_MODE(self):
		"""Get register FIFO_MODE"""
		return self.read(REG.FIFO_MODE, 8)
	
	# Bits reserved_0
	# Bits FIFO_MODE
	# 0 - Stream.
	#           1 - Snapshot.
	#           When set to ‘1’, when the FIFO is full, additional writes will not be written to FIFO.
	#           When set to ‘0’, when the FIFO is full, additional writes will be written to the FIFO,
	#           replacing the oldest data. 
	
	# Register FIFO_COUNTH
	# type USR0, bank 0 
	
	def setFIFO_COUNTH(self, val):
		"""Set register FIFO_COUNTH"""
		self.write(REG.FIFO_COUNTH, val, 8)
	
	def getFIFO_COUNTH(self):
		"""Get register FIFO_COUNTH"""
		return self.read(REG.FIFO_COUNTH, 8)
	
	# Bits reserved_0
	# Bits FIFO_CNT
	# High Bits, count indicates the number of written bytes in the FIFO.
	#           Reading this byte latches the data for both FIFO_COUNTH, and FIFO_COUNTL. 
	
	# Register FIFO_COUNTL
	# type USR0, bank 0 
	
	def setFIFO_COUNTL(self, val):
		"""Set register FIFO_COUNTL"""
		self.write(REG.FIFO_COUNTL, val, 8)
	
	def getFIFO_COUNTL(self):
		"""Get register FIFO_COUNTL"""
		return self.read(REG.FIFO_COUNTL, 8)
	
	# Bits FIFO_CNT
	# Low bits, count indicates the number of written bytes in the FIFO. 
	# Register FIFO_R_W
	# type USR0, bank 0 
	
	def setFIFO_R_W(self, val):
		"""Set register FIFO_R_W"""
		self.write(REG.FIFO_R_W, val, 8)
	
	def getFIFO_R_W(self):
		"""Get register FIFO_R_W"""
		return self.read(REG.FIFO_R_W, 8)
	
	# Bits FIFO_R_W
	# Reading from or writing to this register actually reads/writes the FIFO. For example,
	#           to write a byte to the FIFO, write the desired byte value to FIFO_R_W[7:0]. To read a
	#           byte from the FIFO, perform a register read operation and access the result in
	#           FIFO_R_W[7:0]. 
	
	# Register DATA_RDY_STATUS
	# type USR0, bank 0 
	
	def setDATA_RDY_STATUS(self, val):
		"""Set register DATA_RDY_STATUS"""
		self.write(REG.DATA_RDY_STATUS, val, 8)
	
	def getDATA_RDY_STATUS(self):
		"""Get register DATA_RDY_STATUS"""
		return self.read(REG.DATA_RDY_STATUS, 8)
	
	# Bits WOF_STATUS
	# Wake on FSYNC interrupt status. Cleared on read. 
	# Bits reserved_0
	# Bits RAW_DATA_RDY
	# Data from sensors is copied to FIFO or SRAM.
	#           Set when sequence controller kicks off on a sensor data load. Only bit 0 is relevant in
	#           a single FIFO configuration. Cleared on read. 
	
	# Register FIFO_CFG
	# type USR0, bank 0 
	
	def setFIFO_CFG(self, val):
		"""Set register FIFO_CFG"""
		self.write(REG.FIFO_CFG, val, 8)
	
	def getFIFO_CFG(self):
		"""Get register FIFO_CFG"""
		return self.read(REG.FIFO_CFG, 8)
	
	# Bits reserved_0
	# Bits FIFO_CFG
	# This bit should be set to 1 if interrupt status for each sensor is required. 
	# Register REG_BANK_SEL
	# type ALL, bank 0 
	
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

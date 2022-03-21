# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:08:47 2020

@author: Ilya
"""


'''
NOTE that positions are in steps 2.5 micron each!
'''


from PyQt5.QtCore import QObject,  pyqtSignal
import sys
import os
import numpy as np
import time
from ctypes import (
    c_short,
    c_int,
    c_char_p,
    byref,
)
if __name__ == "__main__":
    os.chdir('..')
from Hardware.thorlabs_kinesis import benchtop_stepper_motor as bsm
from Hardware.thorlabs_kinesis import KCube_DC_Servo as kdc
    

tolerance=5


class ThorlabsStages(QObject):
    connected = pyqtSignal()
    stopped = pyqtSignal()
#    StepSize={'X':10,'Y':10,'Z':10}
    Stage_key={'X':None,'Y':None,'Z':None}
    abs_position={'X':0,'Y':0,'Z':0}
    relative_position={'X':0,'Y':0,'Z':0}
    zero_position={'X':0,'Y':0,'Z':0}
    
    def __init__(self):
        super().__init__()
        self._short_pause=0.1
        self._serial_no_x = c_char_p(bytes("27254353", "utf-8"))
        self.milliseconds = c_int(100)
        kdc.TLI_BuildDeviceList()
        # kdc.CC_StartPolling(self._serial_no_x, milliseconds)
        err=kdc.CC_Open(self._serial_no_x)
        time.sleep(self._short_pause)
        if err==0:
            print('connected to 27254353 ')
            self.isConnected=1
            self.abs_position['X']=(kdc.CC_GetPosition(self._serial_no_x))
        else:
            print('Error: not connected to 27254353 ')
        self._serial_no_z = c_char_p(bytes("70864299", "utf-8"))
        self.channel_z=c_short(2)
        bsm.TLI_BuildDeviceList()
        err=bsm.SBC_Open(self._serial_no_z)
        time.sleep(self._short_pause)
        
        if err==0:
            print('connected to 70864299 ')
            self.isConnected=1
            self.abs_position['Z']=(bsm.SBC_GetPosition(self._serial_no_z,self.channel_z))
            bsm.SBC_SetBacklash(self._serial_no_z,self.channel_z,c_int(0))
        else:
            print('Error: not connected to 70864299 ')


        # try:
        #     self.abs_position['X']=self.get_position('X')
        #     self.abs_position['Z']=self.get_position('Z')
        # except Exception as e:
        #     print('cannot take positions of stages: ' + str(e))
        

        self.update_relative_positions()

    
    
    def set_zero_positions(self,l):
        self.zero_position['X']=l[0]
        self.zero_position['Z']=l[2]
        self.update_relative_positions()
    
    def update_relative_positions(self):
        self.relative_position['X']=self.abs_position['X']-self.zero_position['X']
        self.relative_position['Z']=self.abs_position['Z']-self.zero_position['Z']
        
    def get_position(self, key):
        #for the sage of uniformity, distance is shown in steps 2.5 um each
        if key=='X':
            time.sleep(self._short_pause)
            return int(kdc.CC_GetPosition(self._serial_no_x))
        if key=='Z':
            time.sleep(self._short_pause)
            return int(bsm.SBC_GetPosition(self._serial_no_z,self.channel_z))
        if key=='Y':
            return 0
    
    def move_home(self):
        kdc.CC_StartPolling(self._serial_no_x, self.milliseconds)
        kdc.CC_ClearMessageQueue(self._serial_no_x)
        err1 = kdc.CC_Home(self._serial_no_x)
        time.sleep(0.2)
        if err1 == 0:
            while True:
                time.sleep(1)
                current_pos = int(kdc.CC_GetPosition(self._serial_no_x))
                if current_pos == 0:
                    print("At home.")
                    break
                else:
                    print(f"Homing...{current_pos}")
        kdc.CC_StopPolling(self._serial_no_x)  
        self.abs_position['X']=self.get_position('X')
        
        bsm.SBC_StartPolling(self._serial_no_z, self.channel_z, self.milliseconds)
        bsm.SBC_ClearMessageQueue(self._serial_no_z, self.channel_z)
        err = bsm.SBC_Home(self._serial_no_z,self.channel_z)
        
        time.sleep(0.2)
        if err == 0:
            while True:
                current_pos = int(bsm.SBC_GetPosition(self._serial_no_z,self.channel_z))
                time.sleep(1)
                if current_pos == 0:
                    print("At home.")
                    break
                else:
                    print(f"Homing...{current_pos}")
        bsm.SBC_StopPolling(self._serial_no_z, self.channel_z)
        self.abs_position['Z']=self.get_position('Z')
        self.update_relative_positions()
        self.stopped.emit()
        
    def get_positions(self):
        pos={}
        for K in self.Stage_key:
            pos[K]=self.get_position(K)
        return pos
    
    def shiftOnArbitrary(self, key:str, distance:int,blocking=True):
                #for the sage of uniformity, distance is taken in steps 2.5 um each
        if key=='X':
            kdc.CC_StartPolling(self._serial_no_x, self.milliseconds)
            kdc.CC_ClearMessageQueue(self._serial_no_x)
            time.sleep(self._short_pause)
            init_pos=int(kdc.CC_GetPosition(self._serial_no_x))
            kdc.CC_SetMoveRelativeDistance(self._serial_no_x, c_int(distance))
            kdc.CC_MoveRelativeDistance(self._serial_no_x)
            
            if blocking:
                pos=0
                while not abs(pos - distance-init_pos)<tolerance:
                    pos = int(kdc.CC_GetPosition(self._serial_no_x))
                    time.sleep(self._short_pause)
                    print(pos,init_pos,distance+init_pos,pos == distance+init_pos)
            kdc.CC_StopPolling(self._serial_no_x)  
                    
        if key=='Z':
            bsm.SBC_StartPolling(self._serial_no_z, self.channel_z, self.milliseconds)
            bsm.SBC_ClearMessageQueue(self._serial_no_z, self.channel_z)
            init_pos=int(bsm.SBC_GetPosition(self._serial_no_z,self.channel_z))
            time.sleep(self._short_pause)
                
            bsm.SBC_SetMoveRelativeDistance(self._serial_no_z, self.channel_z,c_int(distance))
            bsm.SBC_MoveRelativeDistance(self._serial_no_z,self.channel_z)
            
            if blocking:
                pos=0
                while not abs(pos - distance-init_pos)<tolerance:
                    pos = int(bsm.SBC_GetPosition(self._serial_no_z,self.channel_z))
                    time.sleep(self._short_pause)
                    print(pos,init_pos,distance+init_pos,pos == distance+init_pos)
            bsm.SBC_StopPolling(self._serial_no_z, self.channel_z) 
        self.abs_position[key]=self.get_position(key)
        self.update_relative_positions()
        self.stopped.emit()
            
    def shiftAbsolute(self, key:str, move_to:int):
        #for the sage of uniformity, distance is taken in steps 2.5 um each
        if key=='X':
            # kdc.CC_SetMoveRelativeDistance(self._serial_no_x, c_int(distance))
            # kdc.CC_MoveRelative(self._serial_no_x)
            # kdc.CC_MoveRelativeDistance(self._serial_no_x)
            kdc.CC_SetMoveAbsolutePosition(self._serial_no_x, c_int(move_to))
            time.sleep(0.2)
            kdc.CC_MoveAbsolute(self._serial_no_x)
#        if (result>-1):
        # self.abs_position[key]=self.get_position(key)
        # self.update_relative_positions()
        # self.stopped.emit()



#    def wait_for_stop(self, device_id, interval):
#        print("\nWaiting for stop")
#        result = self.lib.command_wait_for_stop(device_id, interval)
#        print("Result: " + repr(result+1))


    def __del__(self):
        kdc.CC_Close(self._serial_no_x)



if __name__ == "__main__":
    stages=ThorlabsStages()
    print(stages.get_position('X'))
    a=stages.get_position('Z')
    d=-200
    # stages.shiftOnArbitrary('Z', d,True)
    # print(stages.get_position('X'))
    # print(stages.get_position('Z'))
    stages.shiftOnArbitrary('Z', d,True)
    b=stages.get_position('Z')
    print(b,a,b-a)

    # del stages

#################################### CLOSE CONNECTION #######################################



#plt.grid(True)
#plt.plot(Data[1], Data[0])
#plt.xlabel("Wavelength (nm)")
#plt.ylabel("Power (dBm)")
#plt.show()

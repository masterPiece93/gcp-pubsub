"""
This script is depicting a complex process .
"""
import datetime
import time
import multiprocessing
from zoneinfo import ZoneInfo
from enum import Enum
from datetime import datetime
from zoneinfo import ZoneInfo


class ComplexProcess:
    """
    mimicing a complex process
    - CPU intensive
    - IO intensive
    """

    class P_Type(str, Enum):
        CPU_INTENSIVE=1
        IO_INTENSIVE=2
    
    def __init__(self, name: str, process_type:str = P_Type.CPU_INTENSIVE, ):
        self._name = name
        self._process_type=process_type
    
    def run(self, *args, **kwargs):
        if self._name == "linear" and self._process_type == self.P_Type.CPU_INTENSIVE:
            return self._linear_complex_process(*args, **kwargs)
        if self._name == "py_multiprocess" and self._process_type == self.P_Type.CPU_INTENSIVE:
            ...
        if self._name == "dask" and self._process_type == self.P_Type.CPU_INTENSIVE:
            ...
    
    def _linear_complex_process(self, message_id: str, message_data: dict) -> None:
        """
        a simple process using time module.
        - writes timer info on a file named with process-id
            - filename : process_<message-id>.txt
        """
        process_file = open(f'process_{message_id}.txt', 'w+')
        process_file.close()

        try:
            seconds = 0
            while True:
                with open(f'process_{message_id}.txt', 'a') as f:
                    print(f"{datetime.now(ZoneInfo("Asia/Kolkata")).strftime("[%I:%M:%S-%p]")} | timer:{seconds}",file=f)
                if seconds == message_data["duration"]:
                    break
                time.sleep(1.0)
                seconds += 1
        except:
            ...
            # reraise : if the callback is handling .
            # OR
            # handle
        else:
            # Thread 1 : publish to another `topic` with bucket path
            # Thread 2 : update `metadata` to bucket on same path
            # Thread 3 : etc etc etc ... do any residual task here
            ...
            # if certain event occurs here ( like if you feel you are not able to forward the results to a service or save to DB ) ,
            ## then you may Rasie a specific type of exception , that can indicate the callback to UnAcknowledge the message .
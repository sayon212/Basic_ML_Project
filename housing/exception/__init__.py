import os
import sys

# Write custom Exception by inheriting some features from System defined Exception class
class HousingException(Exception):
    
    def __init__(self, error_message:Exception , error_detail:sys):
                     # object of exception     , object of sys
        # this error_message and details will come from the .py file as parameter while invoking it.
        
        super().__init__(error_message)
        # sending back the error message to class

        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail
                                                                    )
        '''
        It is calling the get_detailed_error_message function which constructs a 
        detailed string stating where the error occurred at what line. It takes
        exception and sys as input params.
        '''

    @staticmethod # can ignore this also. it will work.
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        _ , _ ,exec_tb = error_detail.exc_info()

        '''
        When we are calling this class we are calling like HouseException(e,sys).
        So error_details is mapped with sys and Exception is mapped with e from the main
        .py file . The exec_info has all details like line number, file name of the 
        recent exception in trackback (tb) module.
        '''

        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        return error_message

        '''
        Even if we dont write below lines then also it is working
        str function defines what should be displayed when we print the object
        like print(HousingException) and repr is representation. Check in
        Jupyter notebook
        '''
    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return HousingException.__name__.str()
import inspect
import logging

class LogGenerator:
    @staticmethod
    def logger():
         Name= inspect.stack()[1][3]    #  <-- It is for class name.
         Logger = logging.getLogger(Name)
         Logfile = logging.FileHandler("G:\Python\OrangeHRM\Logs\\OrangeHRM_Automation.log")
         Format = logging.Formatter("%(asctime)s : %(levelname)s : %(filename)s: %(name)s : %(funcName)s : %(lineno)d : %(message)s:")
         Logfile.setFormatter(Format)
         Logger.addHandler(Logfile)
         Logger.setLevel(logging.INFO)  # There are few levels,select which is needed and there below levels automaticlly with it.
         return Logger





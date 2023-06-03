from logging import debug, info, warning, error, critical, basicConfig
class Logging:
    def __init__(self, message = ""):
        self.Message = message
    def LogConfig(self):
        def Wrapper(*args, **kwargs):
            fileName = "filelog.log"
            self.Message = args[2]
            if (self.Message == "" or self.Message == None):
                raise TypeError("Value cann't be None or empty")
            format = "%(asctime)s : %(levelname)s - %(message)s"
            basicConfig(level=args[1], format=format, filename=fileName, filemode='a')
            match args[1]:
                case 10:
                    debug(self.Message)
                case 20:
                    info(self.Message)
                case 30:
                    warning(self.Message)
                case 40:
                    error(self.Message)
                case 50:
                    critical(self.Message)
        return Wrapper
    @LogConfig
    def Log(self, loglevel, message):
        self.Message = message
        return self

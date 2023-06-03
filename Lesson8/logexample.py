from logging import debug, info, warning, error, critical, basicConfig, \
    DEBUG, ERROR, WARNING, INFO, CRITICAL
class Logging:
    def __init__(self, message = ""):
        self.Message = message
    def __str__(self):
        if(self.Message == "" or self.Message == None):
            raise TypeError("Value cann't be None or empty")
        return self.Message
    def LogConfig(self, loginLevel = DEBUG):
                fileName = "filelog.log"
                level = DEBUG
                format = "%(asctime)s : %(levelname)s - %(message)s"
                match loginLevel:
                    case 10:
                        level = DEBUG
                        basicConfig(level=level, format=format, filename=fileName, filemode='a')
                        debug(self.__str__())
                    case 20:
                        level = INFO
                        basicConfig(level=level, format=format, filename=fileName, filemode='a')
                        info(self.__str__())
                    case 30:
                        level = WARNING
                        basicConfig(level=level, format=format, filename=fileName, filemode='a')
                        warning(self.__str__())
                    case 40:
                        level = ERROR
                        basicConfig(level=level, format=format, filename=fileName, filemode='a')
                        error(self.__str__())
                    case 50:
                        level = CRITICAL
                        basicConfig(level=level, format=format, filename=fileName, filemode='a')
                        critical(self.__str__())
    def Log(self, loginLevel):
        self.LogConfig(loginLevel)

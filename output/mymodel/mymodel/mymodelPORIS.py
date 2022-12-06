from PORIS import *

class mymodelPORIS:
    def __init__(self):
        idcounter = 1
        self.sysMyModel = PORISSys("MyModel")
        self.mdMyModelMode_UNKNOWN = PORISMode("MyModelMode_UNKNOWN")
        self.root = self.sysMyModel
        self.prDelta = PORISParam("Delta")
        self.mdDeltaMode_UNKNOWN = PORISMode("DeltaMode_UNKNOWN")
        self.vlDelta_UNKNOWN = PORISValue("Delta_UNKNOWN")
        self.mdMyModelMode_Coarse = PORISMode("MyModelMode_Coarse")
        self.mdMyModelMode_Fine = PORISMode("MyModelMode_Fine")
        self.vlDelta_Coarse = PORISValueFloat("Delta_Coarse")
        self.vlDelta_Fine = PORISValueFloat("Delta_Fine")
        self.mdDeltaMode_Coarse = PORISMode("DeltaMode_Coarse")
        self.mdDeltaMode_Fine = PORISMode("DeltaMode_Fine")
        self.mdMyModelMode_Engineering = PORISMode("MyModelMode_Engineering")

        self.sysMyModel.id = idcounter
        idcounter += 1
        self.sysMyModel.ident = "MyModel"
        self.sysMyModel.description = ""

        self.mdMyModelMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdMyModelMode_UNKNOWN.ident = "MyModelMode_UNKNOWN"
        self.mdMyModelMode_UNKNOWN.description = ""
        self.sysMyModel.addMode(self.mdMyModelMode_UNKNOWN)

        self.prDelta.id = idcounter
        idcounter += 1
        self.prDelta.ident = "Delta"
        self.prDelta.description = ""
        self.sysMyModel.addParam(self.prDelta)

        self.vlDelta_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlDelta_UNKNOWN.ident = "Delta_UNKNOWN"
        self.vlDelta_UNKNOWN.description = "Unknown value for Delta"
        self.prDelta.addValue(self.vlDelta_UNKNOWN)

        self.mdDeltaMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdDeltaMode_UNKNOWN.ident = "DeltaMode_UNKNOWN"
        self.mdDeltaMode_UNKNOWN.description = "Unknown mode for Delta"
        self.prDelta.addMode(self.mdDeltaMode_UNKNOWN)
        self.mdDeltaMode_UNKNOWN.addValue(self.vlDelta_UNKNOWN)
        self.mdMyModelMode_UNKNOWN.addSubMode(self.mdDeltaMode_UNKNOWN)

        self.mdMyModelMode_Coarse.id = idcounter
        idcounter += 1
        self.mdMyModelMode_Coarse.ident = "MyModelMode_Coarse"
        self.mdMyModelMode_Coarse.description = ""
        self.sysMyModel.addMode(self.mdMyModelMode_Coarse)

        self.mdMyModelMode_Fine.id = idcounter
        idcounter += 1
        self.mdMyModelMode_Fine.ident = "MyModelMode_Fine"
        self.mdMyModelMode_Fine.description = ""
        self.sysMyModel.addMode(self.mdMyModelMode_Fine)

        self.vlDelta_Coarse.id = idcounter
        idcounter += 1
        self.vlDelta_Coarse.ident = "Delta_Coarse"
        self.vlDelta_Coarse.description = ""
        self.vlDelta_Coarse.min = 0
        self.vlDelta_Coarse.default_data = 10
        self.vlDelta_Coarse.max = 500
        self.prDelta.addValue(self.vlDelta_Coarse)

        self.vlDelta_Fine.id = idcounter
        idcounter += 1
        self.vlDelta_Fine.ident = "Delta_Fine"
        self.vlDelta_Fine.description = ""
        self.vlDelta_Fine.min = 0
        self.vlDelta_Fine.default_data = 0.01
        self.vlDelta_Fine.max = 0.5
        self.prDelta.addValue(self.vlDelta_Fine)

        self.mdDeltaMode_Coarse.id = idcounter
        idcounter += 1
        self.mdDeltaMode_Coarse.ident = "DeltaMode_Coarse"
        self.mdDeltaMode_Coarse.description = ""
        self.prDelta.addMode(self.mdDeltaMode_Coarse)

        self.mdDeltaMode_Fine.id = idcounter
        idcounter += 1
        self.mdDeltaMode_Fine.ident = "DeltaMode_Fine"
        self.mdDeltaMode_Fine.description = ""
        self.prDelta.addMode(self.mdDeltaMode_Fine)

        self.mdMyModelMode_Engineering.id = idcounter
        idcounter += 1
        self.mdMyModelMode_Engineering.ident = "MyModelMode_Engineering"
        self.mdMyModelMode_Engineering.description = "MyModel engineering mode"
        self.sysMyModel.addMode(self.mdMyModelMode_Engineering)
        # Marcamos DeltaMode_Coarse como elegible para MyModelMode_Coarse
        self.mdMyModelMode_Coarse.addSubMode(self.mdDeltaMode_Coarse)
        # Marcamos DeltaMode_Fine como elegible para MyModelMode_Fine
        self.mdMyModelMode_Fine.addSubMode(self.mdDeltaMode_Fine)
        # Marcamos DeltaMode_Coarse como elegible para MyModelMode_Engineering
        self.mdMyModelMode_Engineering.addSubMode(self.mdDeltaMode_Coarse)
        # Marcamos DeltaMode_Fine como elegible para MyModelMode_Engineering
        self.mdMyModelMode_Engineering.addSubMode(self.mdDeltaMode_Fine)
        # Marcamos Delta_Coarse como elegible para DeltaMode_Coarse
        self.mdDeltaMode_Coarse.addValue(self.vlDelta_Coarse)
        # Marcamos Delta_Fine como elegible para DeltaMode_Fine
        self.mdDeltaMode_Fine.addValue(self.vlDelta_Fine)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## MyModelMode 
    def get_MyModelMode(self)-> PORISMode:
        return self.sysMyModel.selectedMode

    def set_MyModelMode(self, mode: PORISMode)-> PORISMode :
        return self.sysMyModel.setMode(mode)


    ## prParam Delta 

    # Delta
    def get_Delta(self)-> PORISValue :
        return self.prDelta.selectedValue

    def set_Delta(self, value: PORISValue)-> PORISValue :
        return self.prDelta.setValue(value)


    ## DeltaMode 
    def get_DeltaMode(self)-> PORISMode:
        return self.prDelta.selectedMode

    def set_DeltaMode(self, mode: PORISMode)-> PORISMode :
        return self.prDelta.setMode(mode)


    ## prParam MyModel 

    # DeltaDouble  
    def get_DeltaDouble(self)-> float :
        return self.prDelta.selectedValue.getData()

    def set_DeltaDouble(self, data: float)-> float :
        return self.prDelta.selectedValue.setData(data)


    ## prParam MyModel 

    # DeltaDouble  
    def get_DeltaDouble(self)-> float :
        return self.prDelta.selectedValue.getData()

    def set_DeltaDouble(self, data: float)-> float :
        return self.prDelta.selectedValue.setData(data)


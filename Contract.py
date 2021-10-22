import smartpy as sp

class DFIR(sp.Contract):
    def __init__(self):
        self.init(
            patientMap = sp.map(),    
        )
        

    @sp.entry_point       
    def addFir(self, params):
            uid = params.uid
            self.data.patientMap[uid] = sp.record(
            name = params.name, 
            fathersName=params.fathersName,
            age = params.age, 
            gender = params.gender, 
            PhoneNumber = params.PhoneNumber, 
            address = params.address,
            # Place of Occurrence: 
            # Distance from the police station 
            DisPs = params.DisPs,
            #Direction from the police station
            Dirps=params.Dirps,
           # Date and Hour of Occurrence: 
            Date1 = params.Date1,
            time=params.time,
            #offence
            NoO=params.NoO,
            Section=params.Section,
            #Particulars of the property
            pop=params.pop,
            #  Description of the accused:
            Doa=params.Doa,
            #Details of witnesses (if any) 
            Dow=params.Dow,
           # Complaint: Briefly lay down the facts regarding the incident reported in an accurate way. 
            Complaint = params.Complaint,
            
            
        )

@sp.add_test(name = "ADDING FIR ")
def test():
    scenario = sp.test_scenario()

    user = sp.test_account("Test")
    
    panjikaran1 = DFIR()
    scenario += panjikaran1
    
    scenario.h1("Reporting a FIR")
    scenario += panjikaran1.addFir(
        uid = "0123456789", 
        name = "Yuvraj Singh Deora", 
        fathersName="Samandar Singh",
        age = 20, 
        gender = "Male", 
        PhoneNumber = 6176179619, 
        address = "Rajput Vas Hadmatiya",
        # Place of Occurrence: 
            # Distance from the police station 
       DisPs = "25km",
            #Direction from the police station
            Dirps="North-East",
           # Date and Hour of Occurrence: 
            Date1 = "22/10/2021",
            time="15:00:56",
            #offence
            NoO="Murder",
            Section="IPC-305",
            #Particulars of the property
            pop="Samsun S30",
            #  Description of the accused:
            Doa="A scar on the face and a religious tatto on the right hand",
            #Details of witnesses (if any) 
            Dow="Shankar Prasad ",
           # Complaint: Briefly lay down the facts regarding the incident reported in an accurate way. 
            Complaint = "A man came from the van and suddenly attacked the lady who was nearby jogging on the road and again ran towaeds the car and got disappeared."
         
    )
    # scenario.show(vaxScene.balance)

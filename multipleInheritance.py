class TechnicalSkills:
    def code(self):
        print("Writes code.")
class CommunicationSkills:
    def present(self):
        print("Gives presentations.")
class TechLead(TechnicalSkills,CommunicationSkills):
    def lead_team(self):
        print("Leads the tech team.")
lead = TechLead()
lead.code()
lead.present()
lead.lead_team()

    
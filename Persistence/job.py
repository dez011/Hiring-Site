from pymongo import MongoClient


class JobObject:
    def __init__(self, jobName, jobRole, jobDescription, tech_skills, business_skills, attitude):
        self.jobName = jobName
        self.jobRole = jobRole
        self.jobDescription = jobDescription
        self.tech_skills = tech_skills
        self.business_skills = business_skills
        self.attitude = attitude
        self.bestMatch = ["Candidate1"]
        self.db = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.job

    def create(self):
        job_data = {
            'jobName': self.jobName,
            'jobRole': self.jobRole,
            'jobDescription': self.jobDescription,
            'tech_skills': self.tech_skills,
            'business_skills': self.business_skills,
            'attitude': self.attitude,
            'bestMatch': self.bestMatch,
        }
        self.db.insert_one(job_data)
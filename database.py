from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv

engine = create_engine('sqlite:///projects_db.sqlite') 
db_session = scoped_session(sessionmaker(bind=engine)) 
Base = declarative_base() 
Base.query = db_session.query_property() 


class Projects(Base):  
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    project_name = Column(String(50))
    project_description = Column(Text())
    project_city = Column(String(50))
    project_url = Column(String(50)) 

    def __init__(self, project_name=None, project_description=None, project_city=None, project_url=None): 
        self.project_name = project_name
        self.project_description = project_description
        self.project_city = project_city
        self.project_url = project_url

    def __repr__(self):
        return '<Event {} {} {} {}>'.format(self.project_name, self.project_description, self.project_city, self.project_url)

def init_db():
    Base.metadata.create_all(bind=engine)


def create_projects_list_from_csv():
    projects_list = []
    with open('projects.csv', 'r', encoding='utf-8-sig') as file:
        fields = ['ProjectName','Описание проекта','Город','Сайт']
        reader = csv.DictReader(file, fields, delimiter=';')
        for row in reader:
            projects_list.append(row)
        return projects_list


def remove_paragraph_symbols(): #remove \n from "описание проекта"
    repaired_projects_list = []
    for project in create_projects_list_from_csv():
        project["Описание проекта"] = project.get("Описание проекта").replace("\n","")
        repaired_projects_list.append(project) 
    return repaired_projects_list

def write_in_db():
    for project in remove_paragraph_symbols():
        project = Projects(project['ProjectName'],project['Описание проекта'],project['Город'],project['Сайт'] )
        db_session.add(project)

    db_session.commit()

def get_data(city):
    project_name = Projects.query.filter(Projects.project_city == city).all()
    print(project_name)


if __name__ == "__main__":
    init_db()
    remove_paragraph_symbols()
    write_in_db()
    try:
        while True:
            city = input("Enter city name: ")
    except EOFError:
        pass
    get_data(city)
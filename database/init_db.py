from database.schema_DB import *
from datetime import  datetime
import names
import random

# facultyITEM = ['ICOM', 'INEL', 'INSO', 'CIIC', ]
# fn = names.get_first_name()
# ln = names.get_last_name()
# emailc = fn + '.' + ln + "@upr.edu"
# collab1 = Collaborator(first_name = fn,
# last_name = ln,
# approved = random.choice([True, False]),
# faculty = random.choice(facultyITEM),
# banned = random.choice([True, False]),
# email = emailc
# )
# collab1.save()

# SAMPLES
# Damage types
damage_type = Damage()
damage_type.damageType=  "Terremoto"
damage_type.save()

damage_type = Damage()
damage_type.damageType=  "Huracan"
damage_type.save()

damage_type = Damage()
damage_type.damageType=  "Inundaciones"
damage_type.save()

damage_type = Damage()
damage_type.damageType=  "Alcantarillados"
damage_type.save()

# Infrastrucutres
infrastructure_types= Infrastructure()
infrastructure_types.infrastructureType = "Puertos"
infrastructure_types.save()

infrastructure_types= Infrastructure()
infrastructure_types.infrastructureType = "Puentes"
infrastructure_types.save()

infrastructure_types= Infrastructure()
infrastructure_types.infrastructureType = "Alambrado"
infrastructure_types.save()

infrastructure_types= Infrastructure()
infrastructure_types.infrastructureType = "Carreteras"
infrastructure_types.save()

# Tags
tag = Tag()
tag.tagItem="Volatil"
tag.save()

tag = Tag()
tag.tagItem="Renovable"
tag.save()

tag = Tag()
tag.tagItem="Sustento"
tag.save()

# Sample author
sample_author = Author()
sample_author.author_FN = "Author Name"
sample_author.author_LN = "Author Last Name"
sample_author.author_faculty = "ININ"
sample_author.author_email = "author@author.com"

# sample Actor
sample_actor = Actor()
sample_actor.actor_FN = "Actor FN"
sample_actor.actor_LN = "Actor LN"
sample_actor.role = "Gerente de Puertos"

# sample section
sample_section = Section()
sample_section.secTitle = 'Section Title'
sample_section.content = 'Section content here'

# sample timeline
sample_timeline_pair = Timeline()
sample_timeline_pair.event = 'Timeline event'
sample_timeline_pair.eventDate = datetime.today().strftime('%Y-%m-%d')

################################

collaborator1 = Collaborator()
collaborator1.first_name = 'Roberto'
collaborator1.last_name = 'Guzman'
collaborator1.email = 'roberto.guzman3@upr.edu'
collaborator1.faculty = 'ICOM'
collaborator1.banned = False
collaborator1.approved = True
collaborator1.save()

collaborator2 = Collaborator()
collaborator2.first_name = 'Jainel'
collaborator2.last_name = 'Torres'
collaborator2.email = 'jainel.torres@upr.edu'
collaborator2.faculty = 'ICOM'
collaborator2.banned = True
collaborator2.approved = True
collaborator2.save()

collaborator3 = Collaborator()
collaborator3.first_name = 'Alejandro'
collaborator3.last_name = 'Vasquez'
collaborator3.email = 'alejandro.vasquez@upr.edu'
collaborator3.faculty = 'ICOM'
collaborator3.banned = False
collaborator3.approved = False
collaborator3.save()


# Documents
doc = DocumentCase()
doc.creatoriD = str(collaborator1.id)
doc.title= "Document 1"
doc.location = ["San Juan, PR", "Fajardo, PR"]
doc.description = "Lorem ipsum dolor sit amet."
doc.incidentDate = datetime.today().strftime('%Y-%m-%d')
doc.creationDate = datetime.today().strftime('%Y-%m-%d')
doc.tagsDoc = ["sustento"]
doc.infrasDocList =  ["Carreteras"]
doc.damageDocList = ["Alcantarillados"]
doc.author = [sample_author, sample_author]
doc.actor = [sample_actor, sample_actor]
doc.section = [sample_section, sample_section]
doc.timeline = [sample_timeline_pair, sample_timeline_pair]
doc.published = True
doc.save()

doc = DocumentCase()
doc.creatoriD = str(collaborator1.id)
doc.title= "Document 2"
doc.location = ["San Juan, PR", "Fajardo, PR"]
doc.description = "Lorem ipsum dolor sit amet."
doc.incidentDate = datetime.today().strftime('%Y-%m-%d')
doc.creationDate = datetime.today().strftime('%Y-%m-%d')
doc.tagsDoc = ["sustento"]
doc.infrasDocList =  ["Carreteras"]
doc.damageDocList = ["Alcantarillados"]
doc.author = [sample_author, sample_author]
doc.actor = [sample_actor, sample_actor]
doc.section = [sample_section, sample_section]
doc.timeline = [sample_timeline_pair, sample_timeline_pair]
doc.published = True
doc.save()

doc = DocumentCase()
doc.creatoriD = str(collaborator2.id)
doc.title= "COVID-19: Puerto Rico en alerta."
doc.location = ["San Juan, PR", "Fajardo, PR"]
doc.description = "Lorem ipsum dolor sit amet."
doc.incidentDate = datetime.today().strftime('%Y-%m-%d')
doc.creationDate = datetime.today().strftime('%Y-%m-%d')
doc.tagsDoc = ["sustento"]
doc.infrasDocList =  ["Carreteras"]
doc.damageDocList = ["Alcantarillados"]
doc.author = [sample_author, sample_author]
doc.actor = [sample_actor, sample_actor]
doc.section = [sample_section, sample_section]
doc.timeline = [sample_timeline_pair, sample_timeline_pair]
doc.published = False
doc.save()







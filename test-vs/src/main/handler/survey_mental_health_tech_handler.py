
# cluster_out
# This function will help me cluster things in survey-mental-health-tech csv file. I hope I get something within the data.


from re import X
from ssl import ALERT_DESCRIPTION_BAD_RECORD_MAC
from pandas import Interval

"""
data_cleansing

This function dedicated for doing data cleansing. 
"""
def data_cleansing():
    
    # Since its running from main, the folder will be treated as its coming from main.py
    from repository.survey_mental_health_tech_repository import get_raw_data_frame
    
    dataset = get_raw_data_frame()
    
    print("Before cleansing, the total data is : "+ str(len(dataset)))

    # Cleaning invalid ages
    # Take index of which invalid data. 
    invalid_age_indexes = dataset[
        (dataset['Age'] < 0) | (126 < dataset['Age']) # Age Cleansing. Human mostly lifespan at 0 to 126
    ].index
    
    # Cleaning invalid genders. In my country we only aknowledge 2 genders.
    # Female and Male. Female will be marked as 'f' and Male will be 'm'
    invalid_gender_indexes = []
    for idx, e in enumerate(dataset['Gender']):
        gender = e.lower();
        
        if(gender == "m" or gender == "f"):
            continue
        elif(gender == "female"):
            gender = "f"
        elif(gender == "male"):
            gender = "m"
        else:
            # Remove any invalid data.
            invalid_gender_indexes.append(idx)
    
    # Drop data with invalid indexes phase.
    final_invalid_data_index = []
    
    for e in [invalid_age_indexes, invalid_gender_indexes]:
        for f in e:
            
            # Check the index. If it throw exception, append the number. 
            try:
                final_invalid_data_index.index(f)
                continue
            except:
                final_invalid_data_index.append(f)
                
    # Cleanse the data
    dataset = dataset.drop(final_invalid_data_index)

    # Data Encoding Phase
    # Encode Gender

    import pandas
    
    encoded_gender = pandas.get_dummies(dataset['Gender'], prefix = 'gender')
    encoded_self_employed = pandas.get_dummies(dataset['self_employed'], prefix = 'self_employed')
    encoded_family_history = pandas.get_dummies(dataset['family_history'], prefix = 'family_history')
    encoded_treatment = pandas.get_dummies(dataset['treatment'], prefix = 'treatment')
    encoded_work_interfere = pandas.get_dummies(dataset['work_interfere'], prefix = 'work_interfere')
    encoded_remote_work = pandas.get_dummies(dataset['remote_work'], prefix = 'remote_work')
    encoded_tech_company = pandas.get_dummies(dataset['tech_company'], prefix = 'tech_company')
    encoded_benefits = pandas.get_dummies(dataset['benefits'], prefix = 'benefits')
    encoded_care_options = pandas.get_dummies(dataset['care_options'], prefix = 'care_options')
    encoded_wellness_program = pandas.get_dummies(dataset['wellness_program'], prefix = 'wellness_program')
    encoded_seek_help = pandas.get_dummies(dataset['seek_help'], prefix = 'seek_help')
    encoded_anonymity = pandas.get_dummies(dataset['anonymity'], prefix = 'anonymity')
    encoded_leave = pandas.get_dummies(dataset['leave'], prefix = 'leave')
    
    dataset = pandas.concat([dataset, encoded_gender], axis = 1)
    dataset = pandas.concat([dataset, encoded_self_employed], axis = 1)
    dataset = pandas.concat([dataset, encoded_family_history], axis = 1)
    dataset = pandas.concat([dataset, encoded_treatment], axis = 1)
    dataset = pandas.concat([dataset, encoded_work_interfere], axis = 1)
    dataset = pandas.concat([dataset, encoded_remote_work], axis = 1)
    dataset = pandas.concat([dataset, encoded_tech_company], axis = 1)
    dataset = pandas.concat([dataset, encoded_benefits], axis = 1)
    dataset = pandas.concat([dataset, encoded_care_options], axis = 1)
    dataset = pandas.concat([dataset, encoded_wellness_program], axis = 1)
    dataset = pandas.concat([dataset, encoded_seek_help], axis = 1)
    dataset = pandas.concat([dataset, encoded_anonymity], axis = 1)
    dataset = pandas.concat([dataset, encoded_leave], axis = 1)

    # Remove the original columns & unused columns

    for e in [
        'Timestamp', 'Gender', 'Country', 'state', 
        'self_employed', 'family_history', 'treatment', 'work_interfere', 
        'no_employees', 'remote_work', 'tech_company', 'benefits', 
        'care_options', 'wellness_program', 'seek_help', 'anonymity', 
        'leave', 'mental_health_consequence', 'phys_health_consequence', 
        'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview',
        'mental_vs_physical', 'obs_consequence', 'comments'
    ]:
        dataset = dataset.drop(e, axis = 1)
    
    print("After cleansing, the total data is : "+ str(len(dataset)))
    
    return dataset
    
def cluster_out(clean_dataset = []):
    from model.KMeansFactory import KMeansFactory
    import matplotlib.pyplot as plotter
    import numpy
    
    model_id = "TestFactory#1"

    # Fit model
    factory = KMeansFactory()
    factory.createModel(model_id = model_id, clusters = 5)
    factory.fitModel(model_id = model_id, dataset = clean_dataset)

    print ("Model fitted successfully")
    
    # The X stands for age.
    x = clean_dataset['Age']
    
    print("Clustered Total: "+ str(len(factory.getModel(model_id).labels_)))
    print("Data total: "+ str(len(clean_dataset)))
          
    plotter.figure(figsize = (15, 10))
    plotter.scatter(clean_dataset['Age'], factory.getModel(model_id).labels_)
    plotter.title("Survey Mental Health in Tech by its Age")
    plotter.xlabel("The Age")
    plotter.ylabel("Result")
    plotter.show()

def handle_data_clustering():
    cluster_out(data_cleansing())
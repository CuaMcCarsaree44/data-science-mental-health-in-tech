
# cluster_out
# This function will help me cluster things in survey-mental-health-tech csv file. I hope I get something within the data.


def cluster_out():
    
    # Since its running from main, the folder will be treated as its coming from main.py
    from repository.survey_mental_health_tech_repository import get_raw_data_frame
    
    from model.KMeansFactory import KMeansFactory
    import matplotlib.pyplot as plotter

    possible_features = [
        'Age', 'Gender', 'Country', 'state', 
        'self_employed', 'family_history', 'treatment', 'work_interfere',
        'no_employees', 'remote_work', 'tech_company', 'benefits', 
        'care_options', 'wellness_program', 'seek_help', 'anonymity', 
        'leave'
    ]

    dataset = get_raw_data_frame()

    # Take index of which invalid data. 
    invalid_age_indexes = dataset[
        (0 < dataset['Age']) & (126 < dataset['Age']) # Age Cleansing. Human mostly lifespan at 0 to 126
    ].index
    
    for e in dataset:
        ("m" not in dataset['Gender'].lower() or "f" not in dataset['Gender'].lower()) # Gender cleansing. In my country, we only know 2 genders. 
        

    # Cleanse the data
    dataset.drop(invalid_age_indexes)
    
    for e in dataset['Age']:
        print(e)

    # Fit model
    # factory = KMeansFactory()
    # factory.createModel(modelId = 'TestFactory#1')
    # factory.fitModel(modelId = 'TestFactory#1', dataset = get_sorted_data_by_age()[possible_features])
    
    # plotter.scatter(x, y, c=factory.getModel(modelId = 'TestFactory#1').labels_)
    # plotter.show()


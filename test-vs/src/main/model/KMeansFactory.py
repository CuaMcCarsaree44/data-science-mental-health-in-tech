from sklearn.cluster import KMeans

"""
KMeansFactory

This class is a factory class that mainly used for storing any current session used Machine Learning
models, specificly for sklearn.cluster.KMeans 
"""
class KMeansFactory:
    
    """
    @private
    __models
    This attribute made to store your KMeans models
    """
    __models = [];
    
    """
    @public
    getModel
    This function is used to get and return a model.

    @return sklearn.cluster.KMeans
    """
    def getModel(modelId):
        return self.__models[modelId];

    """
    @public
    fitModel
    This function used to fit a model by its model id. 
    
    @param str modelId
        Tell this function which model you want to fit
    @param [] dataset 
        The training dataset.    
    
    @return void
    """
    def fitModel(modelId, dataset):
        self.__models[modelId].fit(dataset)

    """
    @public
    createModel
    This function will create a model, and then store it to __models
    
    @param str modelId 
        Act as model identifier.
    @param int clusters
        Tell how much clusters you wanna make within KMeans. Default 5
    
    @return void
    """
    def createModel(modelId, clusters = 5):
        self.__models[modelId] = KMeans(n_clusters = clusters)
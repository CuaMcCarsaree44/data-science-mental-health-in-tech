from sklearn.cluster import KMeans
import matplotlib.pyplot as plotter

def clustering(all_data = True, cluster = 5):
    kmeans_model = KMeans(n_clusters=cluster)
    
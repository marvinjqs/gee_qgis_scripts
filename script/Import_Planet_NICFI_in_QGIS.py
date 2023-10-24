###########################################################
# Title: Visualization of PlanetNICFI imagery of Metropolitan Lima in QGIS
# Platform: Planet NICFI; image courtesy of Planet Team (2017)
# Author : Marvin J. Quispe Sedano
# Contact : marvinjqs@gmail.com / https://github.com/marvinjqs
###########################################################

# Import the libraries to use
import ee
from ee_plugin import Map

# Import PlanetNICFI images
collection_nicfi = ee.ImageCollection('projects/planet-nicfi/assets/basemaps/americas')

# Import our Area of Interest (AOI)
aoi = ee.FeatureCollection('users/marvinjqs-gis/LIMA_METROPOLITANA_BUF1KM')

# Filter the images of interest
filter_collection = (collection_nicfi.map(lambda image: image.clip(aoi))
    .filterDate('2023','2024')
    .map(lambda image: image.multiply(0.0001))) # Apply scaling factor

# Export all the images in the collection
collection_size = filter_collection.size().getInfo()
list_of_images = filter_collection.toList(collection_size)

vis_nicfi = {'bands':['R','G','B'],
             'min': [0.0451, 0.0568, 0.0359],
             'max': [0.2565, 0.2118, 0.1563],
             'gamma':1}

# Add images to the map
for i in range(collection_size):
    image = ee.Image(list_of_images.get(i))
    description = image.id().getInfo()
    
    Map.addLayer(image, 
        vis_nicfi,
        description,
        shown = False)






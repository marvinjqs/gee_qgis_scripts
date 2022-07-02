###########################################################
# TÍTULO : DESCARGA DE IMAGENES SATELITALES DE LA PLATAFORMA LANDSAT 5-7-8 - SURFACE REFLECTANCE - QGIS + PYTHON
# PLATAFORMA : Landsat- 5,7,8 ;image courtesy of the U.S. Geological Survey
# AUTOR : Marvin J. Quispe Sedano
# CONTACTO : marvinjqs@gmail.com
###########################################################

# Cargamos las librerias

import ee
from ee_plugin import Map

# Seleccionar el area de interes

geometry = ee.Geometry.Polygon(
        [[-81.74357088588678, 0.07285285164088136],
          [-81.74357088588678, -18.99324561294961],
          [-67.59318026088678, -18.99324561294961],
          [-67.59318026088678, 0.07285285164088136]])
          
Map.centerObject(geometry)

# Seleccionar la coleccion de imagenes a usar (L8 y l5- Surface Reflectance)

collection_l8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
collection_l7 = ee.ImageCollection('LANDSAT/LE07/C02/T1_L2')
collection_l5 = ee.ImageCollection('LANDSAT/LT05/C02/T1_L2')

# Ordenamos las imagenes de mayor a menor cobertura de nubes
# El mosaico da prioridad a las últimas imagenes para su creación
# Para los años 2012 y 2002 se usara la plataforma L7

l8_image2015 = ee.ImageCollection(collection_l8
    .filterDate('2015-07-01', '2015-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))

l8_image2014 = ee.ImageCollection(collection_l8
    .filterDate('2014-07-01', '2014-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))

l8_image2013 = ee.ImageCollection(collection_l8
    .filterDate('2013-07-01', '2013-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))

l7_image2012 = ee.ImageCollection(collection_l7
    .filterDate('2012-07-01', '2012-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))

l5_image2011 = ee.ImageCollection(collection_l5
    .filterDate('2011-07-01', '2011-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))

l5_image2010 = ee.ImageCollection(collection_l5
    .filterDate('2010-07-01', '2010-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))
 
l5_image2009 = ee.ImageCollection(collection_l5
    .filterDate('2009-07-01', '2009-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))

l5_image2008 = ee.ImageCollection(collection_l5
    .filterDate('2008-07-01', '2008-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))
    
l5_image2007 = ee.ImageCollection(collection_l5
    .filterDate('2007-07-01', '2007-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))

l5_image2006 = ee.ImageCollection(collection_l5
    .filterDate('2006-07-01', '2006-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))

l5_image2005 = ee.ImageCollection(collection_l5
    .filterDate('2005-07-01', '2005-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))

l5_image2004 = ee.ImageCollection(collection_l5
    .filterDate('2004-07-01', '2004-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))

l5_image2003 = ee.ImageCollection(collection_l5
    .filterDate('2003-07-01', '2003-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))

l7_image2002 = ee.ImageCollection(collection_l7
    .filterDate('2002-07-01', '2002-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))
    
l5_image2001 = ee.ImageCollection(collection_l5
    .filterDate('2001-07-01', '2001-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))
    
l5_image2000 = ee.ImageCollection(collection_l5
    .filterDate('2000-07-01', '2000-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))
    
l5_image1999 = ee.ImageCollection(collection_l5
    .filterDate('1999-07-01', '1999-09-30')
    .filterBounds(geometry)
    .sort('CLOUD_COVER', False))
    
# Creamos el mosaico considerando dar prioridad a imagenes con menos nubes

l8_image2015_mosaic = ee.ImageCollection(l8_image2015.mosaic())
l8_image2014_mosaic = ee.ImageCollection(l8_image2014.mosaic())
l8_image2013_mosaic = ee.ImageCollection(l8_image2013.mosaic())

l7_image2012_mosaic = ee.ImageCollection(l7_image2012.mosaic())
l5_image2011_mosaic = ee.ImageCollection(l5_image2011.mosaic())
l5_image2010_mosaic = ee.ImageCollection(l5_image2010.mosaic())
l5_image2009_mosaic = ee.ImageCollection(l5_image2009.mosaic())
l5_image2008_mosaic = ee.ImageCollection(l5_image2008.mosaic())
l5_image2007_mosaic = ee.ImageCollection(l5_image2007.mosaic())
l5_image2006_mosaic = ee.ImageCollection(l5_image2006.mosaic())
l5_image2005_mosaic = ee.ImageCollection(l5_image2005.mosaic())
l5_image2004_mosaic = ee.ImageCollection(l5_image2004.mosaic())
l5_image2003_mosaic = ee.ImageCollection(l5_image2003.mosaic())

l7_image2002_mosaic = ee.ImageCollection(l7_image2002.mosaic())
l5_image2001_mosaic = ee.ImageCollection(l5_image2001.mosaic())
l5_image2000_mosaic = ee.ImageCollection(l5_image2000.mosaic())
l5_image1999_mosaic = ee.ImageCollection(l5_image1999.mosaic())


print(l8_image2015_mosaic.getInfo())

# Aplicar el factor de escala de L8 para Reflectancia de superficie

l8_image2015_rgb = l8_image2015_mosaic.select(['SR_B4', 'SR_B3', 'SR_B2']).toBands().multiply(0.0000275).add(-0.2)
l8_image2014_rgb = l8_image2014_mosaic.select(['SR_B4', 'SR_B3', 'SR_B2']).toBands().multiply(0.0000275).add(-0.2)
l8_image2013_rgb = l8_image2013_mosaic.select(['SR_B4', 'SR_B3', 'SR_B2']).toBands().multiply(0.0000275).add(-0.2)

l7_image2012_rgb = l7_image2012_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image2011_rgb = l5_image2011_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image2010_rgb = l5_image2010_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image2009_rgb = l5_image2009_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image2008_rgb = l5_image2008_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image2007_rgb = l5_image2007_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image2006_rgb = l5_image2006_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image2005_rgb = l5_image2005_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image2004_rgb = l5_image2004_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image2003_rgb = l5_image2003_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)

l7_image2002_rgb = l7_image2002_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image2001_rgb = l5_image2001_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image2000_rgb = l5_image2000_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)
l5_image1999_rgb = l5_image1999_mosaic.select(['SR_B3', 'SR_B2', 'SR_B1']).toBands().multiply(0.0000275).add(-0.2)

#

l8_image2015_rgb = l8_image2015_rgb.rename(['SR_B4', 'SR_B3', 'SR_B2'])
l8_image2014_rgb = l8_image2014_rgb.rename(['SR_B4', 'SR_B3', 'SR_B2'])
l8_image2013_rgb = l8_image2013_rgb.rename(['SR_B4', 'SR_B3', 'SR_B2'])

l7_image2012_rgb = l7_image2012_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image2011_rgb = l5_image2011_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image2010_rgb = l5_image2010_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image2009_rgb = l5_image2009_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image2008_rgb = l5_image2008_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image2007_rgb = l5_image2007_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image2006_rgb = l5_image2006_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image2005_rgb = l5_image2005_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image2004_rgb = l5_image2004_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image2003_rgb = l5_image2003_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])

l7_image2002_rgb = l7_image2002_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image2001_rgb = l5_image2001_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image2000_rgb = l5_image2000_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])
l5_image1999_rgb = l5_image1999_rgb.rename(['SR_B3', 'SR_B2', 'SR_B1'])


# print(l8_image2015_rgb.getInfo())

# Presentar la paleta de colores de color verdadero 

l8_visualization_rgb = {
  'bands': ['SR_B4', 'SR_B3', 'SR_B2'],
  'min': 0.0,
  'max': 0.3,
}

l7_visualization_rgb = {
  'bands': ['SR_B3', 'SR_B2', 'SR_B1'],
  'min': 0.0,
  'max': 0.3,
}

l5_visualization_rgb = {
  'bands': ['SR_B3', 'SR_B2', 'SR_B1'],
  'min': 0.0,
  'max': 0.3,
}

# Añadir los mosaicos al proyecto de QGIS

Map.addLayer(l8_image2015_rgb, l8_visualization_rgb, 'RGB-LANDSAT8-2015')
Map.addLayer(l8_image2014_rgb, l8_visualization_rgb, 'RGB-LANDSAT8-2014')
Map.addLayer(l8_image2013_rgb, l8_visualization_rgb, 'RGB-LANDSAT8-2013')

Map.addLayer(l7_image2012_rgb, l7_visualization_rgb, 'RGB-LANDSAT7-2012')
Map.addLayer(l5_image2011_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-2011')
Map.addLayer(l5_image2010_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-2010')
Map.addLayer(l5_image2009_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-2009')
Map.addLayer(l5_image2008_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-2008')
Map.addLayer(l5_image2007_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-2007')
Map.addLayer(l5_image2006_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-2006')
Map.addLayer(l5_image2005_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-2005')
Map.addLayer(l5_image2004_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-2004')
Map.addLayer(l5_image2003_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-2003')

Map.addLayer(l7_image2002_rgb, l7_visualization_rgb, 'RGB-LANDSAT7-2002')
Map.addLayer(l5_image2001_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-2001')
Map.addLayer(l5_image2000_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-2000')
Map.addLayer(l5_image1999_rgb, l5_visualization_rgb, 'RGB-LANDSAT5-1999')






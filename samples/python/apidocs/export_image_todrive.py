# Copyright 2023 The Google Earth Engine Community Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START earthengine__apidocs__export_image_todrive]
# A Landsat 8 surface reflectance image.
image = ee.Image(
    'LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508'
).select(['SR_B.'])  # reflectance bands

# A region of interest.
region = ee.Geometry.BBox(-122.24, 37.13, -122.11, 37.20)

# Set the export "scale" and "crs" parameters.
task = ee.batch.Export.image.toDrive(
    image=image,
    description='image_export',
    folder='ee_demos',
    region=region,
    scale=30,
    crs='EPSG:5070'
)
task.start()

# Use the "crsTransform" export parameter instead of "scale" for more control
# over the output grid. Here, "crsTransform" is set to align the output grid
# with the grid of another dataset. To view an image's CRS transform:
# print(image.projection().getInfo())
task = ee.batch.Export.image.toDrive(
    image=image,
    description='image_export_crstransform',
    folder='ee_demos',
    region=region,
    crsTransform=[30, 0, -2493045, 0, -30, 3310005],
    crs='EPSG:5070'
)
task.start()

# If the export has more than 1e8 pixels, set "maxPixels" higher.
task = ee.batch.Export.image.toDrive(
    image=image,
    description='image_export_maxpixels',
    folder='ee_demos',
    region=region,
    scale=30,
    crs='EPSG:5070',
    maxPixels=1e13
)
task.start()

# Export a Cloud Optimized GeoTIFF (COG) by setting the "cloudOptimized"
# parameter to true.
task = ee.batch.Export.image.toDrive(
    image=image,
    description='image_export_cog',
    folder='ee_demos',
    region=region,
    scale=30,
    crs='EPSG:5070',
    formatOptions={
        'cloudOptimized': True
    }
)
task.start()
# [END earthengine__apidocs__export_image_todrive]

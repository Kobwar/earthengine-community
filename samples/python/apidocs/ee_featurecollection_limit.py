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

# [START earthengine__apidocs__ee_featurecollection_limit]
# FeatureCollection of global power plants.
fc = ee.FeatureCollection('WRI/GPPD/power_plants')

print('First 5 features (power plants):', fc.limit(5).getInfo())

print('Smallest 5 power plants by capacity in ascending order:',
      fc.limit(**{'maximum': 5, 'opt_property': 'capacitymw'}).getInfo())

print('Largest 5 power plants by capacity in descending order:',
      fc.limit(**{'maximum': 5, 'opt_property': 'capacitymw',
                  'opt_ascending': False}).getInfo())
# [END earthengine__apidocs__ee_featurecollection_limit]

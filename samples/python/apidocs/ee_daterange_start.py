# Copyright 2021 The Google Earth Engine Community Authors
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

# [START earthengine__apidocs__ee_daterange_start]
# An ee.DateRange.
date_range = ee.DateRange('2017-06-24', '2017-07-24')

# Return the start of the ee.DateRange as an ee.Date.
display('The start of this ee.DateRange is', date_range.start())
# [END earthengine__apidocs__ee_daterange_start]

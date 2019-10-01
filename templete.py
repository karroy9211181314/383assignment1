# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Creates a Compute Engine Instance."""


def GenerateConfig(context):
  
  resources = []
# [START use_basic_template]
  resources.append({
      'name': 'vm-template',
      'type': 'compute.v1.instance',
      'properties': {
          'zone': 'us-central1-a',
          'machineType': 'zones/us-central1-a/machineTypes/n1-standard-1',
          'disks': [{
              'deviceName': 'boot',
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'sourceImage':
                      'projects/ubuntu-os-cloud/global/images/family/ubuntu-1804-lts'
              }
          }],
          'networkInterfaces': [{
              'network': 'global/networks/default'
          }]
      }
  })
# [END use_basic_template]
  return {'resources': resources}
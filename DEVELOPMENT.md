<!--Copyright 2022 Tellius, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.-->
# Developing Tellius Data Manager

# About

# Installing Dependencies
tdm uses poetry as its python package manager. To install the dependencies you must first install poetry. This can be 
installed with brew or directly in python. This works well with IDEs such as pycharm when you set your working 
interpreter.

Once poetry is added simply execute the command
```bash
poetry install
```

If a new product dependency is needed, then 
```bash
poetry add PACKAGE_NAME
```

If the dependency is strictly for development needs - but not used when deploying the product, then install it using
```bash
poetry add --dev PACKAGE_NAME
```

# Creating New Pipes


# Running Tests

TBD

# Formatting Code
The code uses opinionated formatting. Before committing your code the central repository, you must format the code using 
black

```bash
black .
```

This will run through the entire code base and reformat the code to a python standard format.

# Updating Documentation

Documentation uses pdoc3. To update the documentation, which should be done after merging with main (trunk) branch and 
pushing the code to the central repo by:

```bash
pdoc --html tellius_data_manager --force
```
**1. Dataset name**
-> NormanPd Data

**2. Dataset version number or date**
-> Version 1, data - 08-04-2024

**3. Dataset owner/manager contact information, including name and email**
-> Yasir Khan, y.khan@ufl.edu

**4. Who can access this dataset**
-> Anyone for educational purpose

**5. How can the dataset be accessed?**
-> By going to the github and run the code. The steps to run is provided in readme file.

**6. What are the contents of this dataset?**
-> This dataset has the incident report as informed by the Norman Pd. The dataset contains 13 columns and contain information such as date / time, incident number, incident location, nature of incident, incident ori, day of the week, time of the day, weather, location rank,  nature rank, side of town and emsstat. This dataset is specifically for a particular month and day.

**7. What are the intended purposes for this dataset?**
-> This dataset must be use for educational purpose and is served as accountability by providing public access to police incident data. This dataset can be used to develop machine learning model for data-driven policymaking and resource allocation for public safety.

**8. What are some tasks/purposes that this dataset is not appropriate for?**
-> Researchers should avoid making conclusion which makes broad generalizations about crime rates or public safety across larger regions or populations, as this can lead to bias. This dataset is not created to identify and target specific individuals and hence researchers should avoid doing so.

**9. How was the data collected?**
-> Part of this data have taken from Norman, Okhlama police department website and then some data augmentation have been performed on the dataset.

**10. Describe considerations taken for responsible and ethical data collection**
-> This dataset have not been made by crowdsourcing instead I, the primary owner of the dataset, have created the whole dataset and utmost care have been taken to ensure ethical data collection.

**11. Describe procedures and include language used for getting explicit consent for data collection and use, and/or revoking consent (e.g., for future uses or for certain uses). If explicit consent was not secured, describe procedures and include language used for notifying people about data collection and use.**
-> This data does not disclose any personal identifiable information of any particular individual and have been created with information that have already been available publically.

**12. How representative is this dataset? What population(s), contexts (e.g., scripted vs.conversational speech), conditions (e.g., lighting for images) is it representative of?**
-> The representativeness of the Norman PD dataset largely depends on the demographics and characteristics of the Norman, Oklahoma population. It represent incidents reported to the police department within that jurisdiction. However, limitations could arise from underreporting of certain types of incidents, potential biases in law enforcement practices, or exclusion of incidents not documented by the police.

**13. What demographic groups (e.g., gender, race, age, etc.) are identified in the dataset, if any? How were these demographic groups identified**
-> This dataset does not identify any demographics or intersectional groups. 

**14. Is there any missing information in the dataset? If yes, please explain what information is missing and why**
-> Yes there has missing information in the database like the nature of the incident. The reason may be the failure of police to document the information properly.

**15. What errors, sources of noise, or redundancies are important for dataset users to be aware of?**
-> The nature column in the database is repeated. The latitude and longitude of some of the location may not be extracted properly and hence side of the town of these location can not be calculated.

**16. What data might be out of date or no longer available**
-> For very old data (more than a year), weather extraction may not work properly as the api provider does not keep weather of long time ago. 

**17. How was the data validated/verified?**
-> The primary data has been verfied by the police department of norman, okhlama. Then the new augmented data has been verified manually be me.

**18. What are potential validity issues a user of this dataset needs to be aware of**.
-> There might be some error while documenting the incidents in the database by the norman law enforcement. 

**19. What are other potential data quality issues a user of this dataset needs to be aware of?**
-> This dataset contain reduntant column. 

**20. What pre-processing, cleaning, and/or labeling was done on this dataset?**
-> Data augmentation have been done on the original dataset of norman police department.

**21. Provide a link to the code used to preprocess/clean/label the data, if available.**
-> https://github.com/yasir-17/cis6930sp24-assignment2

**22. If there are any recommended data splits (e.g., training, development/validation, testing), please explain.**
-> There is no recommended splitting but it does depend on the user use case.

**23. What are potential data confidentiality issues a user of this dataset needs to be aware of? How might a dataset user protect data confidentiality?**
-> This data exposes address of the incident and hence it can cuase possible confidentaility issues. To protect data confidentiality, users should mask information such as address.

**24. Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?**
-> Its not possible to identify indiviudal directly but with the help of location, its possible to identify group of people.

**25. If an analysis of the potential impact of the dataset and its uses on data subjects (e.g., a data protection impact analysis) exists, please provide a brief description of the analysis and its outcomes here and include a link to any supporting documentation.**
-> No such analysis exists.

**26. If the dataset has undergone any other privacy reviews or other relevant reviews (legal, security) please include the determinations of these reviews, including any limits on dataset usage or distribution.**
-> No such review exists.

**27. How can dataset users receive information if this dataset is updated (e.g., corrections, additions, removals)?**
-> The user should frequently check this github page for any update in the dataset.

**28. For static datasets: What will happen to older versions of the dataset? Will they continue to be maintained?**
-> This dataset will not change over time unless any unforeseeable circumstances. 

**29. For streaming datasets: If this dataset pulls telemetry data from other sources, please specify**
-> This dataset takes elementary information for norman police website and hence this dataset will be active as long as the website remains active. The website access remains with the norman police department. All other information like the access control or how long will it be active remains with the norman police department. 

**30. If this dataset links to data from other sources (e.g., this dataset includes links to content such as social media posts or, news articles, but not the actual content), please specify**
-> Does not apply.

**31. Describe any applicable intellectual property (IP) licenses, copyright, fees, terms of use, export controls, or other regulatory restrictions that apply to this dataset or individual data points.**
-> Any license and copyright remains with the norman police department and with the primary owner of the dataset. See github for more information about the license. 


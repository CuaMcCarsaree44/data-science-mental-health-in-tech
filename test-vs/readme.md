# My First Data Science Mini Project

This is me learning machine learning to find effectives features by doing data cleansing and making an actual module to be production ready service. 

The data within based on public data of [*Mental Health in Tech Survey*](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey).

## About the dataset

The dataset contains 27 features:

| Feature | Description | Data Type | Data Variances |
|---|---|---|---|
| `Timestamp` | The timestamp of the data created | `object` | [timestamp] |
| `Age` | The age of respondent (int) | `int64` | [ 37  44  32  31  33  35 39  42  23  29  36  27 46  41  34  30  40  38 50  24  18  28  26  22 19  25  45  21 -29  43 56  60  54 329  55 99999999999 48  20  57  58  47  62 51  65  49       -1726   5  53 61   8  11  -1  72] |
| `Gender` | The gender of respondent (string) | `object` | ['Female' 'M' 'Male' 'male' 'female' 'm' 'Male-ish' 'maile' 'Trans-female' 'Cis Female' 'F' 'something kinda male?' 'Cis Male' 'Woman' 'f' 'Mal' 'Male (CIS)' 'queer/she/they' 'non-binary' 'Femake' 'woman' 'Make' 'Nah' 'All' 'Enby' 'fluid' 'Genderqueer' 'Female ' 'Androgyne' 'Agender' 'cis-female/femme' 'Guy (-ish) ^_^' 'male leaning androgynous' 'Male ' 'Man' 'Trans woman' 'msle' 'Neuter' 'Female (trans)' 'queer' 'Female (cis)' 'Mail' 'cis male' 'A little about you' 'Malr' 'p' 'femail' 'Cis Man' 'ostensibly male, unsure what that really means'] |
| `Country` | The Country the respondent currently lives in (string) | `object` | ['United States' 'Canada' 'United Kingdom' 'Bulgaria' 'France' 'Portugal' 'Netherlands' 'Switzerland' 'Poland' 'Australia' 'Germany' 'Russia' 'Mexico' 'Brazil' 'Slovenia' 'Costa Rica' 'Austria' 'Ireland' 'India' 'South Africa' 'Italy' 'Sweden' 'Colombia' 'Latvia' 'Romania' 'Belgium' 'New Zealand' 'Zimbabwe' 'Spain' 'Finland' 'Uruguay' 'Israel' 'Bosnia and Herzegovina' 'Hungary' 'Singapore' 'Japan' 'Nigeria' 'Croatia' 'Norway' 'Thailand' 'Denmark' 'Bahamas, The' 'Greece' 'Moldova' 'Georgia' 'China' 'Czech Republic' 'Philippines'] |
| `state` | If the respondent live in US, the state respresent as the state where the respondent lives in (char(2)) | `object` | ['IL' 'IN' nan 'TX' 'TN' 'MI' 'OH' 'CA' 'CT' 'MD' 'NY' 'NC' 'MA' 'IA' 'PA' 'WA' 'WI' 'UT' 'NM' 'OR' 'FL' 'MN' 'MO' 'AZ' 'CO' 'GA' 'DC' 'NE' 'WV' 'OK' 'KS' 'VA' 'NH' 'KY' 'AL' 'NV' 'NJ' 'SC' 'VT' 'SD' 'ID' 'MS' 'RI' 'WY' 'LA' 'ME'] |
| `self_employed` | Determine whatever the respondent is self-employed or not (NA / Yes / No) | `object` | [nan 'Yes' 'No'] |
| `family_history` | Determine whatever the respondent's family had some history regarding mental illness (boolean) | `object` | ['No' 'Yes'] |
| `treatment` | Determine whatever the respondent sought treatment for mental health condition (boolean) |  `object` | ['Yes' 'No'] |
| `work_interfere` | Determine whaterver mental health condition interferes the work (Often / Rarely / Never / Sometimes) | `object` | ['Often' 'Rarely' 'Never' 'Sometimes' nan] |
| `no_employees` | Company's size by employees (enum) | `object` | ['6-25' 'More than 1000' '26-100' '100-500' '1-5' '500-1000'] |
| `remote_work` | Determine whatever the respondent work remotely at least 50% of the time (boolean) | `object` | ['No' 'Yes'] |
| `tech_company` | Determine whatever the respondent work for tech company primarily (boolean) | `object` | ['Yes' 'No'] |
| `benefits` | Determine whatever the respondent received mental health benefits (NA / Yes / No / Don't know) | `object` | ['Yes' "Don't know" 'No'] |
| `care_options` | Determine whatever the respondent know the options regarding the mental health care (Yes / No / Not sure) | `object` | ['Not sure' 'No' 'Yes'] |
| `wellness_program` | Determine whatever the respondent ever discussed mental health as part of an employee wellness program (Yes / No / Don't know) | `object` | ['No' "Don't know" 'Yes'] |
| `seek_help` | Determine whatever employer provide resources to learn more about mental health issues and how to seek help | `object` | ['Yes' "Don't know" 'No'] |
| `anonymity` | Determine whatever anonymity protected if respondent choose to take advantage of mental health or substance abuse treatment resources. | `object` | ['Yes' "Don't know" 'No'] |
| `leave` | Determine whatever is it easy for respondent to take medical leave for a mental health condition. | `object` | ['Somewhat easy' "Don't know" 'Somewhat difficult' 'Very difficult'
 'Very easy'] |
| `mental_health_consequence` | Determine whatever discussing a mental health issue with employer would have negative consequences. | `object` | ['No' 'Maybe' 'Yes'] |
| `phys_health_consequence` |  Determine whatever discussing a physical health issue with employer would have negative consequences. | `object` | ['No' 'Maybe' 'Yes'] |
| `coworkers` | Determine whatever respondent willing to discuss mental health issue with coworkers | `object` | ['Some of them' 'No' 'Yes'] |
| `supervisor` | Determine whatever respondent willing to discuss a mental health issue with direct supervisor(s) | `object` | ['Yes' 'No' 'Some of them'] |
| `mental_health_interview` | Determine whatever respondent willing to bring up mental health issue with a potential employer in an interview | `object` | ['No' 'Yes' 'Maybe'] |
| `phys_health_interview` | Determine whatever respondent willing to bring up physical health issue with a potential employer in an interview | `object` | ['No' 'Yes' 'Maybe'] |
| `mental_vs_physical` | Determine whatever respondent take mental health as serious as physical health | `object` | ['Yes' "Don't know" 'No'] |
| `obs_consequence` | Determine whatever respondent have heard or observed the negative consequences for coworkers with mental health conditions in workplace | `object` | ['No' 'Yes'] |
| `comments` | Addition comments | `object` | [string] |

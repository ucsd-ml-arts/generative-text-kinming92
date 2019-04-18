# Project 1 Generative Text

Kin Ming Loh, A14182456, kmloh@ucsd.edu

## Abstract
Hazards alerts contains flood warning, wind advisory and storm hazards. Alert messages gave the residents a short and precise details about those hazards. They are created to serve the purpose of informing and warning the residents. A char generative rnn( a form of LSTM network) is used to generate the alert message. The idea of the char rnn is to the take a sequence of string which then is used to predict the next sequences. 4 inner layers of 1024 rnn_units are used in this architeture. Datasets are collected and formatted in a txt format through a python script. The datasets are then formatted in two different way which are named out.txt and alert_description.txt. However, the result generated from alert_description.txt are shown for the result presentation because it works better with this char rnn model.


## Files
### training data
- alert_description.txt
- out.txt

### training code
- project1.ipynb 

### code that are used to collect data 
- collect_data.py
- get_alert_report.py
- get_alert_description.py

### raw data
- data_list.txt
- *.json

## Results
- Result.txt

## Notes
#### Before Getting Started
- Make sure there is a file named either out.txt or alert_description.txt
- Otherwise
  - run python collect_data.py
  - run python get_alert_report.py or python get_alert_description.py on the terminal

## Reference

Project requirements: [doc](https://docs.google.com/document/d/13ueceIyuUc4ATD7B-SFZK641MycFZ57eZ9n1lQ3Y1CM/edit?usp=sharing)
[National Weather Service Web API](https://www.weather.gov/documentation/services-web-api)

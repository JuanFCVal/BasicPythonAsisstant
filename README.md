# BasicPythonAsisstant
This is a python voice assistant where you can speak and get an answer with voice. We use Speech to text, and Text to Speech.
## First step.
You can fork, clone or download the project.
## Second step.
Create a virtual environment
For Windows Open Shell and write. (You should have python 3x + installed.)
```
pip install virtualenv
python -m venv venv  
cd venv
cd Scripts
ls  #Search for activate
then activate or ./activate #It depends on the answer in the last step.
cd ..
cd .. #Until you get to main directory. /BasicPythonAssistant
```
## Third step.
Install dependencies.
 `pip install -r requirements.txt`
## Four step.
On the main directory /BasicPythonAssistant where main.py open power shell and run:
 `python main.py`
 You should see a "Start speaking" message right now you can start speaking and wait for an answer.
>In case you want to change or update answers you have to edit answers.json file.

### Json Answers File.

The structure of the json file is the following:
{
 "key": {
     "keywords" : [],
     "respuestas" : []
  }
}
Where key is and identifier of a category of answers, "keywords" is maybe the most important part, the words that are in Keywords array are the one that our system are going to search to return an answer for example, in case your keyword has "tiempo" word, and the person say "Cómo pasa el tiempo", System are going to search in this category answers and going to return a random answer in this category. Hope u understand In case u want more information about this project you can send me a message. 


That's all Folks. =D

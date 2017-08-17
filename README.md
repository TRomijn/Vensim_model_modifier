# Vensim_model_modifier
Functionalities to change and add variables and relations in a Vensim model.

## How it works
A vensim model file is a flat text file, which can be altered to change and add variables in a vensim model.
This 'package' contains functions that changes the text file for some basic changes such as adding variables and changing formulas.

## Why do this?
Changing the model via the text file can enable users that want to algorithmically change model structures to do this automatically annd for multiple variables consecutively.

A usecase example: Automation of the Ford's behavioural approach to loop dominance. In combination with the SILS package (to find the Shortest Independent Loop Set) this package can be used to cut loops in a vensim model. A switch can be added to every loop in the SILS and by simulating the model by consecutively turning off loops, the effects of these loops on the model behaviour become apparent. 

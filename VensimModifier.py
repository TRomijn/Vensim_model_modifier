'''
Created on April - August 2017
@author: TRomijn

'''
import HelperFunctions as hf
from HelperFunctions import read_mdl_file, save_list_to_mdl


# TODO: View1, think of solution. Not each model might have a View 1
def AddVariable(VarName, RHS, model, Gaming=False, view="View 1"):
    '''
    VarName: string
    RHS: right-hand side of formula: String
    model: list object (use read_mdl_file)
    Gaming: Boolean
    view: string
    '''
    # Create formula
    mdl_list = model    # legacy workaround
    Formula = [
        "{var}={game}\n".format(var=VarName, game=" GAME (" if Gaming == True else ""),
        RHS + "{}\n".format(")" if Gaming == True else ""),
        "\t~\t\n",
        "\t~\t\t|\n",
        "\n"]

    # Add Formula
    # Find end of variable definition list
    i = mdl_list.index('********************************************************\n')
    # Add Formula before the end
    mdl_list[i:i] = Formula

    # Add to Sketch
    # TODO: try view else: put in last view
    # find view:
    i2 = mdl_list.index('*{}\n'.format(view))

    for x, line in enumerate(mdl_list[i2:]):
        if "---" in line:
            i3 = x + i2
            break

    # Find variable number
    n = mdl_list[i3-1].split(",")[1]
    sketch_line = [10, int(n)+1, VarName, 0, 0, 50, 50, 8, 3, 0, 0, 0, 0, 0, 0]
    # convert to string
    new_sketch_line = ""
    for x in sketch_line:
        new_sketch_line += str(x) + ","
    # delete last comma and add newline
    new_sketch_line = new_sketch_line[:-1] + "\n"
    mdl_list[i3:i3] = [new_sketch_line]
    # ]
    return mdl_list


def duplicate_variable(model, Orig_Var):
    """
    model: List (the opened MDL file)
    orig_var: The to be duplicated variable

    returns the new model as a list (which can be saved)
    """
    # Find formula start and end.
    i_start, i_end = hf.find_var_function(Orig_Var, model)
    # duplicate formula of a variable
    new_mdl_list = hf.duplicate_formula(Orig_Var, i_start, i_end, model)
    # Add sketch information
    new_mdl_list = hf.add_to_vensim_sketch(Orig_Var, new_mdl_list)
    return new_mdl_list


# Find formula of a variable
def replace_vars_in_RHS(mdl_list, VarName, old_var="", new_var=""):
    '''
    replace variables in the Righ-Hand Side (RHS) of a Target Variable
    VarName: target variable of which the RHS (Right-Hand Side) should be changed
    if old_var and new_var are the same, this function will print the RHS of the Target variable
    old_var: old text that should be changed in the formula
    new_var: new text that should replace the old text.
    '''

    try:
        i = mdl_list.index("{}=\n".format(VarName))
    except Exception:
        i = mdl_list.index("{}= GAME (\n".format(VarName))

    formula = []
    for i2, line in enumerate(mdl_list[i:]):
        if "~" not in line:
            formula.append(line)
        else:
            i3 = i2 + i
            break
    print("Old formula:", formula)

    new_formula = []
    for line in formula:
        new_formula.append(line.replace(old_var, new_var))

    print("New formula:", new_formula)

    # return new_formula, i, i3
    mdl_list[i:i3] = new_formula
    return mdl_list

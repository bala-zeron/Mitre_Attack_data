from pyattck import Attck


def load_mitre_attck():

    global result_dict
    attack = Attck()

    # if result_dict:
    if 'result_dict' in globals():
        return result_dict

    result_dict = {}

    for technique in attack.enterprise.techniques:
        result_dict[technique.technique_id] = technique

    return result_dict

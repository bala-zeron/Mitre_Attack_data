from pyattck import Attck

# global attck
# attck = Attck()
# attck.enterprise
# attck.update()

def load_mitre_attck_techniques():

    global result_dict_techniques

    if 'result_dict_techniques' in globals():
        return result_dict_techniques

    if 'attck' not in globals():
        global attck
        attck = Attck()

    result_dict_techniques = {}

    for technique in attck.enterprise.techniques:
        result_dict_techniques[technique.technique_id] = technique
        # result_dict_techniques[technique.id] = technique

    return result_dict_techniques

def load_mitre_attck_tactics():

    global result_dict_tactics

    if 'attck' not in globals():
        global attck
        attck = Attck()

    attck = Attck()

    result_dict_tactics = {}

    for tactic in attck.enterprise.tactics:
        # result_dict_tactics[tactic.id] = tactic
        result_dict_tactics[tactic.tactic_id] = tactic

    return result_dict_tactics

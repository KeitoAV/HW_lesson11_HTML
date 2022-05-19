import json
from pprint import pprint as pp

from config import DATA_PATH


def load_candidates_from_json(path=DATA_PATH):
    """Возвращает список всех кандидатов"""
    with open(path, 'r', encoding='utf8') as file:
        data = json.load(file)
    return data


# pp(load_candidates_from_json())


def get_candidate(candidate_id):
    """Возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json()
    id_candidates = []
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            id_candidates.append(candidate)
            continue
    return id_candidates


# pp(get_candidate(1))

def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    named_candidates = []
    name_lower = candidate_name.lower()
    candidates = load_candidates_from_json()
    for candidate in candidates:
        name = candidate["name"].lower().strip().split(' ')
        if name_lower in name:
            named_candidates.append(candidate)
            continue
    return named_candidates


# pp(get_candidates_by_name('Austin'))


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""

    skilled_candidates = []
    skill_name_lower = skill_name.lower()

    candidates = load_candidates_from_json()
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(', ')
        if skill_name_lower in skills:
            skilled_candidates.append(candidate)
            continue

    return skilled_candidates

#  pp(get_candidates_by_skill('go'))

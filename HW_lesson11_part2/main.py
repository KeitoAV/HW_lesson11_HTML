from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
def page_all_candidate():
    """Выводим на страницу всех кандидатов"""
    candidate = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidate)


@app.route('/candidate/<int:candidate_id>/')
def page_single_candidate(candidate_id):
    """Выводим на страницу кандидата по id"""
    candidate = utils.get_candidate(candidate_id)

    if len(candidate) == 0:
        return 'Такого кандидата нет.'

    return render_template('single.html', candidates=candidate)


@app.route('/search/<candidate_name>/')
def get_candidates_by_name(candidate_name):
    """Выводим на страницу кандидатов, в имени у которых содержится candidate_name"""
    candidate = utils.get_candidates_by_name(candidate_name)
    all = len(candidate)

    if len(candidate) == 0:
        return 'Кандидата с таким именем нет.'

    return render_template('search.html', candidates=candidate, all_=all)


@app.route('/skill/<skill_name>/')
def get_candidates_by_skill(skill_name):
    """Выводим на страницу кандидатов по skills"""
    candidate = utils.get_candidates_by_skill(skill_name)
    skill = skill_name

    if len(candidate) == 0:
        return 'Кандидаты c такими навыками не найдены.'

    return render_template('skill.html', candidates=candidate, skill_=skill)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)  # проверка режим отладки

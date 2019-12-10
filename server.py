from flask import Flask, render_template, redirect, request, url_for
import data_manager as data_manager

app = Flask(__name__)


@app.route('/list')
def route_index():
    return render_template('index.html')


@app.route('/question/<question_id>')
def route_question(question_id):
    return 'google'


@app.route('/add-question', methods=['GET', 'POST'])
def route_add_question():
    if request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        data_manager.add_question(title, message)
        return redirect(url_for("route_question", question_id=len(data_manager.question_list)))
    else:
        return render_template('add_question.html')


@app.route('/question/<question_id>/edit')
def route_edit_question(question_id):
    pass


@app.route('/question/<question_id>/delete')
def route_delete_question(question_id):
    pass


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def route_add_answer(question_id):
    if request.method == 'POST':
        message = request.form['message']
        data_manager.add_answer(question_id, message)
        return redirect(url_for('route_question', question_id=question_id))
    return render_template('add_answer.html', question_id=question_id)


@app.route('/answer/<answer_id>/delete')
def route_delete_answer(answer_id):
    pass


@app.route('/question/<question_id>/vote_up')
def route_question_vote_up(question_id):
    data_manager.vote_question(question_id, 'vote-up')
    print()


@app.route('/question/<question_id>/vote_down')
def route_question_vote_down(question_id):
    pass


@app.route('/answer/<answer_id>/vote_up')
def route_answer_vote_up(answer_id):
    pass


@app.route('/answer/<answer_id>/vote_down')
def route_answer_vote_down(answer_id):
    pass


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0",
        port="7070"
    )

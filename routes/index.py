from flask import render_template, jsonify


def work_in_progress_route():
    return render_template('work_in_progress.html')


def index_route():
    items = [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}, {'id': 3, 'name': 'Item 3'}]
    return render_template('index.html', items=items)

def about_the_app_route():
    return render_template(
        'about_the_app.html'
    )


def get_info(item_id):
    info = f"Information for Item {item_id}"
    return jsonify({'info': info})

from flask import Flask, jsonify, request



todos = [{"label":"My first task", "done": False}]


app = Flask(__name__)



@app.route('/todos', methods=['GET'])
def hello_world():
    json_todos = jsonify(todos)
    
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return todos


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position=None):

    todos.remove(todos[0])

    print("this is the position to delete", position)

    return jsonify(todos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user data
users = []

@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    user['id'] = len(users) + 1
    users.append(user)
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(id):
    user = next((u for u in users if u['id'] == id), None)
    if user is None:
        return jsonify({'message': 'User not found'}), 404

    if request.method == 'GET':
        return jsonify(user)

    if request.method == 'PUT':
        user.update(request.json)
        return jsonify(user)

    if request.method == 'DELETE':
        users.remove(user)
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)

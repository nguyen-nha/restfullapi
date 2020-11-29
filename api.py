from models import *


# route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'Users': User.get_all_users()})


# route to get user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return_value = User.get_user(id)
    return jsonify(return_value)


# route to add new user
@app.route('/sign_up', methods=['POST'])
def sign_up():
    '''Function to add new user to our database'''
    request_data = request.get_json()  # getting data from client
    User.sign_up(request_data["name"], request_data["email"], request_data["password"])
    response = Response("sign_up success ", status=200, mimetype='application/json')
    return response


@app.route('/sign_in', methods=['POST'])
def sign_in():
    request_data = request.get_json()
    User.sign_up(request_data["email"], request_data["password"])

    return



# route to update user with PUT method
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    '''Function to edit user in our database using movie id'''
    request_data = request.get_json()
    User.update_user(id, request_data['name'], request_data['email'], request_data['password'])
    response = Response("User Updated", status=200, mimetype='application/json')
    return response


# route to delete user using the DELETE method
@app.route('/users/<int:id>', methods=['DELETE'])
def remove_user(id):
    '''Function to delete user from our database'''
    User.delete_user(id)
    response = Response("User Deleted", status=200, mimetype='application/json')
    return response
# route to get all users'

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({'Posts': Post.get_all_posts()})


# route to get user by id
@app.route('/posts/<int:id>', methods=['GET'])
def get_post_by_id(id):
    return_value = User.get_post(id)
    return jsonify(return_value)

@app.route('/posts', methods=['POST'])
def add_post():
    '''Function to add new post to our database'''
    request_data = request.get_json()  # getting data from client
    Post.add_post(request_data["title"], request_data["content"],
                    request_data["creat_at,"],request_data["update_at"], request_data["ranking"], request_data["view_number"])
    response = Response("post added", 201, mimetype='application/json')
    return response

# route to update post with PUT method
@app.route('/posts /<int:id>', methods=['PUT'])
def update_post(id):
    '''Function to edit post in our database using post id'''
    request_data = request.get_json()
    Post.update_movie(id, request_data["title"], request_data["content"],
                    request_data["creat_at,"],request_data["update_at"], request_data["ranking"], request_data["view_number"])
    response = Response("Post Updated", status=200, mimetype='application/json')
    return response


# route to delete user using the DELETE method
@app.route('/posts/<int:id>', methods=['DELETE'])
def remove_post(id):
    '''Function to delete post from our database'''
    User.delete_post(id)
    response = Response("Post Deleted", status=200, mimetype='application/json')
    return response

@app.route('/tags', methods=['GET'])
def get_tags():
    return jsonify({'Tags': Tag.get_all_posts()})


# route to get tag by id
@app.route('/tags/<int:id>', methods=['GET'])
def get_tag_by_id(id):
    return_value = User.get_tag(id)
    return jsonify(return_value)

@app.route('/tags', methods=['POST'])
def add_tag():
    '''Function to add new tag to our database'''
    request_data = request.get_json()  # getting data from client
    Post.add_tag(request_data["name"], request_data["category"],
                    request_data["creat_at,"],request_data["label"])
    response = Response("tag added", 201, mimetype='application/json')
    return response

# route to update user with PUT method
@app.route('/tags /<int:id>', methods=['PUT'])
def update_tags(id):
    '''Function to edit tag in our database using tag id'''
    request_data = request.get_json()
    Post.update_tag(id, request_data["name"], request_data["category"],
                    request_data["creat_at,"],request_data["label"])
    response = Response("Tag Updated", status=200, mimetype='application/json')
    return response


# route to delete user using the DELETE method
@app.route('/tags/<int:id>', methods=['DELETE'])
def remove_tags(id):
    '''Function to delete tag from our database'''
    User.delete_post(id)
    response = Response("Tag Deleted", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=1234, debug=True)

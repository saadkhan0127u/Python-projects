import facebook

def get_profile_info(user_id):
    token = 'your-access-token'
    graph = facebook.GraphAPI(access_token=token, version = 3.1)
    profile = graph.get_object(id=user_id, fields='name,location')

    return profile

print(get_profile_info('user-id'))

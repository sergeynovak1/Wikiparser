topics = {}


def create_topic(topic_name):
    topics[topic_name] = {'users': [], 'feeds': []}


def subscribe(user_id, topic):
    topics[topic]['users'].append(user_id)


def post_feed(topic, feed_id):
    topics[topic]['feeds'].append(feed_id)
    for user_id in topics[topic]['users']:
        print(f'пользователь {user_id} получил новость {feed_id}')

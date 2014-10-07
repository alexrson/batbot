import sys
import time
import praw

def monitor():
    already_replied = set()
    while True:
        already_replied = scan(already_replied)
        time.sleep(100)


def scan(already_replied=set([]), stimulus='swear to god', response='SWEAR TO ME'):
    r = praw.Reddit(user_agent='batbot_agent')
    username = 'PUTUSERNAMEHERE'
    password = 'PUTPASSOWORDHERE'
    r.login(username, password)
    for submission in r.get_front_page():
        print submission
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        time.sleep(2)
        for comment in flat_comments:
            time.sleep(1)
            if isinstance(comment, praw.objects.MoreComments):
                break
            if stimulus.lower() in str(comment).lower() and \
              str(comment.author) != username:
                if not comment.id in already_replied:
                    print 'found comment which meets criterion', comment.permalink
                    print str(comment).lower()
                    already_replied.add(comment.id)
                    if username in [str(rpl.author) for rpl in extract_all_general(comment.replies)]:
                        already_replied.add(comment.id)
                    else:
                        time.sleep(10 * 60)
                        comment.reply(response)
                        print 'JUST COMMENTED', comment.permalink
                        print time.time(), '\n'
                        time.sleep(5)
    return already_replied 


def extract_all_general(comments):
    if not comments:
        return []
    all_comments = comments[:-1]
    if isinstance(comments[-1], praw.objects.MoreComments):
        return all_comments + extract_all_general(comments[-1].comments())
    else:
        return all_comments + [comments[-1]]


if __name__ == '__main__':
    if '--scan' in sys.argv:
        scan()
    elif '--monitor':
        monitor()

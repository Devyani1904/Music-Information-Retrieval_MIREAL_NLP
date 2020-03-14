from IPython.core.display import display

emotions = ['joy', 'trust', 'sadness', 'disgust', 'anger', 'fear', 'anticipation', 'surprise']


def print_time(t):
    """
    Prints human readable time, sort-of (if humans read milliseconds too)
    """
    m = int(t // 60 % 60)
    s = int(t % 60)
    ms = round((t - int(t)) * 1000)
    if m > 0:
        print("{0}m".format(m), end=' ')
    if s > 0:
        print("{0}s".format(s), end=' ')
    print("{0}ms".format(ms))


def display_song_topics(song, data, labels=None, t=False):
    """

    Displays topics associated with a song.

    Adds 1 to the topic indexes to make them correspond to the pyLDAvis topic numbers.

    """
    if type(song) is str:
        if labels is not None:
            d = data[data['song'] == song][['song', 'artist', 'topics', *list(sorted(labels))]]
        else: 
            d = data[data['song'] == song][['song', 'artist', 'topics']]
        d.topics = d.topics + 1
        if t:
            d=d.T
            d.columns = d.loc['artist'].values + " - " + d.loc['song'].values
        display(d)
        return d
    elif type(song) is list:
        if labels is not None:
            d = data[data['song'].isin(song)][['song', 'artist', 'topics', *list(sorted(labels))]]
        else: 
            d = data[data['song'].isin(song)][['song', 'artist', 'topics']]
        d.topics = d.topics + 1
        if t:
            d=d.T
            d.columns = d.loc['artist'].values + " - " + d.loc['song'].values
        display(d)
        return d

        
def display_song_emotions(song, data):
    if type(song) is str:
        display(data[data['song'] == song][['song', 'artist', *emotions]])
    elif type(song) is list:
        display(data[data['song'].isin(song)][['song', 'artist', *emotions]])

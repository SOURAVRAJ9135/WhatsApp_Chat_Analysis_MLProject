from urlextract import URLExtract
extractor=URLExtract()

def fetch_stats(selected_user,df):

    if selected_user!= "Overall":
        df = df[df['user']==selected_user]
    
    # fetch no of messages
    num_messages = df.shape[0]

    #fetch no of words
    words=[]
    for message in df['message']:
        words.extend(message.split())

    #fetch no of media used
    num_media=df[df['message']=='<Media omitted>\n'].shape[0]

    # fetch no of link shared
    links=[]
    for message in df['message']:
        links.extend(extractor.find_urls(message))

    return num_messages,len(words),num_media,len(links)

    

    



    # if selected_user== "Overall":
    #     # fetch no of messages
    #     num_messages=df.shape[0]
    #     # fetch no of words
    #     words=[]
    #     for message in df['message']:
    #         words.extend(message.split())

    #     return num_messages,len(words)
    
    # else:
    #     new_df= df[df['user']== selected_user]
    #     num_messages= new_df.shape[0]
    #     words=[]
    #     for message in new_df['message']:
    #         words.extend(message.split())

    #     return num_messages,len(words)

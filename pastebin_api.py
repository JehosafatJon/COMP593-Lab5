import requests as r

POST_URL = 'https://pastebin.com/api/api_post.php'

def main():
    pass

def create_new_paste(title, body_text, expiration='1M', listed=False):
    """ Posts a new paste to PasteBin

    Args:
        title (str): Paste Title
        body_text (str): Paste body text
        expiration (str, optional): Expiration date of pase (N - never, 10M - minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool, optional): Whether paste is publicly listed (True) or not (False)
    
    Reeturns: 
        str: URL of new paste, if successful. Otherwise None.
    """

    # Create a dictionary of paramter values
    request_data = {
        'api_dev_key': 'CRmDgqN3zsrXtqtPa7MKOYC5wvrYKnU_',
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_private': 0 if listed else 1,
        'api_paste_expire_date': expiration
    }


    print("Posting a new paste to PasteBin...", end=' ')
    resp_msg = r.post(POST_URL, data=request_data)
    
    # Checks success or failure of post and returns
    if resp_msg.status_code == r.codes.ok:
        print('Success!')
        return resp_msg.text
    else:
        print('Failed!')
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"{resp_msg.text}")
        return
    
if __name__ == '__main__':
    main()
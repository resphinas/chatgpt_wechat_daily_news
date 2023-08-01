import datetime
import logging
import sys
import threading
import time
import traceback

from baidu_hot_rank import getContext
from lib import itchat
from news_spider import spider_techcruch, spider_inner, spider_jiqizhixin, spider_scitechdaily, spider_venturebeat, \
    spider_it_daily

try:
    import Queue
except ImportError:
    import queue as Queue

from ..log import set_logging
from ..utils import test_connect
from ..storage import templates

logger = logging.getLogger('itchat')





def run_at_noon():
    now = datetime.datetime.now()
    # [a,b,c,d] = open("noon_test_time.txt","r").read().split()
    # a = int(a)
    # b = int(b)
    # c = int(c)
    # d = int(d)
    #
    # if now.hour == a :
    #     if d ==0:
    #         with open("noon_test_time.txt","w",encoding="utf-8") as file:
    #             file.write(f"{a} {b} {c} 1")
    #
    #         return 1
    #
    #     else:
    #         return 0
    # else:
    #     return 0
    if now.hour == 8 and now.minute == 0 and now.second<2:
        return 1

def run_at_minute(minute):
    now = datetime.datetime.now()
    if  now.minute % minute ==0 and now.second >30 and now.second <35 :
        return 1
    else:
        return 0

def load_register(core):
    core.auto_login       = auto_login
    core.configured_reply = configured_reply
    core.msg_register     = msg_register
    core.run              = run

def auto_login(self, hotReload=False, statusStorageDir='itchat.pkl',
        enableCmdQR=False, picDir=None, qrCallback=None,
        loginCallback=None, exitCallback=None):
    if not test_connect():
        logger.info("You can't get access to internet or wechat domain, so exit.")
        sys.exit()
    self.useHotReload = hotReload
    self.hotReloadDir = statusStorageDir
    if hotReload:
        rval=self.load_login_status(statusStorageDir,
                loginCallback=loginCallback, exitCallback=exitCallback)
        if rval:
            return
        logger.error('Hot reload failed, logging in normally, error={}'.format(rval))
        self.logout()
        self.login(enableCmdQR=enableCmdQR, picDir=picDir, qrCallback=qrCallback,
            loginCallback=loginCallback, exitCallback=exitCallback)
        self.dump_login_status(statusStorageDir)
    else:
        self.login(enableCmdQR=enableCmdQR, picDir=picDir, qrCallback=qrCallback,
            loginCallback=loginCallback, exitCallback=exitCallback)


import pickle

# 将字典保存到文件
def save_dict_to_file(dict_data, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(dict_data, file)

# 从文件中读取字典
def load_dict_from_file(file_path):
    with open(file_path, "rb") as file:
        dict_data = pickle.load(file)
    return dict_data

def configured_reply(self,time_flag,diy_msg):
    ''' determine the type of message and reply if its method is defined
        however, I use a strange way to determine whether a msg is from massive platform
        I haven't found a better solution here
        The main problem I'm worrying about is the mismatching of new friends added on phone
        If you have any good idea, pleeeease report an issue. I will be more than grateful.
    '''
    if  time_flag==1:

        # 从文件中加载字典
        # msg_dict = load_dict_from_file("function_dict1.pkl")
        # loaded_dict = load_dict_from_file("function_dict.pkl").get("Text")

        """
            def send(self, reply: Reply, context: Context):
        receiver = context["receiver"]
        """
        # weathers = get_weather()
        try:
            content = spider_techcruch() + "\n\n" + spider_inner()
        except Exception as file:
            print(file)
            print("定位锚21")
        # print(msg_dict.get('FromUserName'))
        # memberList = itchat.update_chatroom(chatroom_name)

        # users = memberList["MemberList"]
        # for detail in users:
        #
        #     if detail["NickName"] == "resphina":
        #         user_name = detail["UserName"]
        # print(chatroom)
        # print(memberList)
        chatroom_name = itchat.search_chatrooms(name='软考冲刺过过过！')[0]['UserName']
        itchat.send(content, toUserName=chatroom_name)

        # itchat.send(content, toUserName=msg_dict.get('FromUserName'))
    # replyFn = loaded_dict
    elif time_flag ==2:
        try:
            # 从文件中加载字典
            # msg_dict = load_dict_from_file("function_dict1.pkl")
            # loaded_dict = load_dict_from_file("function_dict.pkl").get("Text")
            result = spider_jiqizhixin()
            result2=spider_scitechdaily()
            result3 = spider_venturebeat()
            result4 = spider_it_daily()
            result5 = getContext(2)
            if result != None:
                print(result)
            if result != None:

                chatroom_name = itchat.search_chatrooms(name='软考冲刺过过过！')[0]['UserName']
                itchat.send(result, toUserName=chatroom_name)
            else:
                print("机器之心心跳")

            if result2 != None:

                chatroom_name = itchat.search_chatrooms(name='软考冲刺过过过！')[0]['UserName']
                itchat.send(result2, toUserName=chatroom_name)
            else:
                print("每日科学心跳")

            if result3 != None:

                chatroom_name = itchat.search_chatrooms(name='软考冲刺过过过！')[0]['UserName']
                itchat.send(result3, toUserName=chatroom_name)
            else:
                print("venturebeat心跳")

            if result4 != None:

                chatroom_name = itchat.search_chatrooms(name='软考冲刺过过过！')[0]['UserName']
                itchat.send(result4, toUserName=chatroom_name)

            if result5 != None:
                chatroom_name = itchat.search_chatrooms(name='软考冲刺过过过！')[0]['UserName']
                itchat.send(result5, toUserName=chatroom_name)
                # def send_message():
                #     chatroom_name = itchat.search_chatrooms(name='软考冲刺过过过！')[0]['UserName']
                #     itchat.send(result5, toUserName=chatroom_name)
                # timer = threading.Timer(1800, send_message)
                # timer.start()
                # time.sleep(1800)
            else:
                print("百度热搜心跳")
        except Exception as file:
            print(file,traceback.print_exc())
            time.sleep(0.5)
    elif time_flag == 3:
        try:
            # 从文件中加载字典
            # msg_dict = load_dict_from_file("function_dict1.pkl")
            # loaded_dict = load_dict_from_file("function_dict.pkl").get("Text")
            result5 = getContext(1)

            if result5 != None:
                chatroom_name = itchat.search_chatrooms(name='28')[0]['UserName']
                itchat.send(result5, toUserName=chatroom_name)
            else:
                print("百度热搜心跳")
        except Exception as file:
            print(file, traceback.print_exc())
            time.sleep(0.5)


    try:
        msg = self.msgList.get(timeout=1)
    except Queue.Empty:
        pass
    else:
        if isinstance(msg['User'], templates.User):
            replyFn = self.functionDict['FriendChat'].get(msg['Type'])
        elif isinstance(msg['User'], templates.MassivePlatform):
            replyFn = self.functionDict['MpChat'].get(msg['Type'])

        elif isinstance(msg['User'], templates.Chatroom):
            # print(self.functionDict['GroupChat'])
            # print(msg)
            # # 保存字典到文件
            try:
                save_dict_to_file(self.functionDict['GroupChat'], "function_dict.pkl")
                save_dict_to_file(msg, "function_dict1.pkl")
            except:
                pass

            # 从文件中加载字典
            # loaded_dict = load_dict_from_file("function_dict.pkl")['GroupChat'].get(msg['Type'])
            # print("new dict",loaded_dict)

            # replyFn = loaded_dict


            #原始代码
            replyFn = self.functionDict['GroupChat'].get(msg['Type'])
        if replyFn is None:
            r = None
        else:
            try:
                r = replyFn(msg)
                if r is not None:

                    #原始代码
                    self.send(r, msg.get('FromUserName'))
            except:
                logger.warning(traceback.format_exc())

def msg_register(self, msgType, isFriendChat=False, isGroupChat=False, isMpChat=False):
    ''' a decorator constructor
        return a specific decorator based on information given '''
    if not (isinstance(msgType, list) or isinstance(msgType, tuple)):
        msgType = [msgType]
    def _msg_register(fn):
        for _msgType in msgType:
            if isFriendChat:
                self.functionDict['FriendChat'][_msgType] = fn
            if isGroupChat:
                self.functionDict['GroupChat'][_msgType] = fn
            if isMpChat:
                self.functionDict['MpChat'][_msgType] = fn
            if not any((isFriendChat, isGroupChat, isMpChat)):
                self.functionDict['FriendChat'][_msgType] = fn
        return fn
    return _msg_register






def run(self, debug=False, blockThread=True):
    logger.info('Start auto replying.')
    if debug:
        set_logging(loggingLevel=logging.DEBUG)
    def reply_fn():
        try:
            self.last_time =int(time.time())
            while self.alive:
                #心跳包定位
                # print("test")
                current_time = int(time.time())
                if run_at_noon():
                    # print("Time pass")
                    self.configured_reply(1,"测试  time="+ str(current_time))
                    self.last_time = current_time

                    continue
                elif run_at_minute(12):
                    self.configured_reply(2, "测试  time=" + str(current_time))

                elif run_at_minute(30):
                    self.configured_reply(3, "测试  time=" + str(current_time))
                else:
                    logging.info("time not equal")

                self.configured_reply(False,None)
        except KeyboardInterrupt:
            if self.useHotReload:
                self.dump_login_status()
            self.alive = False
            logger.debug('itchat received an ^C and exit.')
            logger.info('Bye~')
    if blockThread:
        reply_fn()
    else:
        replyThread = threading.Thread(target=reply_fn)
        replyThread.setDaemon(True)
        replyThread.start()

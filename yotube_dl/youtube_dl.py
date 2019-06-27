from selenium import webdriver
import subprocess
import time
import os

# 1:目标UP主视频列表地址(Target_list)及对应标题（title）
Target_list = {"https://www.youtube.com/channel/UCJKv6SFOF7uHjD7ou8gxWFQ/videos": "野合"}

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
DRIVER_PATH = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# 查询视频信息语句
COMMAND_PREFIX_CHECK = 'youtube-dl -F '
# 下载1080p视频语句
COMMAND_PREFIX_DOWNLOAD = 'youtube-dl -f 137+140 '


class YoutubeDL(object):
    # 2:遍历Target_list，提取视频url_list,并保存在以title命名的目录下的url_list.txt文件内.

    def __init__(self, target_url):
        self.target_url = target_url
        self.Path = ABS_PATH + r'\\' + Target_list[self.target_url]
        self.Txt_path = self.Path + r"\url_list.txt"
        self.url_ilst = []

    def crater_path(self):  # 根据字典生成目录
        try:
            os.mkdir(self.Path)
        except Exception as f:
            print(f)

    def get_video_list(self):  # 抓取列表-保存到指定目录下的url_list.txt
        self.web_driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.web_driver.get(self.target_url)
        self.roll_page()
        url_temp = self.web_driver.find_elements_by_xpath('//a[@id="video-title"]')
        for url in url_temp:
            self.url_ilst.append(url.get_attribute("href"))
        self.web_driver.close()

    def save_txt(self):
        fobj = open(self.Txt_path, 'a')
        for url in self.url_ilst:
            fobj.write(url + "\n")

    def roll_page(self):
        js = "var q=document.documentElement.scrollTop={}".format(2 * 10000)
        self.web_driver.execute_script(js)
        time.sleep(1)

    def check_txt(self):  # 查有无txt，无则新建下载列表。有则执行check_video_list
        if os.path.exists(self.Txt_path):
            print("txt文件已存在,将进行更新处理")
            self.check_video_url()
            for url in self.url_ilst:
                self.download_by_url(url)

        else:
            print("txt文件不存在,将全新下载")
            self.get_video_list()
            self.save_txt()
            for url in self.url_ilst:
                self.download_by_url(url)
            subprocess.Popen("move *.mp4 " + r"E:\youtube下载\yotube_dl\野合", shell=True)  # 将视频转移到指定目录


    def check_video_url(self):  # 过滤列表。将无下载的链接放到url_list.txt中，新内容放到开头。
        print("正在进行更新处理")
        fobj = open(self.Txt_path, 'r+')
        last_url = fobj.readline().strip()
        self.get_video_list()
        for url in self.url_ilst:
            if url == last_url:
                del self.url_ilst[self.url_ilst.index(url):]
        fobj = open(self.Txt_path, 'a')
        fobj.seek(0, 0)
        for url in self.url_ilst:
            fobj.write(url + "\n")

    """通过网址下载视频"""
    @staticmethod
    def download_by_url(url):
        p = subprocess.Popen(COMMAND_PREFIX_DOWNLOAD + url, shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        start = time.time()
        print("********\tStart download:" + url + "\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))
        while True:
            line = p.stdout.readline()
            if line:
                print(line.decode("gbk").strip('\n'))
            else:
                break
        p.wait()
        end = time.time()
        print("********\tEnd\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end)), )
        print("taking：" + str(int(end - start)) + " seconds")

    def main(self):
        self.crater_path()     # 创建目录
        self.check_txt()       # 检查是否有txt,无则重新下载。有则做过滤处理


for x in Target_list.keys():
    t = YoutubeDL(x)
    t.main()
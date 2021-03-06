#encoding: utf-8
from spider import HuangliSpider



def show_chinese_day():
   year , month , day ,time = HuangliSpider().get_current_calender()
   print("当前干支:")
   print("{} {} {} {}".format(year,month,day,time))






def main():
    show_chinese_day()














if __name__ == '__main__':
    main()


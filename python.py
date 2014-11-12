#-*-coding=utf-8
from selenium import webdriver
import random,string,re,time

captial = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
number = '1234567890'
unnormal = '~!@#$%^&*()_+}{|":?><[];\/.,*'


def check_c_n(input):
    l = len(input)
    i = 2
    r = True
    if cmp(input[:1],'-')==0 or cmp(input[l-1:l],'-') == 0:
        r = False
    else :
        while i < l:
            tmp = re.search(input[i-1:i],captial+lower+number+'-')
            if tmp == None:
                r = False
                break
            else :
                i +=1
    return r
 
def print_doc():
    """ll第三饭打算的ll"""
def doule_array():
    lists = [[0] * 3 for row in range(10)]
    lists[0][0] = 'Love China'
    lists[0][1] = 'ddddd'
    lists[0][2] = 'kkkkk'
    print lists[0][0]
    print lists[0][1]
    print lists[0][2]
    
def genMatrix(rows,cols):
    matrix = [[4 for col in range(cols)] for row in range(rows)]
    for i in range(rows):
        for j in range(cols):
            print matrix[i][j],
        print '\n'
def underline():
    captial = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    number = '1234567890'
    unnormal = '~!@#$%^&*()-+}{|":?><[];\/.,*'
#     b = True
#     a = ''
#     while b:
#         while re.search('_',a) == None:
#             a = string.join(random.sample(captial+ lower + '_',6)).replace(" ","")
#         l = len(a)
#         print a
#         if cmp(a[:1],'_')== 0 or cmp(a[l-1:l],'_') == 0:
#             b = True
#             a = ''
#         else:
#             b = False

def is_in(input,value):
    lv = len(value)
    k = 0
    n = 0
    while k < lv+1:
        tmp = cmp(input,value[k-1:k])
        if tmp == 0:
            n += 1
        k += 1
    print n

def is_email(input1,input2,value):
    ascii = [45,46,48,49,50,51,52,53,54,55,56,57,64,65,66,57,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,103,104,106,105,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
    k = len(value) 
    i = 0
    p = []#点的个数
    tf = True
    while i<k:
        if ord(value[i]) not in ascii:
            tf = False
            print '含有中文字符'
            break
        else:
            tf = True
        i += 1
    i = 0
    if tf ==True:
        if len(re.findall(input1,value))!=1:
            tf = False
            print '没有@或多于1个@，测试失败'
        elif re.search('^'+input1,value) != None or re.search(input1+'$',value) != None:
            tf = False
            print '@处于首或尾，测试失败'
        else:
            start = re.search(input1,value).start()#@的个数及位置
            i = 0
            while i <k:
                if re.search('^\\'+input2,value) != None or re.search("\\" + input2 + '$',value[:start]) != None or re.search('^\\'+input2,value[start+1:k]) != None or re.search("\\" + input2+'$',value) != None:
                    tf = False
                    print '.位于首尾'
                    break
                else:
                #判断@之前的点
                    for m in re.finditer("\\" + input2,value[:start]):
                        p.append(m.start())
                #判断@之后的点
                    for n in re.finditer("\\" + input2,value[start+1:]):
                        p.append(n.start())
                i += 1
            ii = 0
            if len(re.findall("\\" + input2,value[start+1:]))==0:
                tf = False
                print '邮箱后缀没有点'
            else:
                while ii<len(p)-1:
                    if p[ii+1] - p[ii] == 1:
                         print "两个'.'相邻"
                         tf = False
                         break
                    else:
                        tf = True
                    ii +=1
    if tf == True:
        print '测试通过'
    else:
        print '测试失败'
#     i = 0
#     msgt = ''
#     msgf = ''
#     tf = True
#     while i < n:
#         if poa[0][0] != 0 :#.不在在字符串之首
#             if poa[n-1][0]== 12:#.在@前一位
#                 msgt += '.不在@前一位 True'
#                 tf = True
#             else:
#                 msgf += '.在@前一位 Fasle'
#                 tf = False
#                 break
#             if poa[i+1][0] - poa[i][0] != 1:
#                 msgt += '两个点不相邻 True'
#                 tf = True
#             else:
#                 msgf += '两个.相邻 False'
#                 tf = False
#                 break
#         else:
#             tf = False
#             msgf += '在字符串之首 False '
#             break
#         i += 1
#         
#     if tf == True:
#         print '测试通过，因为： ' + msgt
#     else:
#         print '测试失败，因为： ' + msgf
    
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")
    driver.get_screenshot_as_file("/tmp/baidu.png")
    time.sleep(3)
    driver.quit()
#     phone = 'phone'
#     msg1= 'username:scutech'
#     msg2 = 'password:dingjia123'
#     res = 'pass'
#     fobj = open('/tmp/autotest_result/test.html','w')
#     fobj.write('<html>' + '\n')
#     fobj.write('<body>' + '\n')
#     fobj.write('<table border="1"><tr><th>test_item</th><td>test_miaoshu</td><td>test_result</td></tr>')
#     fobj.write('<tr><th rowspan="3">'+phone+'</th><td>'+msg1+'</br>'+msg2+'</td><td>'+res+'</td></tr>')
#     fobj.write('<tr><td>'+msg1+'</br>'+msg2+'</td><td>'+res+'</td></tr>')
#     fobj.write('<tr><td>'+msg1+'</br>'+msg2+'</td><td>'+res+'</td></tr></table>')
#     fobj.write('</body>' + '\n')
#     fobj.write('</html>' + '\n')
#     fobj.close()
    

#     is_Email('@','.','jlsd@k.jfoe第三饭i')
#     a = 'sdferfe@fsgfsefe'
#     print len(re.findall('@',a))
#     print re.search('@',a).start()
#     is_in('.','sdfsd@sfe@waae..a')
#     a = '8xKGbeNE5XZ1QJlgFwaoO3I0zdScA_T2'
#     b = []
#     b.append(a)
#     print b
#     tmp = re.search('\\','dsfdsfewfew')
#     print tmp
#     print type(ord('?'))
#     r = check_c_n('iwGFGHFGHFjoifjiofj9899^&*88***************789')
#     print r   g
#     print print_doc.__doc__
    #genMatrix(3,4)
#     doule_array()
#     print string.join(random.sample('sdfoiojkrwkf;lskp',8)).replace(" ","")
#    i = 0
#c_l = []
#c_n = []
#l_n = []
#c_l_n = []
#c_l_n_u = []
#while i < 10 :
#    num = random.randint(0,30)
#    a = string.join(random.sample(captial + lower + '-',num)).replace(" ","")  #大写+小写
#    b = string.join(random.sample(captial + number + '-',num)).replace(" ","") #大写+数字
#    c = string.join(random.sample(lower + number + '-',num)).replace(" ","")   #小写+数字
#    d = string.join(random.sample(captial + lower + number + '-',num)).replace(" ","") #大写+小写+数字
#    e = string.join(random.sample(captial + lower + number + unnormal + '-',num)).replace(" ","") #大写+小写+数字+特殊字符
#    c_l.append(a)
#    c_n.append(b)
#    l_n.append(c)
#    c_l_n.append(d)
#    c_l_n_u.append(e)
#    i += 1
#print c_l
#print c_n
#print l_n
#print c_l_n
#print c_l_n_u


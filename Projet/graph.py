from tkinter import *
import analyse

with open("test-4.txt", 'r') as f:
    with open("trame_4.txt", 'w') as f_out:
        for line in f.readlines():
            if line != '\n' and line[0] == '0':
                f_out.writelines(line.replace(line[0:6],'').replace(line[54:],'').replace('\n',''))
            else:
                if line == '\n':
                    f_out.writelines(line)
                else:
                    f_out.writelines('\n')

with open("trame_4.txt",'r') as f:
    l_tous = []
    for line in f.readlines():
        line = line.strip('\n')  # 去掉列表中每一个元素的换行符
        if not line == '':
            l_tous.append(line[0:])

# Il faut que modifier
ip_local = "192.168.31.69"
def printFlecheOuEspace(n,type):
    s=''
    if type == 0:
        for i in range(0,n-1):
            s = s+'-'
    else:
        for i in range(0,n-1):
            s = s+' '
    return s

colors = '''#FFB6C1 LightPink 浅粉红
,#FFC0CB Pink 粉红
,#DC143C Crimson 深红/猩红
,#FFF0F5 LavenderBlush 淡紫红
,#DB7093 PaleVioletRed 弱紫罗兰红
,#FF69B4 HotPink 热情的粉红
,#FF1493 DeepPink 深粉红
,#C71585 MediumVioletRed 中紫罗兰红
,#DA70D6 Orchid 暗紫色/兰花紫
,#D8BFD8 Thistle 蓟色
,#DDA0DD Plum 洋李色/李子紫
,#EE82EE Violet 紫罗兰
,#FF00FF Magenta 洋红/玫瑰红
,#FF00FF Fuchsia 紫红/灯笼海棠
,#8B008B DarkMagenta 深洋红
,#800080 Purple 紫色
,#BA55D3 MediumOrchid 中兰花紫
,#9400D3 DarkViolet 暗紫罗兰
,#9932CC DarkOrchid 暗兰花紫
,#4B0082 Indigo 靛青/紫兰色
,#8A2BE2 BlueViolet 蓝紫罗兰
,#9370DB MediumPurple 中紫色
,#7B68EE MediumSlateBlue 中暗蓝色/中板岩蓝
,#6A5ACD SlateBlue 石蓝色/板岩蓝
,#483D8B DarkSlateBlue 暗灰蓝色/暗板岩蓝
,#0000FF Blue 纯蓝
,#0000CD MediumBlue 中蓝色
,#191970 MidnightBlue 午夜蓝
,#00008B DarkBlue 暗蓝色
,#000080 Navy 海军蓝
,#4169E1 RoyalBlue 皇家蓝/宝蓝
,#6495ED CornflowerBlue 矢车菊蓝
,#B0C4DE LightSteelBlue 亮钢蓝
,#778899 LightSlateGray 亮蓝灰/亮石板灰
,#1E90FF DodgerBlue 闪兰色/道奇蓝
,#F0F8FF AliceBlue 爱丽丝蓝
,#4682B4 SteelBlue 钢蓝/铁青
,#87CEFA LightSkyBlue 亮天蓝色
,#87CEEB SkyBlue 天蓝色
,#00BFFF DeepSkyBlue 深天蓝
,#ADD8E6 LightBlue 亮蓝
,#B0E0E6 PowderBlue 粉蓝色/火药青
,#5F9EA0 CadetBlue 军兰色/军服蓝
,#F0FFFF Azure 蔚蓝色
,#00FFFF Cyan 青色
,#00CED1 DarkTurquoise 暗绿宝石
,#2F4F4F DarkSlateGray 暗瓦灰色/暗石板灰
,#008B8B DarkCyan 暗青色
,#008080 Teal 水鸭色
,#48D1CC MediumTurquoise 中绿宝石
,#20B2AA LightSeaGreen 浅海洋绿
,#40E0D0 Turquoise 绿宝石
,#7FFFD4 Aquamarine 宝石碧绿
,#66CDAA MediumAquamarine 中宝石碧绿
,#00FA9A MediumSpringGreen 中春绿色
,#3CB371 MediumSeaGreen 中海洋绿
,#2E8B57 SeaGreen 海洋绿
,#F0FFF0 Honeydew 蜜色/蜜瓜色
,#8FBC8F DarkSeaGreen 暗海洋绿
,#32CD32 LimeGreen 闪光深绿
,#00FF00 Lime 闪光绿
,#228B22 ForestGreen 森林绿
,#008000 Green 纯绿
,#006400 DarkGreen 暗绿色
,#7FFF00 Chartreuse 黄绿色/查特酒绿
,#7CFC00 LawnGreen 草绿色/草坪绿
,#ADFF2F GreenYellow 绿黄色
,#556B2F DarkOliveGreen 暗橄榄绿
,#9ACD32 YellowGreen 黄绿色
,#6B8E23 OliveDrab 橄榄褐色
,#FAFAD2 LightGoldenrodYellow 亮菊黄
,#FFFF00 Yellow 纯黄
,#808000 Olive 橄榄
,#BDB76B DarkKhaki 暗黄褐色/深卡叽布
,#FFFACD LemonChiffon 柠檬绸
,#EEE8AA PaleGoldenrod 灰菊黄/苍麒麟色
,#F0E68C Khaki 黄褐色/卡叽布
,#FFD700 Gold 金色
,#DAA520 Goldenrod 金菊黄
,#B8860B DarkGoldenrod 暗金菊黄
,#FDF5E6 OldLace 老花色/旧蕾丝
,#F5DEB3 Wheat 浅黄色/小麦色
,#FFE4B5 Moccasin 鹿皮色/鹿皮靴
,#FFA500 Orange 橙色
,#FFEFD5 PapayaWhip 番木色/番木瓜
,#DEB887 BurlyWood 硬木色
,#FFE4C4 Bisque 陶坯黄
,#FF8C00 DarkOrange 深橙色
,#FAF0E6 Linen 亚麻布
,#CD853F Peru 秘鲁色
,#FFDAB9 PeachPuff 桃肉色
,#F4A460 SandyBrown 沙棕色
,#D2691E Chocolate 巧克力色
,#8B4513 SaddleBrown 重褐色/马鞍棕色
,#FFF5EE Seashell 海贝壳
,#A0522D Sienna 黄土赭色
,#FFA07A LightSalmon 浅鲑鱼肉色
,#FF7F50 Coral 珊瑚
,#FF4500 OrangeRed 橙红色
,#E9967A DarkSalmon 深鲜肉/鲑鱼色
,#FF6347 Tomato 番茄红
,#FFE4E1 MistyRose 浅玫瑰色/薄雾玫瑰
,#FA8072 Salmon 鲜肉/鲑鱼色
,#FFFAFA Snow 雪白色
,#F08080 LightCoral 淡珊瑚色
,#BC8F8F RosyBrown 玫瑰棕色
,#CD5C5C IndianRed 印度红
,#FF0000 Red 纯红
,#A52A2A Brown 棕色
,#B22222 FireBrick 火砖色/耐火砖
,#8B0000 DarkRed 深红色
,#800000 Maroon 栗色
,#C0C0C0 Silver 银灰色
,#A9A9A9 DarkGray 深灰色
,#808080 Gray 灰色
,#696969 DimGray 暗淡灰
,#000000 Black 纯黑'''
l_CO = []
for each_color in colors.split(','):
    corlor_list =each_color.split(' ')
    l_CO.append(corlor_list[1])

window = Tk()
window.title('flow graph')
window.geometry('1500x800')

"""
filter les trames TCP et HTTP
"""
x = 100
lIP_D = []
l = [] # les tcp et http trames
lPosition_ip = {} #les positions dans le graphe
lPort = {} #keys sont les ip adresse , values sont les ports associe a chaque ip adresse
lColor = {}
j = 0
for i in range(0, len(l_tous)):
    if analyse.analyseMAC(l_tous[i])[2].__eq__("IP"): #IP trame
        if not len(analyse.analyseIP(l_tous[i])) == 0 and analyse.analyseIP(l_tous[i])[2].__eq__("TCP"):  # tcp trame
            if analyse.analyseIP(l_tous[i])[0].__eq__(ip_local) or analyse.analyseIP(l_tous[i])[1].__eq__(ip_local): #si les deux ip adresses contiennent la ip adresse locale
                l.append(l_tous[i])
                ip_Dst = analyse.analyseIP(l_tous[i])[1]
                if analyse.analyseIP(l_tous[i])[1].__eq__(ip_local):
                    ip_Dst = analyse.analyseIP(l_tous[i])[0]
                    if ip_Dst not in lIP_D:
                        lIP_D.append(ip_Dst)
                    if ip_Dst in lPort:
                        lPort[ip_Dst]['s'].append(analyse.analyseTCP(l_tous[i])['port_D'])
                        lPort[ip_Dst]['d'].append(analyse.analyseTCP(l_tous[i])['port_S'])
                        if analyse.analyseTCP(l_tous[i])['port_D'] not in  lColor:
                            lColor[analyse.analyseTCP(l_tous[i])['port_D']] = l_CO[j]
                            j = j+1
                    else:
                        lPort[ip_Dst] = {'s': [analyse.analyseTCP(l_tous[i])['port_D']],
                                         'd': [analyse.analyseTCP(l_tous[i])['port_S']]}
                        if analyse.analyseTCP(l_tous[i])['port_D'] not in lColor:
                            lColor[analyse.analyseTCP(l_tous[i])['port_D']] = l_CO[j]
                            j = j + 1
                    if ip_Dst not in lPosition_ip:
                        lPosition_ip[ip_Dst] = x
                        x = x + 100
                else:
                    if ip_Dst not in lIP_D:
                        lIP_D.append(ip_Dst)
                    if ip_Dst in lPort:
                        lPort[ip_Dst]['s'].append(analyse.analyseTCP(l_tous[i])['port_S'])
                        lPort[ip_Dst]['d'].append(analyse.analyseTCP(l_tous[i])['port_D'])
                        if analyse.analyseTCP(l_tous[i])['port_S'] not in lColor:
                            lColor[analyse.analyseTCP(l_tous[i])['port_S']] = l_CO[j]
                            j = j + 1
                    else:
                        lPort[ip_Dst] = {'s': [analyse.analyseTCP(l_tous[i])['port_S']],
                                         'd': [analyse.analyseTCP(l_tous[i])['port_D']]}
                        if analyse.analyseTCP(l_tous[i])['port_S'] not in lColor:
                            lColor[analyse.analyseTCP(l_tous[i])['port_S']] = l_CO[j]
                            j = j + 1
                    if ip_Dst not in lPosition_ip:
                        lPosition_ip[ip_Dst] = x
                        x = x + 100

print(l)
def filterTCP():
    lb.delete(0, END)
    text = ip_local
    for i in range(len(lIP_D)):
        text = text + printFlecheOuEspace(150, 1) + lIP_D[i]
    lb.insert(END, text)

    color = ""
    for i in range(0, len(l)):
        analyse_d = analyse.analyseTCP(l[i])
        ip_D = ""
        if analyse.analyseIP(l[i])[1] == ip_local:  # des = lo
            position = lPosition_ip[analyse.analyseIP(l[i])[0]]
            ip_D = analyse.analyseIP(l[i])[0]
        else:
            position = lPosition_ip[analyse.analyseIP(l[i])[1]]
            ip_D = analyse.analyseIP(l[i])[1]

        if analyse_d['port_S'] in lPort[ip_D]['s']:
            port_S = analyse_d['port_S']
            port_D = analyse_d['port_D']
        elif analyse_d['port_S'] in lPort[ip_D]['d']:
            port_S = analyse_d['port_D']
            port_D = analyse_d['port_S']
        color = lColor[port_S]
        info = '[' + analyse_d['flag'] + ']' + ' ' +' '+'Seq=' + analyse_d['seq'] +' '+'Ack='+ analyse_d['ack']+ ' ' + ' ' + 'Len=' + analyse_d['len']

        lb.insert(END, "                " + info)
        lb.itemconfig(END, bg=color)
        if analyse_d['port_S'].__eq__(port_S) and analyse_d['port_D'].__eq__(port_D):
            lb.insert(END, port_S + printFlecheOuEspace(position + int(position/100 - 1)*3, 0) + '>' + port_D)
            lb.itemconfig(END, bg=color)
        else:
            lb.insert(END, port_S + "<" + printFlecheOuEspace(position + int(position/100 - 1)*3, 0) + port_D)
            lb.itemconfig(END, bg=color)


def filterHTTP():
    lb.delete(0, END)
    text = ip_local
    for i in range(len(lIP_D)):
        text = text + printFlecheOuEspace(150, 1) + lIP_D[i]
    lb.insert(END,text)
    color = ""
    http_Response = ""
    for i in range(0, len(l)):
        analyse_d = analyse.analyseTCP(l[i])
        ip_D = ""
        if analyse.analyseIP(l[i])[1] == ip_local:  # des = lo
            position = lPosition_ip[analyse.analyseIP(l[i])[0]]
            ip_D = analyse.analyseIP(l[i])[0]
        else:
            position = lPosition_ip[analyse.analyseIP(l[i])[1]]
            ip_D = analyse.analyseIP(l[i])[1]

        if analyse_d['port_S'] in lPort[ip_D]['s']:
            port_S = analyse_d['port_S']
            port_D = analyse_d['port_D']
        elif analyse_d['port_S'] in lPort[ip_D]['d']:
            port_S = analyse_d['port_D']
            port_D = analyse_d['port_S']
        color = lColor[port_S]

        if analyse_d['flag'].__eq__("PSH,ACK") and not analyse_d['http'] == {}:  # http request ou reponse et trame contient http message
            if 'Request_Method' in analyse_d['http']:
                info = analyse_d['http']['Request_Method'] + ' ' + analyse_d['http']['Request_URI'] + ' ' + \
                       analyse_d['http']['Request_Version']
            else:
                info = analyse_d['http']['Response_version'] + ' ' + analyse_d['http']['Status_code'] + ' ' + \
                       analyse_d['http']['Response_Phrase']

            lb.insert(END, "               " + info)
            lb.itemconfig(END, bg=color)
            if analyse_d['port_S'].__eq__(port_S) and analyse_d['port_D'].__eq__(port_D):
                lb.insert(END, port_S + printFlecheOuEspace(position + int(position/100 - 1)*3,0) + '>' + port_D)
                lb.itemconfig(END, bg=color)
            else:
                lb.insert(END, port_S + "<" + printFlecheOuEspace(position + int(position/100 - 1)*3,0) + port_D)
                lb.itemconfig(END, bg=color)



def filter():
    lb.delete(0, END)
    with open('trame_analyse.txt','w') as f:
        f.truncate(0)
        text = ip_local
        t = ip_local
        for i in range(len(lIP_D)):
            text = text + printFlecheOuEspace(150, 1) + lIP_D[i]
            t = t + printFlecheOuEspace(90,1) + lIP_D[i]
        lb.insert(END, text)
        f.writelines(t)
        f.writelines('\n')

        color = ""
        http_Response = ""
        for i in range(0, len(l)):
            analyse_d = analyse.analyseTCP(l[i])
            ip_D = ""
            if analyse.analyseIP(l[i])[1] == ip_local:  # des = lo
                position = lPosition_ip[analyse.analyseIP(l[i])[0]]
                ip_D = analyse.analyseIP(l[i])[0]
            else:
                position = lPosition_ip[analyse.analyseIP(l[i])[1]]
                ip_D = analyse.analyseIP(l[i])[1]

            if analyse_d['port_S'] in lPort[ip_D]['s']:
                port_S = analyse_d['port_S']
                port_D = analyse_d['port_D']
            elif analyse_d['port_S'] in lPort[ip_D]['d']:
                port_S = analyse_d['port_D']
                port_D = analyse_d['port_S']
            color = lColor[port_S]

            if analyse_d['flag'].__eq__("SYN"):  # [SYN]
                info = '[' + analyse_d['flag'] + ']' + ' ' + 'Seq=' + analyse_d['seq'] + ' ' + 'Win=' + analyse_d['win'] + ' ' + 'Len=' + analyse_d['len'] + ' ' + 'MSS=' + analyse_d['MSS'] + ' ' + 'WS=' + analyse_d['WS']
                lb.insert(END, "              " + info)
                t = "              " + info
                f.writelines(t)
                f.writelines('\n')
                lb.itemconfig(END, bg=color)
                lb.insert(END, port_S + printFlecheOuEspace(position + int(position/100 - 1)*3, 0) + '>' + port_D)
                t = port_S + printFlecheOuEspace(position + int(position/100 - 1)*3, 0) + '>' + port_D
                f.writelines(t)
                f.writelines('\n')
                lb.itemconfig(END, bg=color)

            elif analyse_d['flag'].__eq__("SYN,ACK"):  # [SYN,ACK]
                info = '[' + analyse_d['flag'] + ']' + ' ' + 'Seq=' + analyse_d['seq'] + ' ' + 'Ack=' + analyse_d[
                    'ack'] + ' ' + 'Win=' + analyse_d['win'] + ' ' + 'Len=' + analyse_d['len'] + ' ' + 'MSS=' + \
                       analyse_d['MSS'] + ' ' + 'WS=' + analyse_d['WS']
                lb.insert(END, "               " + info)
                t = "               " + info
                f.writelines(t)
                f.writelines('\n')
                lb.itemconfig(END, bg=color)
                lb.insert(END, port_S + '<' + printFlecheOuEspace(position + int(position/100 - 1)*3, 0) + port_D)
                t = port_S + '<' + printFlecheOuEspace(position + int(position/100 - 1)*3, 0) + port_D
                f.writelines(t)
                f.writelines('\n')
                lb.itemconfig(END, bg=color)

            else:  # d'autre flags
                if analyse_d['flag'].__eq__("PSH,ACK") and not analyse_d[
                                                                   'http'] == {}:  # http request ou reponse et trame contient http message
                    if 'Request_Method' in analyse_d['http']:
                        info = analyse_d['http']['Request_Method'] + ' ' + analyse_d['http']['Request_URI'] + ' ' + \
                               analyse_d['http']['Request_Version']
                    else:
                        info = analyse_d['http']['Response_version'] + ' ' + analyse_d['http']['Status_code'] + ' ' + \
                               analyse_d['http']['Response_Phrase']

                elif analyse_d['flag'].__eq__("PSH,ACK") and analyse_d['http'] == {}:  # tcp segment ou http_reponse
                    info = '[' + analyse_d['flag'] + ']' + ' ' + 'Seq=' + analyse_d['seq'] + ' ' + 'Ack=' + analyse_d['ack'] + ' ' + 'Win=' + analyse_d['win'] + ' ' + 'Len=' + analyse_d['len'] + ' ' + analyse_d['explain']
                    # print

                else:  # no data(ACK,FIN,RST)
                    info = '[' + analyse_d['flag'] + ']' + ' ' + 'Seq=' + analyse_d['seq'] + ' ' + 'Ack=' + analyse_d['ack'] + ' ' + 'Win=' + analyse_d['win'] + ' ' + 'Len=' + analyse_d['len']

                lb.insert(END, "               " + info)
                t = "               " + info
                f.writelines(t)
                f.writelines('\n')
                lb.itemconfig(END, bg=color)
                # print
                if analyse_d['port_S'].__eq__(port_S) and analyse_d['port_D'].__eq__(port_D):
                    lb.insert(END, port_S + printFlecheOuEspace(position + int(position/100 - 1)*3, 0) + '>' + port_D)
                    t = port_S + printFlecheOuEspace(position + int(position/100 - 1)*3, 0) + '>' + port_D
                    f.writelines(t)
                    f.writelines('\n')
                    lb.itemconfig(END, bg=color)
                else:
                    lb.insert(END, port_S + '<' + printFlecheOuEspace(position + int(position/100 - 1)*3, 0) + port_D)
                    t = port_S + '<' + printFlecheOuEspace(position + int(position/100 - 1)*3, 0) + port_D
                    f.writelines(t)
                    f.writelines('\n')
                    lb.itemconfig(END, bg=color)


def filterIP():
    lb.delete(0, lb.size())
    ip = var.get()
    print(ip)
    l1 = []
    for i in range(0, len(l)):
        if analyse.analyseIP(l[i])[0].__eq__(ip) or analyse.analyseIP(l[i])[1].__eq__(ip):
            l1.append(l[i])


    for i in range(0, len(l1)+1):
        if i == 0:
           lb.insert(END, ip_local +'                                                                                                 '+ip)
        else:
            analyse_d = analyse.analyseTCP(l1[i-1])

            if analyse.analyseIP(l1[i-1])[0].__eq__(ip):
                port_S = analyse_d['port_D']
                port_D = analyse_d['port_S']
            else:
                port_S = analyse_d['port_S']
                port_D = analyse_d['port_D']

            if analyse_d['flag'].__eq__("SYN"):  # [SYN]
                info = '[' + analyse_d['flag'] + ']' + ' ' + 'Seq=' + analyse_d['seq'] + ' ' + 'Win=' + analyse_d['win'] + ' ' + 'Len=' + analyse_d['len'] + ' ' + 'MSS=' + analyse_d['MSS'] + ' ' + 'WS=' + analyse_d['WS']
                lb.insert(END, "              " + info)
                lb.insert(END, port_S + '-------------------------------------------------------------------------' + '>' + port_D)

            elif analyse_d['flag'].__eq__("SYN,ACK"):  # [SYN,ACK]
                info = '[' + analyse_d['flag'] + ']' + ' ' + 'Seq=' + analyse_d['seq'] + ' ' + 'Ack=' + analyse_d['ack'] + ' ' + 'Win=' + analyse_d['win'] + ' ' + 'Len=' + analyse_d['len'] + ' ' + 'MSS=' + analyse_d['MSS'] + ' ' + 'WS=' + analyse_d['WS']
                lb.insert(END, "               " + info)
                lb.insert(END, port_S + '<' + '-------------------------------------------------------------------------' + port_D)

            else:  # d'autre flags
                if analyse_d['flag'].__eq__("PSH,ACK") and not analyse_d['http'] == {}:  # http request ou reponse et trame contient http message
                    if 'Request_Method' in analyse_d['http']:
                        info = analyse_d['http']['Request_Method'] + ' ' + analyse_d['http']['Request_URI'] + ' ' + \
                               analyse_d['http']['Request_Version']
                    else:
                        info = analyse_d['http']['Response_version'] + ' ' + analyse_d['http']['Status_code'] + ' ' + \
                               analyse_d['http']['Response_Phrase']

                elif analyse_d['flag'].__eq__("PSH,ACK") and analyse_d['http'] == {}:  # tcp segment ou http_reponse
                    info = '[' + analyse_d['flag'] + ']' + ' ' + 'Seq=' + analyse_d['seq'] + ' ' + 'Ack=' + analyse_d[
                        'ack'] + ' ' + 'Win=' + analyse_d['win'] + ' ' + 'Len=' + analyse_d['len'] + ' ' + analyse_d[
                               'explain']
                    # print

                else:  # no data(ACK,FIN,RST)
                    info = '[' + analyse_d['flag'] + ']' + ' ' + 'Seq=' + analyse_d['seq'] + ' ' + 'Ack=' + analyse_d[
                        'ack'] + ' ' + 'Win=' + analyse_d['win'] + ' ' + 'Len=' + analyse_d['len']

                lb.insert(END, "               " + info)
                # print
                if analyse_d['port_S'].__eq__(port_S) and analyse_d['port_D'].__eq__(port_D):
                    lb.insert(END,
                              port_S + '-------------------------------------------------------------------------' + '>' + port_D)
                else:
                    lb.insert(END,
                              port_S + '<' + '-------------------------------------------------------------------------' + port_D)



b1 = Scrollbar(window, width=20)
b1.pack(side=RIGHT, fill=Y)
b3 = Scrollbar(window, orient=HORIZONTAL, width=20)
b3.pack(side=BOTTOM, fill=X, anchor=S)
lb = Listbox(window, yscrollcommand=b1.set, xscrollcommand=b3.set, width=100)
lb.pack(side=LEFT, fill=BOTH)
b1.config(command=lb.yview)
b3.config(command=lb.xview)


Label(text='FilterIP :').place(x=910, y=0)
var = StringVar()
k = 20
for i in range(0, len(lIP_D)):
    Radiobutton(window, text=lIP_D[i],variable=var, value=lIP_D[i], command=filterIP).place(x=910, y = k)
    k = k+20


Label(text='Filter :').place(x=1100, y=80)
r1 = Radiobutton(window, text='tcp',value="tcp", command= filterTCP).place(x=1100, y=100)
r2 = Radiobutton(window, text='http',value="http", command= filterHTTP).place(x=1100, y=120)
r3 = Radiobutton(window, text='tous',value="tous", command= filter).place(x=1100, y=140)

window.mainloop()
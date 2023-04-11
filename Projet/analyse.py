str = 'e4 f0 42 3d fd c9 8c 85 90 c6 98 e5 08 00 45 00 01 2e 00 00 40 00 40 06 b6 4b c0 a8 01 16 c0 a8 01 18 ed 6e 1f 48 39 db d1 c2 42 0d 72 e3 80 18 08 0a 9f b3 00 00 01 01 08 0a 04 e6 ad e1 00 46 80 e4 47 45 54 20 2f 73 73 64 70 2f 64 65 76 69 63 65 2d 64 65 73 63 2e 78 6d 6c 20 48 54 54 50 2f 31 2e 31 0d 0a 48 6f 73 74 3a 20 31 39 32 2e 31 36 38 2e 31 2e 32 34 3a 38 30 30 38 0d 0a 43 6f 6e 6e 65 63 74 69 6f 6e 3a 20 6b 65 65 70 2d 61 6c 69 76 65 0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 20 4d 6f 7a 69 6c 6c 61 2f 35 2e 30 20 28 4d 61 63 69 6e 74 6f 73 68 3b 20 49 6e 74 65 6c 20 4d 61 63 20 4f 53 20 58 20 31 30 5f 31 35 5f 37 29 20 41 70 70 6c 65 57 65 62 4b 69 74 2f 35 33 37 2e 33 36 20 28 4b 48 54 4d 4c 2c 20 6c 69 6b 65 20 47 65 63 6b 6f 29 20 43 68 72 6f 6d 65 2f 31 30 37 2e 30 2e 30 2e 30 20 53 61 66 61 72 69 2f 35 33 37 2e 33 36 0d 0a 41 63 63 65 70 74 2d 45 6e 63 6f 64 69 6e 67 3a 20 67 7a 69 70 2c 20 64 65 66 6c 61 74 65 0d 0a 0d 0a'
str2 = '08 87 c6 41 53 10 8c 85 90 c6 98 e5 08 00 45 00 03 ef 00 00 40 00 40 06 71 79 c0 a8 01 16 a2 3e 61 93 ed 72 00 50 71 c8 6d 01 53 aa 25 f8 50 18 10 00 0f 82 00 00 50 4f 53 54 20 2f 6d 6d 74 6c 73 2f 30 38 36 38 62 64 39 38 20 48 54 54 50 2f 31 2e 31 0d 0a 41 63 63 65 70 74 3a 20 2a 2f 2a'
str3 = '50 64 2b 77 1e 81 f8 4d 89 70 1b ba 08 00 45 00 00 40 00 00 40 00 40 06 e5 46 c0 a8 1f 45 80 77 f5 0c f1 97 00 50 1c b4 fc d0 00 00 00 00 b0 02 ff ff fe c1 00 00 02 04 05 b4 01 03 03 06 01 01 08 0a d2 8c 04 cf 00 00 00 00 04 02 00 00       '

def analyseMAC(str):
    mac_D = str[0:17]
    mac_S = str[18:35]
    pro_Hex = ''.join(str[36:41].split())
    pro = ""
    if pro_Hex.__eq__("0800"):
        pro = "IP"
    return [mac_D, mac_S, pro]


def analyseIP(str):
    l=[]
    if analyseMAC(str)[2].__eq__("IP"):
        ipS_Hex = str[78:89]
        ipD_Hex = str[90:101]
        pro_Hex = str[69:71]
        ip_S = ''
        ip_D = ''
        protocol = ""
        i = 0
        while i < 11:
            if i == 9:
                ip_S = ip_S + '%d' % (int(ipS_Hex[i:i + 2], 16))
                ip_D = ip_D + '%d' % (int(ipD_Hex[i:i + 2], 16))
            else:
                ip_S = ip_S + '%d' % (int(ipS_Hex[i:i + 2], 16)) + '.'
                ip_D = ip_D + '%d' % (int(ipD_Hex[i:i + 2], 16)) + '.'
            i += 3
        if int(pro_Hex,16) == 6:
            protocol = "TCP"
        l = [ip_S, ip_D, protocol]

    return l



def analyseHTTP(str):
    Request_Method = ""
    if ''.join(str[0:11].split()).__eq__('504f5354'):
        Request_Method = "POST"
        str = str[12:]

    elif ''.join(str[0:9].split()).__eq__('474554'):
        Request_Method = "GET"
        str = str[9:]

    Request_URI_Hex = '0'
    Request_Version_Hex = '0'
    for i in range(0, len(str)):
        if str[i:i+2].__eq__('48') and str[i+3:i+5].__eq__("54")  and str[i+6:i+8].__eq__("54") and str[i+9:i+11].__eq__("50"):
            Request_URI_Hex = ''.join(str[3:i-3].split())
            Request_Version_Hex = ''.join(str[i:i+24].split())
            break
        i = i+3
    Request_URI = hex_to_str(Request_URI_Hex)
    Request_Version = hex_to_str(Request_Version_Hex)

    return {'Request_Method': Request_Method, 'Request_URI': Request_URI,'Request_Version': Request_Version}



def hex_to_str(s):
    str = bytes.fromhex(s).decode()
    return str



def analyseTCP(str):
    portS_Hex = ''.join(str[102:107].split()) # supprimer les espaces
    portD_Hex = ''.join(str[108:113].split())
    seq_Hex = ''.join(str[114:126].split())
    ack_Hex = ''.join(str[126:138].split())
    header_length_Hex = ''.join(str[138:139].split())
    flags_Hex = ''.join(str[139:143].split())
    win_Hex = ''.join(str[144:150].split())

    port_S = '%d' %(int(portS_Hex, 16))
    port_D = '%d' %(int(portD_Hex, 16))
    seq = '%d' %(int(seq_Hex, 16))
    ack = '%d' %(int(ack_Hex, 16))
    header_length = int(header_length_Hex, 16)
    data_position = 102 + header_length*4 + header_length*8
    MSS = ""
    WS = '0'
    length = '0'
    flag = ""
    explain = ""
    http = {}
    if int(flags_Hex, 16) == 2:
        flag = "SYN"
        MSS_Hex = ''.join(str[169:174].split())
        MSS = '%d' %(int(MSS_Hex, 16))
        WS = '64'
    elif int(flags_Hex, 16) == 18:
        flag = "SYN,ACK"
        MSS_Hex = ''.join(str[169:174].split())
        MSS = '%d' % (int(MSS_Hex, 16))
        WS = '128'

    elif int(flags_Hex, 16) == 16:
        flag = "ACK"
    elif int(flags_Hex, 16) == 24:
        flag = "PSH,ACK"
    elif int(flags_Hex, 16) == 17:
        flag = "FIN,ACK"
    elif int(flags_Hex, 16) == 4:
        flag = "RST"
    elif int(flags_Hex, 16) == 25:
        flag = "FIN,PSH,ACK"

    if flag.__eq__("PSH,ACK"):  # flag = PSH,ACK
        if ''.join(str[data_position:data_position+9].split()).__eq__('504f53') or ''.join(str[data_position:data_position+9].split()).__eq__('474554'):  # #si c'est une requete
            http = analyseHTTP(str[data_position:])
            length = '%d' % (len(''.join(str[data_position:].split())) / 2)
        else:  # web发送，可能是http回答，可能是其他数据
            if ''.join(str[data_position:data_position+12].split()).__eq__("48545450"):  # si contient http reponse
                http['Response_version'] = hex_to_str(''.join(str[data_position:data_position + 23].split()))
                http['Status_code'] = hex_to_str(''.join(str[data_position+26:data_position + 35].split()))
                http['Response_Phrase'] = hex_to_str(''.join(str[data_position+38:data_position + 44].split()))
                length = '%d' % (len(''.join(str[data_position:].split())) / 2)
            else:
                length = '%d' % (len(''.join(str[data_position:].split())) / 2)


    win = '%d' %(int(win_Hex, 16))




    return {'port_S':port_S , 'port_D':port_D, 'seq':seq, 'ack':ack,'len': length, 'flag':flag, 'win':win,'MSS':MSS,'WS':WS,'http':http, 'explain':explain}




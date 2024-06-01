import re

import requests
import re

"""第一次请求：获取 csrf 参数"""
# 跨站请求伪造令牌(Cross-Site Request Forgery Token)
# Web应用程序会要求携带CSRF令牌，以验证请求是否是合法的
headers = {
    'Cookie': 'uuid=8f794c7999cbe207a1a89e73ca6372dd54c7254ff96fdfb23615981e8c720032a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22uuid%22%3Bi%3A1%3Bs%3A32%3A%22034c9c2e96ee352f5284c1e35582d753%22%3B%7D; new_uuid=bde8294126c80ab28b4165d1e667718f58dc98e6afc2a9b43bac20cac30e8399a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22new_uuid%22%3Bi%3A1%3Bi%3A1%3B%7D; abuv=d8d72aaf0481426636b2b7b027a0b3663f2a9bba8823b7fdfb8b8777bbc88c8ea%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22abuv%22%3Bi%3A1%3Bs%3A32%3A%22bbd9a5a68307f31ec491ad4d86452002%22%3B%7D; _csrf-frontend=dfe72c5365c8250dc02c2868c4736b7bd57c9a285ce7bdd1066eca86d89aaa15a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22famGGN75F-KMXnoy0fIem2vsFl-Jpf51%22%3B%7D; FIRSTVISITED=1717050017.867; Hm_lvt_a0e66ced62f1926ee48b5f059ad9f039=1717050018; _identity-usernew=ce32b87868f533b3387505b0d3eacf4da00ff19a5b01d8669bce14cb2f5b5de4a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22_identity-usernew%22%3Bi%3A1%3Bs%3A53%3A%22%5B27960128%2C%22X9C-krBcVEshBv6hB1suO1kOaYj1ydQJ%22%2C2592000%5D%22%3B%7D; login-type=e5d0e9061cc4427689b18b97b2974f58b0d45df8c757f63d15e8a457257c9779a%3A2%3A%7Bi%3A0%3Bs%3A10%3A%22login-type%22%3Bi%3A1%3Bs%3A5%3A%22weixi%22%3B%7D; ISREQUEST=1; WEBPARAMS=is_pay=0; advanced-frontend=79cu9gv37mfudovqqilugblmp7; uv=21c13ffe8e3dce936f4eaec8c750b6ef5960d2c796c59a3f7913dfd353bb3b2ea%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22uv%22%3Bi%3A1%3Bs%3A32%3A%22026c0765554856419e662d99fc701cbf%22%3B%7D; REFERRER_COME_HOST=f41e51d037c2897e57c2a9dda6442eb540fd29361836255fc46ff0fe0e64fb73a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22REFERRER_COME_HOST%22%3Bi%3A1%3Bi%3A1%3B%7D; requestChannel=2a2e8f4187d8c2d1ac0057c74606a5ebea6bbff8f61590ff5d9c3d561b298997a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22requestChannel%22%3Bi%3A1%3Bs%3A9%3A%22natural%7C%7C%22%3B%7D; REFERRER_STATISTICS_RECHARGE=096c63594052fffbd27ac43f2d47f3affad46597297e41b6434c92e4a95a0fd8a%3A2%3A%7Bi%3A0%3Bs%3A28%3A%22REFERRER_STATISTICS_RECHARGE%22%3Bi%3A1%3Bi%3A2001%3B%7D; firstVisitData=1baedf2d14021a36deb4b7452c2caf274baae6f67287d436a33cdb4741987039a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22firstVisitData%22%3Bi%3A1%3Bi%3A27960128%3B%7D; ALLVIP_EXPIRE_FIRST=fbe6d758848746f9fae60bd7dd86a07580d660ab49523e345ee8b1869424ee67a%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22ALLVIP_EXPIRE_FIRST%22%3Bi%3A1%3Bi%3A1%3B%7D; activity-new-user=dad1a1aaa107542b63f76d17ac3fa999e7d5f07994247ccd49d2dcbd9d1d45c8a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22activity-new-user%22%3Bi%3A1%3Bi%3A1%3B%7D; IPSTRATIFIED=966e40c1416b75359e7b3f341114a552dfae4dfca5e31e2507764146d446f05ca%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22IPSTRATIFIED%22%3Bi%3A1%3Bi%3A1%3B%7D; ACTIVITY_20201221=1; Hm_lpvt_a0e66ced62f1926ee48b5f059ad9f039=1717085243',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
url = 'https://huke88.com/course/161468.html'
response = requests.get(url=url, headers=headers)
html = response.text
csrf = re.findall('<meta name="csrf-token" content="(.*?)">', html)[0]

"""第二次请求：获取 m3u8 链接 和 视频标题"""
# 1) 请求网址：Video-play
# （具体步骤：<网站按F12>--<搜索到video-play点击>--<Headers的General第一条Request URL:>--<复制进来>）
link = 'https://asyn.huke88.com/video/video-play'
# 2) 还需要请求参数
# （具体步骤：<网站按F12>--<搜索到video-play点一条>--<Headers右边找到Payload>--<复制进来>）
# 使用批量替换技巧，注意不要漏空格：<clrl+R>--<然后上面输入(.*?): (.*)>--<下面输入'$1': '$2',>--<最后replace All>
# 然后把前面获取到的csrf替换到字典的对应value处
data = {
    'id': '161468',
    'exposure': '0',
    'studySourceId': '2',
    'confirm': '0',
    'async': 'false',
    'isFreeLimit': '0',
    'isSeries': '0',
    '_csrf-frontend': csrf,
}
# 3) 发送请求，注意区分请求方法，这里变成Post了
# 一般来说，GET请求用于获取数据，例如搜索结果；
# 而POST请求用于提交数据，例如提交表单、上传文件等
# 用requests.post上传信息，并在左边变量中拿到了网页F12中可以看到的
# Headers第四个条目Response的数据，也可以去网页上去看一下是哪些data
json_data = requests.post(url=link, data= data, headers=headers).json()
# 4) 提取视频标题，通过key-value对从字典中取
title = json_data['catalogHeaderTitle']  # 从条目Response字典观察到catalogHeaderTitle是我们要的信息
# 5) 提取m3u8链接，通过key-value对从字典中取
m3u8_url = json_data['video_url']  # 从条目Response字典观察到video_url是我们要的信息
print(title)            #【版式设计】纯文字排版构图设计练习（一）
print(m3u8_url)         # https://m3u8.huke88.com/video/hls/v_1/2023-12-17/E9D9B
                        # D03-5747-FA16-E679-6C2DB60E8CE1.m3u8?pm3u8/0/deadline/
                        # 1717162408&e=1717122808&token=HUwgVvJnrW6fXOzqd_myfnE3
                        # FFoFLWJnNktg7ThD:BgEiDlwi9c0-HAhpabzz-FNokZI=

"""第三次请求：获取 所有ts链接"""
# 000063.ts 000064.ts 000065.ts 等等视频流文件
m3u8 = requests.get(url= m3u8_url, headers=headers).text
# 发现打印内容中有 METHOD=AES-128 ，说明存在AES加密
# URI="https://asyn.huke88.com/video/decrypt" | 密钥资源请求地址
# IV=0x30794560f7b3abbcdab6b336e84b61eb | 密钥偏移量
# /dg3OheJun-8XZgYF7RfgVdw0JxM=/loe6T66lScjfei7FciznaCg2lJ_F/000000.ts?e=1717162 | 这一长串是ts链接
print(m3u8)     # #EXTM3U
                # #EXT-X-VERSION:3
                # #EXT-X-MEDIA-SEQUENCE:0
                # #EXT-X-ALLOW-CACHE:YES
                # #EXT-X-TARGETDURATION:17
                # #EXT-X-KEY:METHOD=AES-128,URI="https://asyn.huke88.com/video/decrypt",IV=0x30794560f7b3abbcdab6b336e84b61eb
                # #EXTINF:16.733333,
                # /dg3OheJun-8XZgYF7RfgVdw0JxM=/loe6T66lScjfei7FciznaCg2lJ_F/000000.ts?e=1717162408&token=HUwgVvJnrW6fXOzqd_myfnE3FFoFLWJnNktg7ThD:16lwNOHjLZQbb6dqic-SKfy6WRc
                # #EXT-X-KEY:METHOD=AES-128,URI="https://asyn.huke88.com/video/decrypt",IV=0xb7dd6dc0248b372c96aacec4d0d726de
                # #EXTINF:8.333333,
                # /dg3OheJun-8XZgYF7RfgVdw0JxM=/loe6T66lScjfei7FciznaCg2lJ_F/000001.ts?e=1717162408&token=HUwgVvJnrW6fXOzqd_myfnE3FFoFLWJnNktg7ThD:-zwpC8T2SSxW1-EaQzidU4tk-88
                # #EXT-X-KEY:METHOD=AES-128,URI="https://asyn.huke88.com/video/decrypt",IV=0xf718384cb0603e2ad463ebd322a0f42f
                # #EXTINF:8.333333,
                # /dg3OheJun-8XZgYF7RfgVdw0JxM=/loe6T66lScjfei7FciznaCg2lJ_F/000002.ts?e=1717162408&token=HUwgVvJnrW6fXOzqd_myfnE3FFoFLWJnNktg7ThD:8rkko6Hoco2oaXhZ-5KlhGNoG1Y
                # #EXT-X-KEY:METHOD=AES-128,URI="https://asyn.huke88.com/video/decrypt",IV=0xbb8cb03ab5465ec06cfeb78bb2f64a5e
                # #EXTINF:8.333333,
                # ......



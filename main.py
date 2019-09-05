# coding:utf-8

import urllib.request
from bs4 import BeautifulSoup
import csv
from time import sleep

ListId = []
finalListId = ['a1083a1ae81d45c0b76506f61d2bd46a', 'fd7e35339560456c9e9c663b28eceb39', '7a0ff0875348440b83879f68905d01ce', '5de05b37dc7e4f39bcf2a907367b6170', 'ff181ef5c0be4ae0a74564ea8c306740', 'ac3b925e176c4d039724bd40733a05aa', '46a0a495f93c44fbbaf6d8acd687d378', 'bf7e83aa93f343fdb19e5c0a5c570987', '47e12f0ea52348e58cb80373ca4321bc', 'da69bb32195240c4ac621301a910fdc9', 'b0bc4edaf7fc45c5bec6ada42a349242', '8cdb947b9ad44dec9aa9babfe7e6b68e', '1f738fdea925467fa2d42fdf1a776b01', 'e4e812c0576e469a9c7a88cde4922ce6', 'f93d60a940844b748827ae25e8083c02', 'f01d1ac861314e0fb6766ddecd71a50a', '6f3425ae2ec64799aef6351b9747b966', '098a5a33384a43099f2d9200ebc38e4b', '90b575b0ae4948f8a75a867feb794f34', '24263ec6bc164714b4507929f44f0ad1', 'f2f4f9ed237c4c5989d9ee7c0b426b9e', 'c90d8a101ea043659f8b12f16d80d0a5', '7cf6b7c12f2d4ff19a9440261622db4e', 'f5a54caeab534b72b548c7010ed6e108', '17c7da6b080049a3b2ce9724427147b6', 'c02043d26103479d95122ee0e85d161e', '4e700d6bc1104cee9f392cc191228d1a', '5e5818a4a4414155b912fed65e71d7e1', 'fb828a0c9e6243c88288e12299ca889c', '7080de8570d84c64aaa663994af84a0f', '557b9459d2cf43cda30a66aa37d98806', 'd567cf11bbae44babea6db804eca3788', '600688a69c7c4cb5967df87e51360d82', '9601cc4c49a64fb6a2c843235e1260c5', '19e9dc2b719f40058a5de72137badee3', '8ba44cc7266f470e86dfa392e76c3f42', '073d1eadd0af4f288ff048ad2df15641', '7b7798d2d4d5424f9f5d419e6c3a68b0', 'c02723a96abf4eee8aafa21135cb4ca6', '68d463db57524691afebda625f6a23ad', 'bbdc66dbc3fa4404bc349ef143417840', '0ec79368510b479a966316a55e42cf0e', '925ebffde1114f7da1560fbdb3aec5d4', 'd12b04d0330e49abaa5e2f3c91e2de5f', '0a1623b20a194266a0891a8ef0278297', 'fb8271078b5e42f3b2a92902730236ab', '17081afd44da43e48e436112e729a6e5', 'c830ab47cb4a4cbea13680e3ba193e98', '6e58873a9e4843f08fd893324b82325b', '36d659bb2a5443a3a845bf55ddd6c5bc', '8cdf8ea4f48e4abcb0c5b87d9a92dba8', 'd58fd3a83a3d429f811d3ea954358dca', 'a77b5cf43ff54eefa3b6191116512a58', '4eda14f24ac446b2a48869b364170896', 'd6d3dc407972406d886317f966cc5f59', 'bf5ba4a32f304afd88e26587f0186e65', 'fd61d769f837480cac70b99df4d4e5d8', 'c3599f32a67947778edf739edb4407d2', 'b1b2569f5fd946d1b7a753ee4e24e5a2', '7e57d2887be34f59aa9a4117f6434221', '6a7504c12f114d89ab95024e5ca27d56', '1952d09648d74f9fa41a7e91d28b0a02', '7d494d260ed846c6801cb3fbbc4613a7', 'a802aa40062642e490112e3d2928f662', '50426b76b8d2450faebb5aa54cd0450f', 'b9425f37367b44118e0700666ea74a3c', '22c2d89f69c84ac1801e5a545cca61b7', 'cedcbce62a0c4bf2a2b60e37fddca672', '6842ab54fdd944b68578c75fa03c8268', 'e9463669d1644da69070b5d7cb643684', '3cef9831ddb54481acfca572b7900d75', '5526b8db4b4c473ab679c20139d8c4bb', '9067460b95f8497f88728a2d6aed5ec7', '7a9d06d266264bea863452f0f2568b23', '3a2cf0363e5d44d98d46b75d5da2439e', 'd19035e5a24948539e1f7ec5e7cfb770', 'f602de9445eb4691a7529d35c7f7a9d6', '4ebc4270ddac4d859c9c9a30c77ab816', 'a354721c9542405086b1354211345370', '80aedfe404d84bf3a36afae9026a25c7', '821ef90932124ffeb066fd76cdeefced', '95aca3b615df44aea3b2cca725a72812', '629a9f01afed4d0eba8666772d88743a', '13152964b3f544fe879cb04f35c28c33', 'c58488c56d5a43c5a78fa2b71bf1eb2a', 'e6491e5dd2ee42a29243cf6c45b6a487', '940ac18bd46140e59e60b3c561d8eeff', '10f77ed38f314ca08bce904a374665fa', 'eaf1c4fc1bd44c0cabfd800fb3d5656a', '99a54ab1f468498c861b95ccfd8be11a', 'dae1a24014ba41559f5db2aefeb6d7c8', '8986032bff6a404d81283829095152dc', 'c5e88797ed3d464dba8f822cd626e9d6', '34f846ccd33341c2935bacf22a12d1f7', 'fb5dca1b92b345b68833ba77a23526b6', '8d21fa21394d4c39b6fce1ec7215a347', '996eee4bba034ccfa3f87e0aa98fd7fc', '11e75bf7ec78458f842bc71a5f3b8e37', 'a64c3106a4c749a7a54eefde45103f29', '21dd05662a734b359056012fdb699b6e', 'e93cdcad91be4cb6bde273ba9abe0ef6', '148c146701ab4264bc500b66a0dfdbca', '26894ec715324509915442b6f644a68e', '9d52a58169bf4056ae3e22b953b45c87', '40531cca05d74f678e2017afe9ce508c', '93c020278dc5479ab8115a5a08cb619a', 'e60b3cd656984bf789b9c53ffd8e5577', '9fa3aed0d24c492ea74bff936d47fa81', '6736002be7b847998e5f13bf7716e471', '6ec8e9ea23254ab289d1a9855972fcb1', 'fb7890e1ec1f4fdc80093ad865e07758', 'b1a596f361f2499da05dfd1bfb38c6e0', '43170720c24e468fbd0d5479a1bfcc18', '730ad1b6efe941d288c36251ac0bb79e', '58345a895e8e4b09bd6f9136354ae207', '58d6b2229406448ea12c8a083470011a', '7b2f7fea8706420e85b7412067701f64', '225247b7286040679b59cb71f385f498', '2a406197072a4118a201292e662aba35', '6c187aef693d41e595a2f4131a462deb', '422583c6a3184e41ac96a8735d859a2f', '78c76ebde3da4df197bd917f5b25b04a', 'c3182568f07a432ead4576c1b0a911b1', '3cdc5b22ecfc43b3b876999aed274d1a', '52c2c4fbdad24220b23f88adc7e63d98', '4d3ef1d462f2462d990a1e8940325d66', 'eb5e9e29f3aa46bab93c8c967d598f1e', 'ac5365550be54469b02e27bf613c1e1b', '37b68df2e2c54d35a595092925cf28f8', '9dfb000fe0354f7aaf8aaf2a157862cb', '2890312f5fec4028bfed53586d4ec510', '18b8ea2890624584a7588e9dbf036dc0', 'd2849b5b43a94229b27c84c2b54ee8fe', '0a9c841ee2b94c60b7e04c57514db28c', 'cabe09b2649945368fb09192c79053a0', '6d18d83a3a6248558bf7170685ea77d1', 'd6e1dc22782347e9bf259aee3711c668', '61e77ee22eec4ce18664a58da19e3643', '820bf76efc1b4767b6fdb333bf16ffa1', 'c6e17ed3b39e442787d0034ef6dafdf2', '5b2444dd51af42b59465e7a9e8e9fc72', '6c8fe0d5ca5a441886d9162e4bb000ab', 'f0937094c0c84d96a1b8a1dbdb40c462', '9dad0761107e447bb0ff8f33be003a0e', 'a08f15c0bab841f79580606f8dfe6e7e', 'c22513ced794411daaeb8695b691f714', 'cfa06270368c482787e641a4c1a61e8c', '063d79ce456f4a1b9957b56a15305df3', '94cddac91cda418b8efe0890ec0258dc', '625af31289a2489da569d5159d1484de', 'ea564097bd204df886eab92dcb245698', '0e3f64a2677b4d8da0596f0205586318', '120bf30b68c648808f2fd17546805fe6', 'c330aba9615244a9aad2d50b1aa7f2ad', '9edd726052714255b2cb6bff37ddb7bc', '242ebc8487a64da89918f2a65330928b', '3632fb1580d24326bec7af114b961f60', 'dd0ec872d3644e858fa90445f851f7fb', '4e3890229a7e4ea2ae21a48589966e3b', '4994a10bf0e24199a4eecbcf85fdf326', '48ef8602446b4b1c8467e494e2643fa7', '35415d40d1b446e3bad9136670afec7b', 'f98600e8d581475fb7214bb204ac7d1f', 'c1270be0601944539af9910efdc77c41', '5301fcbfa87048dbb947a7e89a03077f', 'a6741029709748da8b4c58a69374fc3f', '05e99be732da4e70b86342ce685a6368', '6be2d37fcd194f6085c49893058a538b', 'cbde1c6a91364e4980780179c82511ab', '31106ba8564b494294a9962e51f8c884', 'c11342f316a84d158f022c5d686f4aac', '922ecfcbcb5f400d89ace0b1fde3be8f', '99b1ce712fcb45498c467c6537dcea8c', 'efb576d1fbd54cb28511b94f4781cd7d', 'e4bc01b83e1841e58048124c43bb5e95', 'aa248f6eed1b44c1a33bfcace2497902', '6ffb27ab340240a6a0cb7186f8fc2849', '4b5b3d3c93a34ef7b375c0566ef31d9f', 'f084aef758b74a359d5427e2492f5c21', 'af6fe4f50ca04b7a9d9cbfaee575b3b8', 'ff2f5c56f69545b386f938ed161d1b41', '263d6d9d323e495fa0ba0a22fd25e3ba', 'a1424468f4da48a8b620a2c8e11392e2', 'f1e4020923d24755bad0a6ee94c2c290', 'f2654029d09040b28cb3993ead65d6df', '71d95ea2db024c82b3ea9d5d5afabf39', '94551620ebcb4769a21b0bdd5bce79c4', 'ab2bf488063e472b9a23d6601dadffa6', '55bce7db10e5456ab7222632912a9e40', '9d6a4ccd08c64a2787eba607c418117f', '75aba34e7b6c4d6280ca35a92e121026', 'e72046e9566d4767b09f1bf92df7b4a2', 'f2582efcef894c56b0313bdc4b2c27dd', '0a21c5c1134d4373aad4c90618dcbcab', 'b828953b2a2a4c859de35041eb817825', 'bd7af0d445c0485cbd39679137f59b04', '08570933b28e4a17b37b30486f4a66a7', '7ab9d797851a495689d4b62ef05303e4', '12ec0f56f9f948d1ad741893155bae15', '0e5d879b4a2c44608a00002642f379a3', '221a41fe74094fb584d5493879a23b2e', 'ab59f67495ff4934a49996961a6525d3', '46edaab23478416095ad4fd6f56833a7', '189dc01c102c435ba6e45004b286d33a', '5eb8d93df45445c2b8fea4ef0bc2765f', 'e16f3874abd647588e582b7fd44545bd', '54de00258c1240619fd1657d07507e08', '68eaf7b350dd4d14b9b0ce9d92ec542a', 'd91e5a038c6f4a019d86530e41959b85', 'c09e9a6c3d35468691016c6ed61c6a24', '5ae095cb609d47d6b650cd8dcae3f344', '444d6b0e515041e0a917f922ebe2abac', '46c1b38008ca4fbaa24693e3a40a6e08', '10153c3a23a24279949c41176f193384', '3b0f9c1d97bd4a3380bb24f115f5bc3f', 'b8d6cc34d1724ea58431be1519f6ea50', '7ee984863f724f1c9752166bda0d9856', '10e38591d2ab4c45b431a9ee5d149403', '249fd803aad5466784cb98e232684a1f', '1f66165d3cb446e8960f1d09b512c2b7', 'a8dd4d785cb64853a471cd5eed6a79c7', '9eeebccbbb6b4f7ebca5e923c9e3eba9', '89238177ee3e4889b240af2165201056']


def getId(pageNum):
    homeData = urllib.request.urlopen("http://syj.beijing.gov.cn/eportal/ui?pageId=331136&filter_LIKE_XKZH"
                                      "=&filter_LIKE_TITLE=&filter_EQ_FZJG=&currentPage=" + pageNum + "&pageSize=20")
    response = homeData.read()
    html = BeautifulSoup(response, 'html.parser')

    for i in html.select('td a[href]'):
        if "/eportal/ui?pageId=331623&exampleId=" in i['href']:
            ListId.append(i['href'][-32:])
    for x in ListId:
        if x not in finalListId:
            finalListId.append(x)


def getDetail():
    for i in finalListId:
        detailList = []
        detailData = urllib.request.urlopen(
            "http://syj.beijing.gov.cn/eportal/ui?pageId=331623&exampleId=" + i)
        response = detailData.read()
        html = BeautifulSoup(response, 'html.parser')
        for x in html.select('tbody tr td'):
            detailList.append(x.get_text())
        print(detailList)
        with open('bj.csv', 'a+', newline='', encoding="gbk") as f:
            f_csv = csv.writer(f, dialect='excel')
            try:
                f_csv.writerow([detailList[0], detailList[1], detailList[2], detailList[4], detailList[5], detailList[6],
                                detailList[7], detailList[8], detailList[11], detailList[12], detailList[13],
                                detailList[14],
                                detailList[15],
                                detailList[-10], detailList[-9], detailList[-7], detailList[-5], detailList[-3],
                                detailList[-2],
                                detailList[-1]])
            except:
                pass

        # sleep(1)


if __name__ == '__main__':
    csv_header = ['许可证号', '企业名称', '注册地址', '法定代表人', '企业负责人', '质量负责人', '分类码', '生产地址和范围',
                  '发证机关', '签发人', '发证日期', '有效期至', '状态说明', 'GMP信息-证书编号', '企业名称', '地址', '认证范围',
                  '发证机关', '发证日期', '有效期至']
    with open('bj.csv', 'a+', newline='', encoding='gbk')as f:
        f_csv = csv.writer(f, dialect='excel')
        f_csv.writerow(csv_header)
    # for i in range(1, 13):
    #     getId(str(i))
    #     sleep(1)
    # print(finalListId)
    # sleep(2)
    getDetail()
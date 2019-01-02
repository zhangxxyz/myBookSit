# 笔趣阁的书籍规则是1_1001 2_2001 11_11001 每个最大999
biqugeUrl = 'http://www.biquyun.com'


def getUrl():
    urlArray = []
    for i in range(1,2):
        for j in range(0,5):
            url = '{}/{}_{}{}'.format(biqugeUrl,'%d'%i,'%d'%i,getUrlSuffix(j))
            urlArray.append(url)

    return urlArray




def getBookInfo():
    print('666666666')
    pass


def getUrlSuffix(index):
    index = int(index)
    strs = ""
    if index < 10:
        strs = '{}{}'.format('00','%d'%index)
        return strs

    if index < 100:
        strs = '{}{}'.format('0', '%d' % index)
        return strs

    else:
        strs = str(index)
        return strs






# import js2py
# js = js2py.EvalJs()
# js.execute('var x="@length@challenge@reverse@false@window@a@document@catch@@pathname@18@@16@@toString@EY@@@1545578893@Array@firstChild@@@28@@A@B9P@Bby@substr@JgSe0upZ@function@@@@@charAt@8@while@M6V@replace@@__p@0xEDB88320@href@d@attachEvent@addEventListener@@cookie@@0xFF@https@@36@s@new@f@@1500@match@@split@Path@13@search@RegExp@@@@1@chars@@innerHTML@div@location@var@@else@l@@2@@charCodeAt@join@jX@as@setTimeout@eval@for@hantom@DOMContentLoaded@23@try@Sun@@createElement@@3@g@e@@D@@@791@@toLowerCase@fromCharCode@0@@onreadystatechange@@@parseInt@return@rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@@captcha@if@@String@__jsl_clearance@Dec@GMT@Expires@@".replace(/@*$/,"").split("@"),y="1k 2e=w(){1v('1j.J=1j.b+1j.19.F(/[\\?|&]25-3/,\\'\\')',13);8.O='29=k.1N|1R|'+(w(){1k 1b=[w(2e){22 2e},w(1b){22 1b},(w(){1k 2e=8.1E('1i');2e.1h='<7 J=\\'/\\'>1L</7>';2e=2e.m.J;1k 1b=2e.14(/R?:\\/\\//)[1R];2e=2e.u(1b.2).1P();22 w(1b){1x(1k 1L=1R;1L<1b.2;1L++){1b[1L]=2e.B(1b[1L])};22 1b.1s('')}})(),w(2e){22 1w('28.1Q('+2e+')')}],1L=['t',[(-~![]+((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])+(((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])],(!{}+[]+[[]][1R]).B(((+!+{})<<(+!+{}))),[[-~![]]+(((+!+{})<<(+!+{}))+[])],'s',[[-~![]]+(~~{}+[[]][1R])+(1p-~(+!+{})+((+!+{})+[1p]>>1p)+[]+[[]][1R])],'E',[6['H'+'1y'+'1u']+[]][1R].B(1p),'1t',[(-~![]+((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])],'U',[((-~{}<<(-~[]|((+!+{})<<(+!+{}))))+[]+[])+[1p+1p-~(+!+{})+((+!+{})+[1p]>>1p)]],'r',[(-~![]+((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])+(((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])],'1n',((-~{}<<(-~[]|((+!+{})<<(+!+{}))))+[]+[]),[(1p-~(+!+{})+((+!+{})+[1p]>>1p)+[]+[[]][1R])+(~~{}+[[]][1R]),(1p-~(+!+{})+((+!+{})+[1p]>>1p)+[]+[[]][1R])+(((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])],'h',[[-~[-~[]-~[]]]+(1p-~(+!+{})+((+!+{})+[1p]>>1p)+[]+[[]][1R])],[-~[-~[]-~[]]],'1K'];1x(1k 2e=1R;2e<1L.2;2e++){1L[2e]=1b[[1e,1G,1R,1p,1e,1G,1e,1R,1e,1p,1e,1G,1e,1G,1e,1R,1G,1e,1G,1R,1e][2e]](1L[2e])};22 1L.1s('')})()+';2c=1C, 1A-2a-c e:p:18 2b;17=/;'};26((w(){1B{22 !!6.M;}9(1I){22 5;}})()){8.M('1z',2e,5)}1m{8.L('1T',2e)}",f=function(x,y){var a=0,b=0,c=0;x=x.split("");y=y||99;while((a=x.shift())&&(b=a.charCodeAt(0)-77.5))c=(Math.abs(b)<13?(b+48.5):parseInt(a,36))+y*c;return c},z=f(y.match(/\w/g).sort(function(x,y){return f(x)-f(y)}).pop());while(z++)try{eval(y.replace(/\b\w+\b/g, function(y){return x[f(y,z)-1]||("_"+y)}));break}catch(_){};')
# # data = js2py.eval_js("@length@challenge@reverse@false@window@a@document@catch@@pathname@18@@16@@toString@EY@@@1545578893@Array@firstChild@@@28@@A@B9P@Bby@substr@JgSe0upZ@function@@@@@charAt@8@while@M6V@replace@@__p@0xEDB88320@href@d@attachEvent@addEventListener@@cookie@@0xFF@https@@36@s@new@f@@1500@match@@split@Path@13@search@RegExp@@@@1@chars@@innerHTML@div@location@var@@else@l@@2@@charCodeAt@join@jX@as@setTimeout@eval@for@hantom@DOMContentLoaded@23@try@Sun@@createElement@@3@g@e@@D@@@791@@toLowerCase@fromCharCode@0@@onreadystatechange@@@parseInt@return@rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@@captcha@if@@String@__jsl_clearance@Dec@GMT@Expires@@".replace(/@*$/,"").split("@"),y="1k 2e=w(){1v('1j.J=1j.b+1j.19.F(/[\\?|&]25-3/,\\'\\')',13);8.O='29=k.1N|1R|'+(w(){1k 1b=[w(2e){22 2e},w(1b){22 1b},(w(){1k 2e=8.1E('1i');2e.1h='<7 J=\\'/\\'>1L</7>';2e=2e.m.J;1k 1b=2e.14(/R?:\\/\\//)[1R];2e=2e.u(1b.2).1P();22 w(1b){1x(1k 1L=1R;1L<1b.2;1L++){1b[1L]=2e.B(1b[1L])};22 1b.1s('')}})(),w(2e){22 1w('28.1Q('+2e+')')}],1L=['t',[(-~![]+((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])+(((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])],(!{}+[]+[[]][1R]).B(((+!+{})<<(+!+{}))),[[-~![]]+(((+!+{})<<(+!+{}))+[])],'s',[[-~![]]+(~~{}+[[]][1R])+(1p-~(+!+{})+((+!+{})+[1p]>>1p)+[]+[[]][1R])],'E',[6['H'+'1y'+'1u']+[]][1R].B(1p),'1t',[(-~![]+((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])],'U',[((-~{}<<(-~[]|((+!+{})<<(+!+{}))))+[]+[])+[1p+1p-~(+!+{})+((+!+{})+[1p]>>1p)]],'r',[(-~![]+((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])+(((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])],'1n',((-~{}<<(-~[]|((+!+{})<<(+!+{}))))+[]+[]),[(1p-~(+!+{})+((+!+{})+[1p]>>1p)+[]+[[]][1R])+(~~{}+[[]][1R]),(1p-~(+!+{})+((+!+{})+[1p]>>1p)+[]+[[]][1R])+(((+!+{})+[~~{}])/[-~[]-~[]]+[[]][1R])],'h',[[-~[-~[]-~[]]]+(1p-~(+!+{})+((+!+{})+[1p]>>1p)+[]+[[]][1R])],[-~[-~[]-~[]]],'1K'];1x(1k 2e=1R;2e<1L.2;2e++){1L[2e]=1b[[1e,1G,1R,1p,1e,1G,1e,1R,1e,1p,1e,1G,1e,1G,1e,1R,1G,1e,1G,1R,1e][2e]](1L[2e])};22 1L.1s('')})()+';2c=1C, 1A-2a-c e:p:18 2b;17=/;'};26((w(){1B{22 !!6.M;}9(1I){22 5;}})()){8.M('1z',2e,5)}1m{8.L('1T',2e)}",f=function(x,y){var a=0,b=0,c=0;x=x.split("");y=y||99;while((a=x.shift())&&(b=a.charCodeAt(0)-77.5))c=(Math.abs(b)<13?(b+48.5):parseInt(a,36))+y*c;return c},z=f(y.match(/\w/g).sort(function(x,y){return f(x)-f(y)}).pop());while(z++)try{eval(y.replace(/\b\w+\b/g, function(y){return x[f(y,z)-1]||("_"+y)}));break}catch(_){})
# # print(data)
# print(js)
# print('你好')

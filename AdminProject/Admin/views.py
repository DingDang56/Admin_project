from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from Admin.models import *
import hashlib
import random

def setPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie = request.COOKIES.get("username")
        if cookie and request.session["username"]:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return inner

def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        admin=Admin()
        admin.username=username
        admin.password=setPassword(password)
        admin.save()
        return HttpResponseRedirect("/login/")
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        login_from = request.COOKIES.get('login_from')
        if login_from=="login_page":
            username=request.POST.get("username")
            password=request.POST.get("password")

            user=Admin.objects.filter(username=username).first()
            if user:
                form_password=setPassword(password)
                db_password=user.password
                if form_password==db_password:
                    response=HttpResponseRedirect("/index/")
                    response.set_cookie("username",user.username)
                    request.session["username"]=user.username
                    return response

    response=render(request,"login.html")
    response.set_cookie("login_from","login_page")
    return response

# Create your views here.
@loginValid
def index(request):
    return render(request,"base.html")

def logout(request):
    response=HttpResponseRedirect("/login/")
    response.delete_cookie("username")
    del request.session["username"]
    return response

# def students(request,page):
#     # 原生
#     page = int(page)
#     start = (page-1)*10
#     end = page*10
#     student_list=Student.objects.all()[start:end]
#     if page<4:
#         page_range = range(1,6)
#     else:
#         page_range=range(page-2,page+3)
#     return  render(request,"students.html",{"student_list":student_list,"page_range":page_range})

    #分页插件
# from django.core.paginator import Paginator
# def students(request,page):
#     student_list=Student.objects.all()
#     P=Paginator(student_list,10)#将student_list当中的数据按照每10条一页进行分页
#     page_data=P.page(page)#获取指定页的数据
#     #P.page_range()#页码的范围
#     #page_data.has_previous()#是否有前一页
#     #page_data.has_next()#是否有下一页
#     #page_data.number#当前页面
#     return render(request, "students.html", {"student_list":page_data,"P":P})
    #return render(request,"student.html",locals())
# def insertData(request):
#     pass
    # # subjects=[("python",20),("html",15),("mysql",5),("linux",5),("django",15),("flask",5),("小程序",2),("爬虫",15),("人工智能",15)]
    # # for sub,day in subjects:
    # #     s=Subject()
    # #     s.name=sub
    # #     s.date=day
    # #     s.save()
    #     #插入学员
    #     first_names=[
    # "俞",
    # "任",
    # "袁",
    # "柳",
    # "酆",
    # "鲍",
    # "史",
    # "唐",
    # "费",
    # "廉",
    # "岑",
    # "薛",
    # "雷",
    # "贺",
    # "倪",
    # "汤",
    # "滕",
    # "殷",
    # "罗",
    # "毕",
    # "郝",
    # "邬",
    # "安",
    # "常",
    # "乐",
    # "于",
    # "时",
    # "傅",
    # "皮",
    # "卞",
    # "齐",
    # "康",
    # "伍",
    # "余",
    # "元",
    # "卜",
    # "顾",
    # "孟",
    # "平",
    # "黄",
    # "和",
    # "穆",
    # "萧",
    # "尹",
    # "姚",
    # "邵",
    # "湛",
    # "汪",
    # "祁",
    # "毛",
    # "禹",
    # "狄",
    # "米",
    # "贝",
    # "明",
    # "臧",
    # "计",
    # "伏",
    # "成",
    # "戴",
    # "谈",
    # "宋",
    # "茅",
    # "庞",
    # "熊",
    # "纪",
    # "舒",
    # "屈",
    # "项",
    # "祝",
    # "董",
    # "梁",
    # "杜",
    # "阮",
    # "蓝",
    # "闵",
    # "席",
    # "季",
    # "麻",
    # "强",
    # "贾",
    # "路",
    # "娄",
    # "危",
    # "江",
    # "童",
    # "颜",
    # "郭",
    # "梅",
    # "盛",
    # "林",
    # "刁",
    # "钟",
    # "徐",
    # "邱",
    # "骆",
    # "高",
    # "夏",
    # "蔡",
    # "田",
    # "樊",
    # "胡",
    # "凌",
    # "霍",
    # "虞",
    # "万",
    # "支",
    # "柯",
    # "昝",
    # "管",
    # "卢",
    # "莫",
    # "经",
    # "房",
    # "裘",
    # "缪",
    # "干",
    # "解",
    # "应",
    # "宗",
    # "丁",
    # "宣",
    # "贲",
    # "邓",
    # "郁",
    # "单",
    # "杭",
    # "洪",
    # "包",
    # "诸",
    # "左",
    # "石",
    # "崔",
    # "吉",
    # "钮",
    # "龚",
    # "程",
    # "嵇",
    # "邢",
    # "滑",
    # "裴",
    # "陆",
    # "荣",
    # "翁",
    # "荀",
    # "羊",
    # "於",
    # "惠",
    # "甄",
    # "曲",
    # "家",
    # "封",
    # "芮",
    # "羿",
    # "储",
    # "靳",
    # "汲",
    # "邴",
    # "糜",
    # "松",
    # "井",
    # "段",
    # "富",
    # "巫",
    # "乌",
    # "焦",
    # "巴",
    # "弓",
    # "牧",
    # "隗",
    # "山",
    # "谷",
    # "车",
    # "侯",
    # "宓",
    # "蓬",
    # "全",
    # "郗",
    # "班",
    # "仰",
    # "秋",
    # "仲",
    # "伊",
    # "宫",
    # "宁",
    # "仇",
    # "栾",
    # "暴",
    # "甘",
    # "钭",
    # "厉",
    # "戎",
    # "祖",
    # "武",
    # "符",
    # "刘",
    # "景",
    # "詹",
    # "束",
    # "龙",
    # "叶",
    # "幸",
    # "司",
    # "韶",
    # "郜",
    # "黎",
    # "蓟",
    # "薄",
    # "印",
    # "宿",
    # "白",
    # "怀",
    # "蒲",
    # "邰",
    # "从",
    # "鄂",
    # "索",
    # "咸",
    # "籍",
    # "赖",
    # "卓",
    # "蔺",
    # "屠",
    # "蒙",
    # "池",
    # "乔",
    # "阴",
    # "鬱",
    # "胥",
    # "能",
    # "苍",
    # "双",
    # "闻",
    # "莘",
    # "党",
    # "翟",
    # "谭",
    # "贡",
    # "劳",
    # "逄",
    # "姬",
    # "申",
    # "司马",
    # "上官",
    # "欧阳",
    # "夏侯",
    # "诸葛",
    # "东方",
    # "皇甫",
    # "尉迟",
    # "公羊",
    # "公冶",
    # "淳于",
    # "单于",
    # "公孙",
    # "仲孙",
    # "轩辕",
    # "令狐",
    # "宇文",
    # "长孙",
    # "慕容",
    # "司徒",
    # "司空",
    # "丌官",
    # "百里",
    # "东郭",
    # "南门",
    # "呼延",
    # "归海",
    # "左丘",
    # "东门",
    # "西门",
    #     ]
    #     last_names=[
    # "华君",
    # "子睿",
    # "宏君",
    # "旦宇",
    # "甫宇",
    # "英宇",
    # "霏功",
    # "君韬",
    # "功瑞",
    # "梓睿",
    # "希甫",
    # "泰圩",
    # "军舒",
    # "华益",
    # "荣曦",
    # "奕瑞",
    # "子桂",
    # "荣甫",
    # "欣宇",
    # "硕阳",
    # "君霖",
    # "金曦",
    # "泰智",
    # "锦甫",
    # "新杰",
    # "新臻",
    # "利韬",
    # "瑞曦",
    # "铠硕",
    # "锋纯",
    # "政祺",
    # "文曦",
    # "韬军",
    # "帅文",
    # "生瑞",
    # "子佳",
    # "锋睿",
    # "茂智",
    # "嵘华",
    # "慧祺",
    # "大铭",
    # "泉存",
    # "奕华",
    # "震纯",
    # "海豪",
    # "昌弘",
    # "继兴",
    # "首天",
    # "永睿",
    # "新明",
    # "海潇",
    # "宇泽",
    # "瑞浩",
    # "正舒",
    # "煜君",
    # "培睿",
    # "浩天",
    # "富铠",
    # "灏祺",
    # "新华",
    # "祥晔",
    # "梓存",
    # "英洁",
    # "英珂",
    # "硕雪",
    # "瑞键",
    # "虞锋",
    # "英凯",
    # "煜杰",
    # "希霏",
    # "枚永",
    # "茂宏",
    # "祥希",
    # "祺嵘",
    # "佳嵘",
    # "荣彤",
    # "春瑞",
    # "健晏",
    # "晖宝",
    # "瑞锋",
    # "华铠",
    # "健凯",
    # "宇政",
    # "弘凯",
    # "天壮",
    # "甫瑞",
    # "泰睿",
    # "希智",
    # "欣希",
    # "政鸿",
    # "佳铠",
    # "滨君",
    # "希曦",
    # "瑞文",
    # "青渭",
    # "嵘华",
    # "晔辉",
    # "春程",
    # "华嵘",
    # "铭洋",
    # "泓祺",
    # "新文",
    # "枚旦",
    # "瑞文",
    # "荣熙",
    # "荣华",
    # "宇森",
    # "宝森",
    # "金森",
    # "梓豪",
    # "梓宇",
    # "伟霖",
    # "傲蕾",
    # "炎彬",
    # "桐君",
    # "桐华",
    # "桑叶",
    # "桑林",
    # "桓文",
    # "桥山",
    # "梓榆",
    # "梦华",
    # "梵志",
    # "梓旬",
    # "棠华",
    # "森茂",
    # "森立",
    # "森荣",
    # "森秀",
    # "楚怀",
    # "楚风",
    # "楚天",
    # "楚云",
    # "蔚桐",
    # "楠风",
    # "楷宸",
    # "楚航",
    # "文彬",
    # "文森",
    # "越彬",
    # "烨霖",
    # "梓桐",
    # "曲桐",
    # "梓岩",
    # "松霖",
    # "枫林",
    # "木森",
    # "木犀",
    # "木樨",
    # "木槿",
    # "木棉",
    # "木莲",
    # "木香",
    # "林桥",
    # "木蓝",
    # "林立",
    # "林壑",
    # "林海",
    # "林樾",
    # "林涛",
    # "林箫",
    # "林衡",
    # "林森",
    # "林松",
    # "朴诚",
    # "朴淳",
    # "朴心",
    # "杉松",
    # "杏林",
    # "材德",
    # "材勇",
    # "材俊",
    # "材贤",
    # "林彬",
    # "烨霖",
    # "梓桐",
    # "曲桐",
    # "梓岩",
    # "蔚桐",
    # "梓旬",
    # "朴诚",
    # "朴淳",
    # "朴心",
    # "林棱",
    # "杉松",
    # "杏林",
    # "材德",
    # "材勇",
    # "材俊",
    # "材贤",
    # "松雨",
    # "松涛",
    # "松风",
    # "林柯",
    # "梓旬",
    # "梓宁",
    # "缙桐",
    # "栐培",
    # "梦翾",
    # "兆霖",
    # "松卿",
    # "柏维",
    # "楷博",
    # "信棠",
    # "胜榕",
    # "铭析",
    # "相淳",
    # "星权",
    # "彬凡",
    # "哲标",
    # "植威",
    # "檀奕",
    # "胤格",
    # "飞杰",
    # "思杰",
    # "楚轩",
    # "雪松",
    # "楷瑞",
    # "健柏",
    # "浩楠",
    # "林枫",
    # "荣轩",
    # "玉楠",
    # "梓铭",
    # "木棉",
    # "木莲",
    # "木香",
    # "木蓝",
    # "林立",
    # "林壑",
    # "林海",
    # "林樾",
    # "林涛",
    # "林棋",
    # "林箫",
    # "林衡",
    # "林森",
    # "林子",
    # "林濠",
    # "林冠",
    # "朴学",
    # "栋梁",
    # "栋宇",
    # "林楠",
    # "林子",
    # "林濠",
    # "林冠",
    # "朴学",
    # "栋梁",
    # "栋宇",
    # "树心",
    # "树声",
    # "树君",
    # "林桐",
    # "永继",
    # "思淇",
    # "宇洁",
    # "梓凯",
    # "政方",
    # "新嘉",
    # "安邦",
    # "安福",
    # "安歌",
    # "安国",
    # "安和",
    # "安康",
    # "安澜",
    # "安民",
    # "安宁",
    # "安平",
    # "安然",
    # "安顺",
    # "安翔",
    # "安晏",
    # "安宜",
    # "安怡",
    # "安易",
    # "安志",
    # "昂然",
    # "昂雄",
    # "博文",
    # "博学",
    # "博雅",
    # "博延",
    # "宾白",
    # "宾鸿",
    # "宾实",
    # "彬彬",
    # "彬炳",
    # "彬郁",
    # "斌斌",
    # "斌蔚",
    # "滨海",
    # "波光",
    # "波鸿",
    # "波峻",
    # "波涛",
    # "博瀚",
    # "博超"]
    #     for i in range(1000):
    #         name=random.choice(first_names)+random.choice(last_names)
    #         age=random.randint(18,25)
    #         gender = random.choice("男女")
    #         major = random.choice(["python","java","UI","web全栈","php","软件测试","Unity 3D","自媒体"])
    #         grade=random.randint(1,5)
    #
    #         st=Student()
    #         st.name=name
    #         st.age=age
    #         st.gender=gender
    #         st.major= major
    #         st.grade=grade
    #         st.save()
    #         for j in range(5):
    #             sub = random.choice(Subject.objects.all())
    #             st.subject.add(sub)
    #             st.save()
    #
    #     return HttpResponse("插入数据成功")
def students(request,page):
    page=int(page)#1
    start = (page-1)*10
    end = page * 10
    student_list = Student.objects.filter(delete_flag="false").order_by("id")[start:end]
    if page<4:
        page_range = range(1,6)
    else:
        page_range = range(page-2,page+3)
    return render(request,"students.html",locals())

def addStudent(request):
    subjects=Subject.objects.all()
    if request.method=="POST":
        data= request.POST
        name = data.get("name")
        age = data.get("age")
        gender = data.get("gender")
        major = data.get("major")
        grade = data.get("grade")
        img = request.FILES.get("photo")

        stu = Student()
        stu.name = name
        stu.age = age
        stu.gender = gender
        stu.major = major
        stu.grade = grade
        stu.photo=img
        stu.delete_flag = "false"
        stu.save()
        for id in data.get("sub"):
            id = int(id)
            sub = Subject.objects.get(id=id)
            stu.subject.add(sub)
            stu.save()
        return HttpResponseRedirect("/stu/1/")
    return render(request,"addStudent.html",locals())
#
def dismiss(request,id):
    url = request.META.get("HTTP_REFERER")#请求来自哪个路由REFERER
    stu = Student.objects.get(id = id)
    stu.delete_flag = "true"
    stu.save()
    #stu.delete()#物理删除
    return HttpResponseRedirect(url)
#
def updateStudent(request,id):
    subjecs = Subject.objects.all()
    stu = Student.objects.get(id = int(id))
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        age = data.get("age")
        gender = data.get("gender")
        major = data.get("major")
        grade = data.get("grade")

        stu.name=name
        stu.age = age
        stu.gender = gender
        stu.major = major
        stu.grade=grade
        stu.delete_flag='false'
        stu.save()
        # for id in data.get("sub"):
        #     id = int(id)
        #     sub = Subject.objects.get(id=id)
        #     stu.subject.add(sub)
        #     stu.save()
        # return HttpResponseRedirect("/student_list/1")
    return render(request,"updateStudent.html",locals())
#
def studentResource(request,id):
    stu = Student.objects.get(id = int(id))
    return render(request,"student_resource.html",locals())

def grade(request,count):
    stu=Student.objects.get(grade=int(count))
    return render(request,"gradex.html",locals())

def ajax_page(request):
    '''
    用来返回ajax页面
    '''
    return render(request,"ajax_file.html")

def ajax_data(request):
    '''
    用来处理ajax请求
    :param request:
    :return:
    '''
    result= {"data":"error"}
    if request.method=="POST":
        result["data"]="ok"
        img = request.FILES.get("imgage")
        ph = Student.objects.get(id=1000)
        ph.save()
        result["data"]="ok"
    return JsonResponse(result)

def echart(request):
    return render(request,"echart.html")
<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. DjangoUtil django的常用工具集</a>
<ul>
<li><a href="#sec-1-1">1.1. 安装</a></li>
<li><a href="#sec-1-2">1.2. django_utils</a></li>
<li><a href="#sec-1-3">1.3. mixin_utils</a></li>
</ul>
</li>
</ul>
</div>
</div>


# DjangoUtil django的常用工具集

## 安装

python setup.py install

## django\_utils

常用的工具集

    from dutils import django_utils

    # 超级用户装饰器
    require_superuser

    # 员工装饰器
    require_staff

    # 获取今天的时间
    get_today

    # 获取明天
    get_tomorrow

    # 获取后天
    get_after_tomorrow

    # 获取7天后
    after7day

    # 获取昨天
    get_yesterday

    # datetime to json encode
    DateTimeJSONEncoder

    # 返回Json的HttpResponse
    JsonResonse

    # 获取model的一个实例，如果找不到返回None
    get_object_or_none

    # 获取整数
    get_int

    # 将字符串转换成时间
    str2datetime

    # 获取浮点数
    get_float

    # 电话号码正则校验
    error_phone

    # 电子邮件正则校验
    error_email

    # 添加用户组
    user_add_group

    # 添加用户权限
    user_add_permission

    # FileField上传文件路径
    UploadFilepath

    # django的model转换成json
    django_model2json

    # 将一个url转换成带http的url
    get_http_url

## mixin\_utils

常用class base view的mixin

    from dutils import mixin_utils
    # 登陆
    LoginRequiredMixin

    # 去掉csrf校验
    CSRFExemptMixin

    # 员工登陆
    StaffRequiredMixin

    # 恶意IP限制
    MaliceMixin

    # 恶意组用户限制
    NotMaliceGroupUser

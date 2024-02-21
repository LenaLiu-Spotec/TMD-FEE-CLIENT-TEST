# 正确的登录账号与密码
login_success = [{"account": "lena.liu@spotec.net", "password": "abc123", "msg": "Lena.liu@spotec.net"}]

# 验证码登录成功
login_code_success = [{"account": "lena.liu@spotec.net", "msg": "Lena.liu@spotec.net"}]

# 登录账号错误或为空时
login_account_error = [
    {"account": "lena.liu@spotec.ne", "password": "abc123", "msg": "账号错误，请检查后再试"},
    {"account": "", "password": "abc123", "msg": "手机号/邮箱不能为空"}
]

# 密码错误或为空时
login_password_error = [
    {"account": "lena-test105@1.com", "password": "abc1234", "msg": "登录失败，请检查注册账号及登录密码"},
    {"account": "lena.liu@spotec.net", "password": "", "msg": "登录密码不能为空"}
]

# 验证码错误或为空时
login_code_error = [
    {"accoutn": "lena.liu@spotec.net", "code": "11111", "msg": "验证失败，请重试"},
    {"accoutn": "lena.liu@spotec.net", "code": "", "msg": "验证码不能为空"}
]

# 登录账号已拉入黑名单
login_invalid = [{"account": "lena-agent01@1.com", "password": "abc123", "msg": "未知错误R"}]

from overriding.base_value_error import BaseValueError



class CustomNotImplementedError(BaseValueError):
    message = "功能未实现"


class CustomServiceUnavailableError(BaseValueError):
    message = "服务暂时不可用"


class CustomInvalidParamError(BaseValueError):
    message = "参数无效"


class CustomMissingParamError(BaseValueError):
    message = "缺失参数"


class CustomForbiddenError(BaseValueError):
    message = "没有权限访问资源"


class CustomNotFoundError(BaseValueError):
    message = "资源不存在"


class CustomMethodNotAllowedError(BaseValueError):
    message = "方法不被允许"


class CustomNotAcceptableError(BaseValueError):
    message = "不支持的响应格式"


class CustomTooManyRequestsError(BaseValueError):
    message = "触发限流，调用太频繁"

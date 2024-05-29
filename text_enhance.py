# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus
import dashscope
import pandas as pd

# def sample_sync_call():
#     messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
#                 {'role': 'user', 'content': '介绍下故宫？'}]
#     resp = dashscope.Generation.call(
#         model='qwen-turbo',
#         messages=messages,
#         result_format='message',  # set the result to be "message" format.
#     )
#     # The response status_code is HTTPStatus.OK indicate success,
#     # otherwise indicate request is failed, you can get error code
#     # and message from code and message.
#     if resp.status_code == HTTPStatus.OK:
#         print(resp.output)  # The output text
#         print(resp.usage)  # The usage information
#     else:
#         print(resp.code)  # The error code.
#         print(resp.message)  # The error message.
#
#
# sample_sync_call()

#文本增强函数
def enhance_text(text):
    #设置脚本自动提问，要求只输出处理后的结果
    request = "Please text enhance the following text, only output the enhanced text do not lick any new content, do not change the original language"+'\n'
    resp = dashscope.Generation.call(
        model='qwen-plus',
        prompt=request + text
    )
    if resp.status_code == HTTPStatus.OK:
        print(resp.output.text)
        print(resp.usage)
        return resp.output.text #如果能处理返回处理结果
    else:
        print(resp.code)
        print(resp.message)
        return text #如果不能处理返回原结果


def correct_text(text):
    request = "Please correct the errors in the following sentences, only output the corrected sentences, do not have any extra answers"+'\n'
    resp = dashscope.Generation.call(
        model='qwen-plus',
        prompt=request + text
    )
    if resp.status_code == HTTPStatus.OK:
        print(resp.output.text)  # The output text
        #print(resp.usage)  # The usage information
        return resp.output.text
    else:
        print(resp.code)  # The error code.
        print(resp.message)  # The error message.
        return text







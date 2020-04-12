# -*- coding: utf-8 -*-
import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。

from tencentcloud.ecc.v20181213 import ecc_client, models

from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    # cred = credential.Credential( "","")
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY")
    )

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "ecc.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
    httpProfile.keepAlive = True

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "HmacSHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile

    client = ecc_client.EccClient(cred, "", clientProfile)
    req = models.ECCRequest()
    req.Content = "this composition content"
    req.Grade = "grade7"
    req.Outline = ""
    req.ModelSubject = ""
    req.ModelContent = ""

    resp = client.ECC(req)

    # 输出json格式的字符串回包
    print("%s" % resp.to_json_string())

except TencentCloudSDKException as err:
    print("%s" % err)

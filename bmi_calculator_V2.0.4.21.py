# BMI计算器_V2.0.4.21
# 2025年5月30日最后修改
# BMI = 体重 / (身高 ** 2)

# Underweight (BMI < 18.5)
# Healthy Weight (BMI 18.5-24.9)
# Overweight (BMI 25-29.9)
# Obesity Class I (BMI 30-34.9)
# Obesity Class II+ (BMI ≥35)


import sys
import time

version = "2.0.4.21"
ver = "2.0.4"
updata_time = "2025/05/30"
developer = "SurinChi"


def countdown(t=15):
    """ 15s/自定义时间 程序自动关闭 """
    print()
    while  t != 0:
        print(f"\r程序将{t: 2d}秒后自动关闭。", end = "", flush = True)
        time.sleep(1)
        t = t - 1
    sys.exit()

def commonly_test(value, type):
    """ 通用验证函数 """
    print()
    try:
        value = float(value)
    except ValueError:
        print("（请输入一个数据，注意输入时不用带单位）")
        print("\n（请重新运行程序）")
        countdown()
    except Exception as e:
        print(f"\n（{e}）\n（发生未知错误，请尝试重新运行程序）")
        countdown()

    if value == 0:
        print(f"({type}不能为0哦，请手动关闭窗口或等待程序关闭后，再次启动并输入。)")
        countdown(7)
    elif value < 0:
        print(f"（{type}不能为负数，请重新运行程序）")
        countdown(7)



print(f"\n{'=' * 35}")
print(f"Version: {ver}")
print(f"Updata Time: {updata_time}")
print(f"{'-' * 35}")
print("欢迎使用BMI计算器！\n未经许可，禁止商用！")
print(f"{'=' * 35}\n")
print()

# 获取用户体重
user_weight = input("请输入你的体重（kg）：")

# 验证数据合理性
commonly_test(user_weight, "体重")

user_weight = float(user_weight)

#分类验证
if 0 < user_weight <= 35:
    print("（此处应输入体重，请重新运行程序）")
    countdown(7)
elif user_weight >= 165:
    print("（体重单位为千克，请重新运行程序）")
    countdown(7)

# 获取用户身高
user_height = input("请输入你的身高（m）：")

# 验证数据合理性

commonly_test(user_height, "身高")

user_height = float(user_height)
if  3 <= user_height <= 100 or user_height > 300:
    print("（此处应输入身高，请重新运行程序。）")
    countdown(7)
elif 100 < user_height <= 250:
    print(f"（检测到您输入的数据单位为cm）")
    print("\n（正在尝试将数据从“cm”转换为“m”）")
    try:
         user_height = round(user_height / 100, 2)
    except:
        print("（转换失败）\n（请重新运行程序）")
        countdown(7)
    print("\n（转换成功）")

# 开始计算BMI
bmi = round(user_weight / (user_height ** 2), 2)

# 判断BMI类型
if bmi < 18.5:
    category = "过轻"
elif 18.5 <= bmi <= 24.9:
    category = "正常"
elif 25 <= bmi <= 29.9:
    category = "超重"
elif 30 <= bmi <= 34.9:
    category = "肥胖Ⅰ级"
elif bmi >= 35:
    category = "肥胖Ⅱ级"
# 健康建议

advice_underweight = """
【潜在风险】营养不良、免疫力下降、骨质疏松、女性月经紊乱。

【建议】
〔营养强化〕增加高热量、高营养食物（如坚果、牛油果、全脂乳制品），少量多餐。
〔蛋白质摄入〕每日1.2-1.6g/kg体重（如鸡蛋、鱼肉、豆类）。
〔力量训练〕抗阻运动（如哑铃、弹力带）帮助增肌，避免仅依赖有氧运动。
〔医学排查〕检查甲亢、消化吸收障碍或进食障碍等潜在疾病。
"""
advice_heathy = """
【目标】维持健康状态，预防慢性病。

【建议】
〔均衡饮食〕遵循“膳食宝塔”，全谷物占主食1/3，每日蔬果500g以上。
〔运动习惯〕每周150分钟中等强度有氧（如快走、游泳）＋2次力量训练。
〔代谢指标监测〕即使BMI正常，仍需关注腰围（男性<85cm，女性<80cm）和体脂率（男性15-18%，女性20-25%）。
"""
advice_overweight = """
【潜在风险】高血压、糖尿病前期、脂肪肝风险升高。

【建议】
〔热量缺口〕每日减少300-500大卡，优先减精制糖和饱和脂肪（如甜品、油炸食品）。
〔饮食调整〕替换白米白面为杂粮，蛋白质选择瘦肉、鱼类（每周≥2次深海鱼）。
〔运动处方〕每周300分钟中高强度运动（如骑行、跳操），结合HIIT提升代谢。
〔行为干预〕记录饮食日记，识别情绪性进食诱因。
"""
advice_obesity_class_1 = """
【风险】心血管疾病、睡眠呼吸暂停、关节炎概率显著增加。

【建议】
〔医疗介入〕咨询营养科制定个性化方案，必要时考虑GLP-1受体激动剂等药物（需医生评估）。
〔低升糖指数（GI）饮食〕选择GI<55的食物（如燕麦、藜麦），控制血糖波动。
〔运动保护关节〕游泳、椭圆机等低冲击运动，避免跑步损伤膝盖。
〔睡眠与压力管理〕保证7小时睡眠（睡眠不足易刺激饥饿素分泌）。 
"""
advice_obesity_class_2_and_plus = """
【风险】2型糖尿病、严重心脑血管事件、预期寿命缩短。

【建议】
〔多学科团队支持〕联合内分泌科、康复科、心理科进行综合管理。
〔减重手术评估〕如BMI≥40或≥35合并并发症（如糖尿病），可考虑袖状胃切除术等。
〔渐进式目标〕先减重5-10%以显著改善代谢指标，再制定长期计划。
〔社会支持〕加入减重社群，家庭参与饮食环境调整。
"""

advice = {f"过轻":str(advice_underweight),
          "正常":str(advice_heathy),
          "超重":str(advice_overweight),
          "肥胖Ⅰ级":str(advice_obesity_class_1),
          "肥胖Ⅱ级":str(advice_obesity_class_2_and_plus),
          }

print(f"\n【BMI指数】{bmi}")
print(f"\n【健康状况】{category}")
print(f"{advice[category]}")
print("-- 以上建议由DeepSeek生成 --")
print()
countdown(120)
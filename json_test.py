import json

# 将Python对象转换为json对象
persons = [
    {
        'username':'苏勇智',
        'age':23,
        'country':'china'
    },
    {
        'username':'小明',
        'age':25,
        'country':'china'
    },
    {
        'username':'小张',
        'age':25,
        'country':'china'
    }
]
# json_str = json.dumps(persons)
# print(type(json_str))
# print(json_str)
# with open("result.json","a",encoding="utf-8") as f: # json格式保存到本地
#     # f.write(json_str)
#     json.dump(persons,f,ensure_ascii=False,indent=2)

json_str = '''[
  {
    "username": "苏勇智",
    "age": 23,
    "country": "china"
  },
  {
    "username": "小明",
    "age": 25,
    "country": "china"
  },
  {
    "username": "小张",
    "age": 25,
    "country": "china"
  }
]'''

# persons = json.loads(json_str)
# print(type(persons))
# print(persons)

with open("result.json","r",encoding="utf-8") as f:
    persons = json.load(f)
    print(type(persons))
    for person in persons:
        print(person)
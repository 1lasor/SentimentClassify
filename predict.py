import re
import random
from web_request import spider
#from text_enhance import enhance_text,correct_text
import pandas as pd
from sklearn.svm import NuSVC
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.model_selection import train_test_split#划分训练集和测试集
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline#用管道结合各种方法
from sklearn.metrics import accuracy_score, classification_report#准确度，评估报告
from sklearn.ensemble import RandomForestClassifier

#应用大模型文本增强范围
frac = 0.001
# 潜在停用词
potential_stop_words = [
    'of', 'been', 'could', 'we', 'i', 'have', 'a', 'it', 'she', 'prices', 'that', 'you', 'in', 'on', 'the', 'to',
    'were', 'this', 'with', 'should', 'at',
    'her', 'he', 'would', 'food', 'his', 'was', 'is', 'will', 'supermarket', 'and', 'had', 'for', 'has', 'they', 'are'
]

# 数据读取
train_csv_path = "sentiment_train.csv"
test_csv_path = "sentiment_test.csv"

train_data = pd.read_csv(train_csv_path)
test_data = pd.read_csv(test_csv_path)

# 数据预处理
def preprocess_text(text):
    # 全部转为小写
    text = text.lower()
    # 去除网址
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # 去除以'@'开头的字段
    text = re.sub(r'@\w+', '', text)
    #去除非字母空格感叹问号的其它符号
    text = ''.join([char for char in text if char.isalpha() or char.isspace() or char == '!' or char == '?'])
    return text


i=0
def enhance(text):
    global i
    i+=1
    print(i)
    request = "你是自然语言处理大师，请对下面的英文进行文本增强，只输出增强后的结果。"
    return spider(text+request)


#随机选择应用文本增强，可控时间
train_random_rows = train_data.sample(frac=frac, random_state=1)
train_data.loc[train_random_rows.index, 'ProcessedTweet'] = train_random_rows['OriginalTweet'].apply(enhance)
train_data['ProcessedTweet'].fillna(train_data['OriginalTweet'], inplace=True)

test_random_rows = test_data.sample(frac=frac, random_state=1)
test_data.loc[test_random_rows.index, 'ProcessedTweet'] = test_random_rows['OriginalTweet'].apply(enhance)
test_data['ProcessedTweet'].fillna(test_data['OriginalTweet'], inplace=True)

train_data['ProcessedTweet'] = train_data['ProcessedTweet'].apply(preprocess_text)
test_data['ProcessedTweet'] = test_data['ProcessedTweet'].apply(preprocess_text)


with open("ProcessedTweet",'w') as f:
    for ProcessedTweet in test_data['ProcessedTweet']:
        f.write(ProcessedTweet + '\n'+'\n')


# 交叉验证
X_train, X_val, y_train, y_val = train_test_split(
    train_data['ProcessedTweet'],
    train_data['Sentiment'],
    test_size=0.2
)

# 建立模型
model = make_pipeline(
    TfidfVectorizer(stop_words=potential_stop_words),
    #RandomForestClassifier()
    #MultinomialNB()
    NuSVC()
)

# 训练模型
model.fit(X_train, y_train)

# 评估模型
val_predictions = model.predict(X_val)
accuracy = accuracy_score(y_val, val_predictions)
classification_rep = classification_report(y_val, val_predictions)

# 预测
test_predictions = model.predict(test_data['ProcessedTweet'])
print(test_data.head())

# 写入数据
output_text_path = "pred.txt"
with open(output_text_path, 'w') as f:
    for sentiment in test_predictions:
        f.write(sentiment + '\n')

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_rep)

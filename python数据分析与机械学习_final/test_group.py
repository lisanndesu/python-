import pandas as pd

# 创建一个示例数据框
data = {
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Charlie'],
    'Age': [25, 30, 26, 35, 30, 35],
    'Score': [85, 90, 80, 95, 88, 92]
}
df = pd.DataFrame(data)

# 使用 groupby 方法按 Name 列分组，并计算每个组的 Score 的平均值
grouped = df.groupby(['Name', "Age"]).agg("mean")

print(grouped)
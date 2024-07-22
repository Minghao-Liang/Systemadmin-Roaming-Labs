import os

# 定义目录和文件名前缀  
directory = 'nonsense'
prefix = 'naming_is_hard'

# 创建一个空文件来保存合并后的消息 
with open('combined_message.txt', 'w') as f:  
    pass

# 打开combined_message.txt以追加内容   
with open('combined_message.txt', 'a') as combined_file:
    # 遍历00到18  
    for i in range(19):  # 包括0到18，共19个数字
        # 使用字符串格式化来创建文件名  
        filename = f"{prefix}{i:02d}"
        file_path = os.path.join(directory, filename)
          
        # 检查文件是否存在  
        if os.path.exists(file_path):
            # 读取文件内容并追加到combined_message.txt
            with open(file_path, 'r') as file:
                content = file.read()
                
                # 问题3开始
                # 请在下方填写你的代码
                
                # 问题3结束

                combined_file.write(content)
        else:
            print(f"Warning: File {file_path} does not exist.")
  
# 完成文件操作后，无需显式关闭文件，因为使用了with语句

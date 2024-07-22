printf '' > combined_message.txt  # 创建一个空文件来保存合并后的消息  
  
# 使用for循环来构建文件名，并添加前导零  
for i in {0..18}; do  
    # 问题1开始
    # 请在下方补全代码
    filename=
    # 问题1结束
    file="nonsense/$filename"  
  
    # 检查文件是否存在  
    if [ -f "$file" ]; then  
        # 问题2开始
        # 请在下方填写你的代码

        # 问题2结束 
    else  
        echo "Warning: File $file does not exist."  # 如果文件不存在，输出警告信息  
    fi  
done
#!/bin/bash

# 检查是否有文件作为参数传入
if [ "$#" -eq 0 ]; then
  echo "用法: $0 <文件1> [文件2] ..."
  echo "示例: $0 domain-direct.txt domain-adblock.txt"
  exit 1
fi

# 遍历所有传入的文件
for file in "$@"; do
  if [ -f "$file" ]; then
    echo "正在排序文件: $file"
    # 找出原始文件中的重复行
    duplicate_lines=$(sort "$file" | uniq -d)

    # 使用 sort -u 对文件内容进行排序并去重，然后写回原文件
    sort -u "$file" -o "$file"

    if [ -n "$duplicate_lines" ]; then
      echo "以下重复行已被删除:"
      echo "$duplicate_lines"
    else
      echo "没有发现重复行被删除。"
    fi

    echo "文件 $file 已排序并去重。"
  else
    echo "错误: 文件 $file 不存在或不是一个常规文件。"
  fi
done

echo "所有指定文件处理完毕。"

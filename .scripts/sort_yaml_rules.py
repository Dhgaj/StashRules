import sys
import yaml

def sort_yaml_rules(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        if 'payload' in data and isinstance(data['payload'], list):
            # 对 payload 列表进行排序并去重
            sorted_payload = sorted(list(set(data['payload'])))
            
            # 检查是否有任何更改
            if sorted_payload != data['payload']:
                data['payload'] = sorted_payload
                with open(file_path, 'w', encoding='utf-8') as f:
                    yaml.dump(data, f, allow_unicode=True, sort_keys=False)
                print(f"已排序并更新：{file_path}")
            else:
                print(f"无需更改：{file_path}")
        else:
            print(f"警告：在 {file_path} 中未找到 'payload' 键或其不是列表")

    except Exception as e:
        print(f"处理 {file_path} 时出错：{e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python sort_yaml_rules.py <file1.yaml> [<file2.yaml> ...]")
        sys.exit(1)

    for file in sys.argv[1:]:
        sort_yaml_rules(file)

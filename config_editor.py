import json


CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, 'r',encoding="utf-8") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, 'w',encoding="utf-8") as f:
        json.dump(config, f, indent=4)

def show_config(config):
    print("\n当前配置：")
    for key, value in config.items():
        print(f"{key}: {value}")
        
def update_config(config):
    show_config(config)
    key = input("\n请输入要修改的配置项（或按Enter跳过）：")
    if key in config:
        new_value = input(f"请输入新的值（当前值：{config[key]}）：")
        if key == "font_size":
            new_value = int(new_value)
            if new_value < 8 or new_value > 32:
                print("字体大小必须在8到32之间，跳过修改。")
                return                                      
        config[key] = new_value
        print(f"{key} 已更新为 {new_value}")
    else:
        print("配置项不存在，跳过修改。")

def main():
    config = load_config()
    while True:
        print("\n1. 查看配置\n2. 修改配置\n3. 退出")
        choice = input("请选择操作：")
        if choice == "1":
            show_config(config)
        elif choice == "2":
            update_config(config)
            save_config(config)
        elif choice == "3":
            break
        else:
            print("无效选择，请重新输入。")

main()

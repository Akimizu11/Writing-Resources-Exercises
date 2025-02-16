import os
import random
import datetime

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def get_random_file_from_directory(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return random.choice(files)

def generate_exercise():
    base_dir = r'C:\Users\秋水\OneDrive\我的文库\小说素材库'
    exercise_dir = 'C:\Users\秋水\OneDrive\我的文库\小说素材库\练习'
    os.makedirs(exercise_dir, exist_ok=True)
    
    categories = ['人物设定', '背景设定', '核心灵感', '特别话题', '情绪素材']
    
    selected_category = random.choice(categories)
    selected_file = get_random_file_from_directory(os.path.join(base_dir, selected_category))
    
    content = read_file(selected_file)
    
    exercise_content = f"# 练习题类别: {selected_category}\n\n"
    exercise_content += f"## 素材文件: {selected_file}\n\n"
    exercise_content += "### 题目内容:\n\n"
    exercise_content += content
    exercise_content += "\n\n### 写作区域:\n\n"
    exercise_content += "<请在此处开始你的写作>\n"
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    exercise_filename = os.path.join(exercise_dir, f"练习题_{timestamp}.md")
    
    with open(exercise_filename, 'w', encoding='utf-8') as file:
        file.write(exercise_content)
    
    print(f"练习题已生成: {exercise_filename}")

if __name__ == "__main__":
    generate_exercise()

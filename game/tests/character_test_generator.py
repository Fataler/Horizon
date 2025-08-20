import re
import os
import argparse

not_emotion_attributes = ['talk', 'right', 'left']
not_state_groups = ['pose', 'direction', 'emotion', 'mouth', 'effects']

def parse_layeredimage(layeredimage_string):
    """
    Парсит строку с определением layeredimage и извлекает состояния персонажа.

    Args:
        layeredimage_string (str): Строка, содержащая определение layeredimage.

    Returns:
        tuple: (имя_образа, словарь_состояний)
               Словарь состояний имеет вид: {'поза': ['эмоция1', 'эмоция2']}.
    """
    image_name_match = re.search(r'layeredimage\s+(\w+):', layeredimage_string)
    if not image_name_match:
        print("Error: Could not find layeredimage name.")
        return None, {}
    image_name = image_name_match.group(1)

    states = {}
    lines = layeredimage_string.strip().split('\n')
    
    current_group_name = None
    current_group_conditions = []
    
    attribute_re = re.compile(r'^\s+attribute\s+(\w+)')

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.startswith('group '):
            if_any_match = re.search(r'if_any\s+"([^"]+)"', stripped_line)
            if if_any_match:
                current_group_conditions = [c.strip() for c in if_any_match.group(1).split(',')]
            else:
                group_name_match = re.search(r'group\s+(\w+):', stripped_line)
                if group_name_match:
                    group_name = group_name_match.group(1)
                    if group_name not in not_state_groups:
                        states[group_name] = []
                        current_group_conditions = [group_name]
                    else:
                        current_group_conditions = []
        
        attr_match = attribute_re.match(line)
        if attr_match:
            attribute = attr_match.group(1)
            for condition in current_group_conditions:
                if condition not in states:
                    states[condition] = []
                if attribute not in not_emotion_attributes:
                    states[condition].append(attribute)

    return image_name, states


def generate_test_script(image_name, states, character_id=None, background="bg black"):
    """
    Генерирует тестовый Ren'Py скрипт.

    Args:
        image_name (str): Имя layeredimage (например, 'r_f').
        states (dict): Словарь состояний персонажа.
        character_id (str, optional): ID персонажа для диалога. Если None, используется image_name.
        background (str, optional): Фон для отображения теста.

    Returns:
        str: Содержимое сгенерированного .rpy файла.
    """
    if not character_id:
        character_id = image_name

    script_lines = [
        f'label test_{image_name}_states:',
        f'    "Тестирование всех состояний персонажа {character_id}"',
        '',
        f'    scene {background}',
        '',
        '    window show',
        ''
    ]

    sorted_poses = sorted(states.keys())
    for pose in sorted_poses:
        emotions = sorted(states[pose])
        if not emotions:
            script_lines.append(f'    show {image_name} {pose}')
            script_lines.append(f'    {character_id} "{pose}"')
            script_lines.append('')
        else:
            for emotion in emotions:
                script_lines.append(f'    show {image_name} {pose} {emotion}')
                script_lines.append(f'    {character_id} "{pose} {emotion}"')
                script_lines.append('')
    
    script_lines.append('    window hide')
    script_lines.append('    return')
    return '\n'.join(script_lines)

def main():
    parser = argparse.ArgumentParser(
        description="Генерирует тестовый .rpy скрипт для layeredimage персонажа.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-i', '--input', 
        required=True,
        help="Путь к файлу с определениями персонажей (например, characters.rpy)."
    )
    parser.add_argument(
        '-n', '--name', 
        required=True,
        help="Имя layeredimage для генерации теста (например, 'r_f')."
    )
    parser.add_argument(
        '-o', '--output',
        default='game/tests/auto_tests.rpy',
        help="Путь для сохранения сгенерированного файла.\nПо умолчанию: 'game/tests/auto_tests.rpy'"
    )
    parser.add_argument(
        '-c', '--char_id',
        help="ID персонажа для диалогов (например, 'r_f').\nЕсли не указан, используется имя layeredimage."
    )
    parser.add_argument(
        '-bg', '--background',
        default='black',
        help="Фон для теста (например, 'bg room_rayan' или 'black').\nПо умолчанию: 'black'."
    )
    
    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {args.input}")
        return

    layeredimage_regex = re.compile(
        r"layeredimage\s+" + re.escape(args.name) + r"\s*:\s*\n([\s\S]*?)(?=\n\w|#endregion|\Z)", 
        re.DOTALL
    )
    match = layeredimage_regex.search(content)

    if not match:
        print(f"Ошибка: Не удалось найти 'layeredimage {args.name}' в файле {args.input}")
        return
        
    layeredimage_def = f"layeredimage {args.name}:\n{match.group(1)}"

    image_name, states = parse_layeredimage(layeredimage_def)
    if not image_name:
        return

    test_script_content = generate_test_script(
        image_name, 
        states, 
        character_id=args.char_id or args.name,
        background=args.background
    )

    output_dir = os.path.dirname(args.output)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Создана директория: {output_dir}")

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(test_script_content)

    print(f"Тестовый скрипт успешно сгенерирован и сохранен в: {args.output}")


if __name__ == "__main__":
    main()

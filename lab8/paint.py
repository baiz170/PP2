import pygame
import random

pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Шрифт
font = pygame.font.Font(None, 36)

# Уровень (изначально 1)
level = 1

# Генерация числа уровня (2n+1 цифр)
def generate_number(level):
    return "".join(str(random.randint(1, 9)) for _ in range(2 * level + 1))

# Функция для проверки выражения (без eval)
def calculate_expression(expression):
    try:
        # Заменяем "//" на "/" для правильной обработки
        expression = expression.replace("//", "/")
        
        # Проверяем корректность символов
        valid_chars = set("0123456789+-*/() ")
        if not all(char in valid_chars for char in expression):
            return None

        # Разбираем выражение
        numbers, operators = [], []
        num = ""
        
        for char in expression:
            if char.isdigit():
                num += char
            else:
                if num:
                    numbers.append(int(num))
                    num = ""
                if char in "+-*/()":
                    operators.append(char)
        
        if num:
            numbers.append(int(num))

        # Проверяем деление на 0 и остаток при делении
        if "/" in operators:
            for i in range(len(operators)):
                if operators[i] == "/" and numbers[i + 1] == 0:
                    return None
                if operators[i] == "/" and numbers[i] % numbers[i + 1] != 0:
                    return None

        # Выполняем вычисление
        result = numbers[0]
        for i in range(len(operators)):
            if operators[i] == "+":
                result += numbers[i + 1]
            elif operators[i] == "-":
                result -= numbers[i + 1]
            elif operators[i] == "*":
                result *= numbers[i + 1]
            elif operators[i] == "/":
                result //= numbers[i + 1]  # Целочисленное деление

        return result
    except:
        return None

# Создание элементов уровня (единожды)
def setup_level(level):
    global current_number, buttons, target_numbers
    current_number = generate_number(level)
    original_digits = list(current_number)

    # Целевые числа
    target_numbers = [[2, 5, 7], [11, 13, 17], [19, 23, 29],
                      [31, 37, 41], [43, 47, 53], [59, 61, 67],
                      [71, 73, 79], [83, 89, 97], [101, 103, 107]][level - 1]

    # Кнопки
    buttons = []
    button_x, button_y = 50, 250

    # Кнопки цифр (только доступные)
    for digit in sorted(set(original_digits)):
        rect = pygame.Rect(button_x, button_y, 50, 50)
        buttons.append((rect, digit))
        button_x += 60

    # Кнопки операций
    ops = ["+", "-", "*", "/", "(", ")"]
    button_x = 50
    button_y += 60
    for op in ops:
        rect = pygame.Rect(button_x, button_y, 50, 50)
        buttons.append((rect, op))
        button_x += 60

# Инициализация уровня
setup_level(level)

# Основной игровой цикл
running = True
while running:
    screen.fill(WHITE)

    # Отображение текущего числа
    text = font.render(f"Use digits: {current_number}", True, BLACK)
    screen.blit(text, (50, 50))

    # Отображение целевых чисел уровня
    target_text = font.render(f"Target: {target_numbers}", True, BLACK)
    screen.blit(target_text, (50, 100))

    # Отображение кнопок
    for rect, label in buttons:
        pygame.draw.rect(screen, GRAY, rect)
        text = font.render(label, True, BLACK)
        screen.blit(text, (rect.x + 15, rect.y + 10))

    # Обновление экрана
    pygame.display.flip()

pygame.quit()

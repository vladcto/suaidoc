---
department: 12
teacher: И. О. Фамилия
teacher_title: Степень
theme: Markdown в Pandoc
variant: 1
number: 0
discipline: Отчеты ГУАП
group: 0000
student: И. О. Фамилия
year: 2024
---

# Почему suaidoc?

## Возможности

## Как установить?

# Текст

## Параграфы

## Форматирование

# Заголовки

## Заголовок 2 уровня

### Заголовок 3 уровня

## Длинный заголовок - очень очень очень очень очень очень очень очень очень очень очень длинный заголовок

`<suaidoc-center>`


# Списки

## Обычный список

- Обычно здесь текст.
- $Можно\;использовать\;формулы\:\frac{1}{2}$.
- Также можно писать длинные списки. Здесь текст списка занимает несколько строчек.
- Можно использовать подсписки.
  - Подсписок 2 уровня.
    - Подсписок 3 уровня.
      - Подсписок 4 уровня. Cписки более глубоко уровня делать нельзя.
  - Можно начать текст с новой строки

    Вот так

## Нумерованный список

1. Обычно здесь текст.
2. $Можно\;использовать\;формулы\:\frac{1}{2}$.
3. Также можно писать длинные списки. Здесь текст списка занимает несколько строчек.
4. Можно начать текст с новой строки
  Можно начать текст с новой строки.

## Известные проблемы

**1. Нумерованный список не может иметь подсписки**

Это ограничение Markdown, нумерованных вложенных списков не существует в Markdown.

Можно использовать \LaTeX:

\begin{enumerate} 
  \item первый элемент первого уровня содержит список 
    \begin{enumerate} 
        \item элемент списка второго уровня
        \item второй элемент списка второго уровня
    \end{enumerate}
  \item  второй элемент первого уровня
\end{enumerate}

# Изображения

# Формулы

# Таблицы

# Код

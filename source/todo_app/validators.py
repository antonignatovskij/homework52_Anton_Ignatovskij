def validate_task(task):
    errors = {}
    print(task.description, task.date, task.detail_description)
    if not task.description:
        errors['description'] = 'Поле описания не должно быть пустым.'
    elif len(task.description) > 50:
        errors['description'] = 'Общая длина символов описания не должна превышать 50 символов.'
    if not task.date:
        errors['date'] = "Поле для Даты не должно быть пустым"
    if task.date != "":
        date = task.date
        date = date.split('-')
        if len(date) != 3:
            errors["date"] = "Вводите числа в формате YYYY-MM-DD"
        else:
            for dat in date:
                for d in dat:
                    try:
                        int(d)
                    except ValueError:
                        errors["date"] = "В вашей дате присутсвуют не числа"
    if task.detail_description:
        if len(task.detail_description) > 3000:
            errors["detail_description"] = "Общая длина символов детального описания не должна превышать 3000"
    return errors

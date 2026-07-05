class NewTaskValidator:
    @staticmethod
    def validate_new_task(new_task):
        flag = []
        if new_task['description'] == '':
            flag.append('Поле описания обязательно к заполнению')
        if new_task['date'] != '':
            date = new_task['date']
            if date != None:
                date = date.split('-')
                if len(date) != 3:
                    flag.append('Дата указана в неправильном формате')
                for d in date:
                    try:
                        d = int(d)
                    except:
                        flag.append('в ваших датах присутствуют не цифровые значения')
        if len(flag) == 0:
            return True
        return flag

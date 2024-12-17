from collections import defaultdict

class Document:
    def __init__(self, id, name, pages, section_id):
        self.id = id
        self.name = name
        self.pages = pages
        self.section_id = section_id

class Section:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class DocSection:
    def __init__(self, doc_id, section_id):
        self.doc_id = doc_id
        self.section_id = section_id

def one_to_many_mapping(documents, sections):
    result = [(doc.name, doc.pages, sec.name) for doc in documents for sec in sections if doc.section_id == sec.id]
    # Сортируем по названию отдела (третьему элементу кортежа)
    result.sort(key=lambda x: x[2])
    return result


def many_to_many_mapping(documents, sections, docs_sections):
    """м ко м"""
    section_dict = {s.id: s.name for s in sections}
    result = defaultdict(set)

    for ds in docs_sections:
        for doc in documents:
            if doc.id == ds.doc_id and ds.section_id in section_dict:
                result[section_dict[ds.section_id]].add(doc.name)

    return {key: list(value) for key, value in result.items()}

def task_a2(one_to_many, sections):
    """сум страниц"""
    totals = defaultdict(int)

    for _, pages, section in one_to_many:
        totals[section] += pages

    return sorted(totals.items(), key=lambda x: -x[1])

def task_a3(many_to_many, sections):
    """разделы с 'раздел'(для проверки м ко м поиск по разделу, а не по отделу, но и так и так работает правильно) и их документы"""
    result = {}
    for section, docs in many_to_many.items():
        if 'раздел' in section.lower():
            result[section] = docs
    return result

# if __name__ == '__main__':
#     sections = [
#         Section(1, 'Исторический раздел'),
#         Section(2, 'Научный отдел'),
#         Section(3, 'Литературный раздел'),
#         Section(4, 'Философский отдел'),
#         Section(5, 'Раздел математики'),
#     ]
#
#     documents = [
#         Document(1, 'История Древнего Мира', 300, 1),
#         Document(2, 'Квантовая механика', 250, 2),
#         Document(3, 'Сборник стихов Лермонтова', 200, 3),
#         Document(4, 'Метафизика Аристотеля', 150, 4),
#         Document(5, 'Геометрия Евклида', 350, 5),
#     ]
#
#     docs_sections = [
#         DocSection(1, 1),
#         DocSection(2, 2),
#         DocSection(3, 3),
#         DocSection(4, 4),
#         DocSection(5, 5),
#         DocSection(1, 3),
#         DocSection(2, 5),
#     ]
#
#     one_to_many = one_to_many_mapping(documents, sections)
#     print("One-to-Many Mapping:")
#     print(one_to_many)
#
#     result_task_a2 = task_a2(one_to_many, sections)
#     print("\nTask A2 Result:")
#     print(result_task_a2)
#
#     many_to_many = many_to_many_mapping(documents, sections, docs_sections)
#     result_task_a3 = task_a3(many_to_many, sections)
#     print("\nTask A3 Result:")
#     for key, value in result_task_a3.items():
#         print(f"{key}: {value}")

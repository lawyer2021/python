def thesaurus(*args):
    name_a = [idx.capitalize() for idx in args if idx.upper().startswith("А" or "а")]
    stuff = {args[:1]: name_a}
    name_i = [idx.capitalize() for idx in args if idx.upper().startswith("И" or "и")]
    stuff = {args[:1]: name_i}
    name_m = [idx.capitalize() for idx in args if idx.upper().startswith("М" or "м")]
    stuff = {args[:1]: name_m}
    name_p = [idx.capitalize() for idx in args if idx.upper().startswith("П" or "п")]
    stuff = {args[:1]: name_p}
    name_s = [idx.capitalize() for idx in args if idx.upper().startswith("С" or "с")]
    stuff = {args[:1]: name_s}
    stuff = {
        "А": name_a,
        "П": name_p,
        "М": name_m,
        "И": name_i,
        "C": name_s
    }
    print(stuff)


thesaurus("Иван", "Мария", "анна", "Игнат", "Семён", "Алексей", "Константин", "Станислав", "Петр", "Илья", "Святополк",
          "сергей")
import json

# ============================================================
# TREE 1: Марков Лазарь Тимофеевич root — the main tree
# ============================================================

# --- Branch: Александра Лазаревна Маркова & Федор Максимович Кашевский ---

konstantin_kash_st = {
    "name": "Константин Кашевский & Роза Ледовская",
    "attributes": {"Location": "Ставрополь"},
    "children": [
        {"name": "Дочь (имя не указано)", "attributes": {"Location": "Канада"}},
        {"name": "Дочь (имя не указано)"}
    ]
}

ekaterina_koroleva = {
    "name": "Екатерина Королёва",
    "attributes": {"Location": "Владимир"},
    "children": [{"name": "Сын (имя не указано)"}]
}

yulia_koroleva = {
    "name": "Юлия Королёва",
    "attributes": {"Location": "Москва"},
    "children": [{"name": "Сын (имя не указано)"}]
}

vyacheslav_korolev = {
    "name": "Вячеслав Королёв & Лариса",
    "attributes": {"Location": "Владимир"},
    "children": [ekaterina_koroleva]
}

yuri_korolev = {
    "name": "Юрий Королёв & Людмила",
    "attributes": {"Location": "Москва"},
    "children": [yulia_koroleva]
}

valentina_kash_korolev = {
    "name": "Валентина Кашевская & Анатолий Павлович Королёв",
    "attributes": {"Location": "Москва"},
    "children": [vyacheslav_korolev, yuri_korolev]
}

tatyana_lyakhova_krasnoyarsk = {
    "name": "Татьяна Ляхова",
    "attributes": {"Location": "Красноярск"}
}

nadezhda_lyakhova = {
    "name": "Надежда Ляхова",
    "attributes": {"Location": "Красноярск"},
    "children": [tatyana_lyakhova_krasnoyarsk]
}

gennady_lyakhov = {
    "name": "Геннадий Ляхов",
    "attributes": {"Location": "Ставроп. кр., Изобильное", "Dates": "1949–2011"}
}

olga_lyakhova = {"name": "Ольга Ляхова"}
sergei_lyakhov = {"name": "Сергей Ляхов"}

vladimir_lyakhov = {
    "name": "Владимир Ляхов",
    "attributes": {"Location": "Ставроп. кр., Изобильное"},
    "children": [olga_lyakhova, sergei_lyakhov]
}

vera_kash_lyakhov = {
    "name": "Вера Кашевская & Евгений Ляхов",
    "attributes": {"Location": "Ставроп. кр., Изобильное"},
    "children": [gennady_lyakhov, nadezhda_lyakhova, vladimir_lyakhov]
}

andrei_popov = {"name": "Андрей Попов"}
alexei_popov = {"name": "Алексей Попов"}

tatyana_popova = {
    "name": "Татьяна (Кашевская) & Владимир Попов",
    "attributes": {"Location": "Ставроп. кр., Изобильное"},
    "children": [andrei_popov, alexei_popov]
}

yuri_kash_horosh = {
    "name": "Юрий Кашевский & Людмила Хорошаева",
    "attributes": {"Location": "Хабаровск", "Dates": "Юрий: 1957–1996; Людмила: 1938 г.р."},
    "children": [tatyana_popova]
}

# children of Владимир Кашевский & Людмила
elizaveta_chestnykh = {"name": "Елизавета (?) Честных", "attributes": {"Location": "Москва"}}
chestnykh_unnamed = {"name": "Дочь/сын (имя не указано)", "attributes": {"Location": "Москва"}}

yulia_kash_chestnykh = {
    "name": "Юлия Кашевская & Дмитрий Честных",
    "attributes": {"Location": "Москва"},
    "children": [elizaveta_chestnykh, chestnykh_unnamed]
}

eva_gurikova = {"name": "Ева Гурикова", "attributes": {"Location": "Омск"}}

irina_kash_gurinov = {
    "name": "Ирина Кашевская & Игорь Гуринов",
    "attributes": {"Location": "Омск"},
    "children": [eva_gurikova]
}

konstantin_kash_ginyeva = {
    "name": "Константин Кашевский & Марина Гринёва",
    "attributes": {"Location": "Хабаровск", "Dates": "погиб в 2006 г."},
    "children": [yulia_kash_chestnykh, irina_kash_gurinov]
}

anna_romina = {
    "name": "Анна Ромина & Вячеслав Боровских",
    "attributes": {"Location": "Хабаровск", "Dates": "Анна: 1983 г.р.; Вячеслав: 1977 г.р."}
}

irina_kash_romin = {
    "name": "Ирина Кашевская & Андрей Ромин (?)",
    "attributes": {"Location": "Хабаровск", "Dates": "Ирина: 1960 г.р.; Андрей: 1961 г.р."},
    "children": [anna_romina]
}

tatyana_kash_1954 = {
    "name": "Татьяна Кашевская & Александр (?)",
    "attributes": {"Location": "Хабаровск", "Dates": "1954–1994"}
}

viktor_krumkin = {"name": "Виктор Крумкин", "attributes": {"Location": "Хабаровск"}}
evgeny_krumkin = {"name": "Евгений (?)", "attributes": {"Location": "Хабаровск"}}
kanashnikov_couple = {
    "name": "Дочь (имя не разборчиво) & Алексей Канашников",
    "attributes": {"Location": "Хабаровск", "Dates": "Алексей: 1976 г.р."}
}

olga_kash_krumkin = {
    "name": "Ольга Кашевская & Анатолий Крумкин",
    "attributes": {"Location": "Хабаровск"},
    "children": [kanashnikov_couple, evgeny_krumkin, viktor_krumkin]
}

vladimir_kash_ludmila = {
    "name": "Владимир Кашевский & Людмила",
    "attributes": {"Location": "Хабаровск"},
    "children": [konstantin_kash_ginyeva, irina_kash_romin, tatyana_kash_1954, olga_kash_krumkin]
}

alexandra_markova_kashevsky = {
    "name": "Александра Лазаревна Маркова & Фёдор Максимович Кашевский",
    "attributes": {"Location": "Хабаровск"},
    "children": [konstantin_kash_st, valentina_kash_korolev, vera_kash_lyakhov,
                 yuri_kash_horosh, vladimir_kash_ludmila]
}

# --- Branch: Михаил Лазаревич Марков & Надежда Ищенко ---

sergei_verikhov = {"name": "Сергей Верихов", "attributes": {"Location": "Биробиджан"}}
dmitry_verikhov = {"name": "Дмитрий Верихов", "attributes": {"Location": "Биробиджан"}}

tatyana_markova_verikhov = {
    "name": "Татьяна Маркова & (?) Верихов",
    "attributes": {"Location": "Биробиджан"},
    "children": [sergei_verikhov, dmitry_verikhov]
}

olga_markova = {
    "name": "Ольга Маркова",
    "attributes": {"Location": "Биробиджан"},
    "children": [{"name": "Сын (имя не указано)"}]
}

viktor_markov_lyubov = {
    "name": "Виктор Марков & Любовь",
    "attributes": {"Location": "Биробиджан"},
    "children": [olga_markova, tatyana_markova_verikhov]
}

konstantin_kositsyn = {
    "name": "Константин Косицын",
    "attributes": {"Location": "Биробиджан"},
    "children": [{"name": "Дочь (имя не указано)"}]
}

valentina_markova_kositsyn = {
    "name": "Валентина Маркова & Николай Косицын",
    "attributes": {"Location": "Биробиджан"},
    "children": [konstantin_kositsyn]
}

tamara_markova = {
    "name": "Тамара Маркова",
    "attributes": {"Location": "Биробиджан"}
}

mikhail_markov_ischenko = {
    "name": "Михаил Лазаревич Марков & Надежда Ищенко",
    "attributes": {"Location": "Биробиджан"},
    "children": [viktor_markov_lyubov, valentina_markova_kositsyn, tamara_markova]
}

# --- Branch: Юлия Лазаревна Маркова & (1) Пётр Мельников (2) Александр Важенов ---

evgenia_yudova = {"name": "Евгения Юдова", "attributes": {"Location": "Биробиджан", "Dates": "1996 г.р."}}

elena_romanenko_yudov = {
    "name": "Елена Романенко & Игорь Юдов",
    "attributes": {"Location": "Биробиджан", "Dates": "Елена: 1965 г.р.; Игорь: 1964 г.р."},
    "children": [evgenia_yudova]
}

lilia_melnikova = {
    "name": "Лилия Мельникова & Евгений Романенко / Николай Липатов",
    "attributes": {"Location": "Биробиджан", "Dates": "Лилия: 1942 г.р.; Евгений Романенко: 1938–1996; Николай Липатов: 1942 г.р."},
    "children": [elena_romanenko_yudov]
}

vladimir_pikalov_1999 = {"name": "Владимир Пикалов", "attributes": {"Location": "Биробиджан", "Dates": "1999 г.р."}}

alexander_pikalov = {
    "name": "Александр Пикалов & Анна",
    "attributes": {"Location": "Биробиджан", "Dates": "Александр: 1976 г.р."},
    "children": [vladimir_pikalov_1999]
}

elena_vazhenova_pikalov = {
    "name": "Елена Важенова & Владимир Пикалов",
    "attributes": {"Location": "Биробиджан", "Dates": "Елена: 1954 г.р.; Владимир: 1955 г.р."},
    "children": [alexander_pikalov]
}

andrei_vyalkov = {"name": "Андрей Вялков (?)", "attributes": {"Location": "Биробиджан"}}

konstantin_vazhenov_1996 = {
    "name": "Константин Важенов (?)",
    "attributes": {"Location": "Биробиджан", "Dates": "погиб в 1996 г."},
    "children": [andrei_vyalkov]
}

ivan_velkov = {"name": "Иван Велков", "attributes": {"Location": "Биробиджан"}}

irina_vazhenova_velkov = {
    "name": "Ирина Важенова & Андрей Велков",
    "attributes": {"Location": "Биробиджан", "Dates": "Ирина: 1958 г.р."},
    "children": [ivan_velkov]
}

vladimir_vazhenov_tsukanova = {
    "name": "Владимир Важенов & Надежда Цуканова",
    "attributes": {"Location": "Биробиджан", "Dates": "Владимир: 1952 г.р."},
    "children": [konstantin_vazhenov_1996, irina_vazhenova_velkov]
}

yulia_markova_melnikov_vazhenov = {
    "name": "Юлия Лазаревна Маркова & (1) Пётр Мельников (2) Александр Важенов",
    "attributes": {"Location": "Биробиджан", "Dates": "Юлия: 1918–2000; Пётр Мельников погиб в 1942 г."},
    "children": [lilia_melnikova, elena_vazhenova_pikalov, vladimir_vazhenov_tsukanova]
}

# --- Branch: Иван Лазаревич Марков & Капитолина (WWII casualty) ---

ivan_markov_kapitolina = {
    "name": "Иван Лазаревич Марков & Капитолина",
    "attributes": {"Location": "Биробиджан", "Dates": "Иван погиб во время ВОВ под Ленинградом"},
    "children": [
        {"name": "Сын (имя не указано)", "attributes": {"Location": "Владивосток"}},
        {"name": "Сын (имя не указано)", "attributes": {"Location": "Владивосток"}}
    ]
}

# --- Branch: Елена Лазаревна Маркова & Иван Васильевич Гриднев ---

sofia_glotova = {"name": "Софья Глотова"}
elena_glotova = {"name": "Елена Глотова"}

sergei_glotov_spirina = {
    "name": "Сергей Глотов & Лилия Спирина",
    "attributes": {"Location": "Париж (Дубай)"},
    "children": [sofia_glotova, elena_glotova]
}

irina_scherbakova = {"name": "Ирина Щербакова", "attributes": {"Location": "Калуга"}}

olga_glotova_scherbakov = {
    "name": "Ольга Глотова & Сергей Щербаков",
    "attributes": {"Location": "Калуга"},
    "children": [irina_scherbakova]
}

irina_gridneva_glotov = {
    "name": "Ирина Гриднева & Александр Глотов",
    "attributes": {"Location": "Алексин, Тульск. обл."},
    "children": [sergei_glotov_spirina, olga_glotova_scherbakov]
}

arina_gridneva = {"name": "Арина Гриднева", "attributes": {"Location": "Самара"}}

alexei_gridnev_emelyanova = {
    "name": "Алексей Гриднев & Елена Емельянова",
    "attributes": {"Location": "Самара"},
    "children": [arina_gridneva]
}

viktoria_gridneva = {"name": "Виктория Гриднева", "attributes": {"Location": "Самара"}}

vladimir_gridnev_chugunova = {
    "name": "Владимир Гриднев & Ольга Чугунова",
    "attributes": {"Location": "Самара"},
    "children": [viktoria_gridneva]
}

alexander_gridnev_tsvarina = {
    "name": "Александр Гриднев & Светлана Цварина (?)",
    "attributes": {"Location": "Самара"},
    "children": [alexei_gridnev_emelyanova, vladimir_gridnev_chugunova]
}

elena_markova_gridnev = {
    "name": "Елена Лазаревна Маркова & Иван Васильевич Гриднев",
    "attributes": {"Location": "Самара"},
    "children": [irina_gridneva_glotov, alexander_gridnev_tsvarina]
}

# --- Root of Tree 1 ---

tree1_root = {
    "name": "Марков Лазарь Тимофеевич (Моисеевич?) & Комогоруева Устинья",
    "attributes": {"Location": "Биробиджан"},
    "children": [
        alexandra_markova_kashevsky,
        mikhail_markov_ischenko,
        yulia_markova_melnikov_vazhenov,
        ivan_markov_kapitolina,
        elena_markova_gridnev
    ]
}

# ============================================================
# TREE 2: Гриднев Василий Степанович root (second, linked root)
# ============================================================

yuri_gordeev = {"name": "Юрий Гордеев", "attributes": {"Location": "Самара"}}
vladimir_gordeev = {"name": "Владимир Гордеев", "attributes": {"Location": "Самара"}}

valentina_polovinkina_gordeev = {
    "name": "Валентина Половинкина & Евгений Гордеев",
    "attributes": {"Location": "Самара"},
    "children": [yuri_gordeev, vladimir_gordeev]
}

ksenia_gridneva_polovinkin = {
    "name": "Ксения Васильевна Гриднева & Михаил Половинкин",
    "attributes": {"Location": "Самара"},
    "children": [valentina_polovinkina_gordeev]
}

ivan_gridnev_markova_ref = {
    "name": "Иван Васильевич Гриднев & Елена Лазаревна Маркова",
    "attributes": {"Location": "Самара", "Note": "Полное потомство этой пары показано в дереве Маркова Лазаря Тимофеевича выше"}
}

tree2_root = {
    "name": "Гриднев Василий Степанович & Юдакова Агафья Васильевна",
    "attributes": {"Location": "Самара, Богатовский р-н, с. Утростенка"},
    "children": [ivan_gridnev_markova_ref, ksenia_gridneva_polovinkin]
}

# ============================================================
# Combine and write
# ============================================================

forest = [tree1_root, tree2_root]

with open("genealogy_tree_temp.json", "w", encoding="utf-8") as f:
    json.dump(forest, f, ensure_ascii=False, indent=2)

print("JSON written successfully.")

# quick validation + stats
def count_nodes(node):
    n = 1
    for c in node.get("children", []):
        n += count_nodes(c)
    return n

total = sum(count_nodes(t) for t in forest)
print(f"Total people recorded (with possible cross-link overlap): {total}")
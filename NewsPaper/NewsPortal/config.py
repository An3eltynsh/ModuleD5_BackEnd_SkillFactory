
article = 'A'
news = 'N'


CHOICE = [
    (article, 'Статья'),
    (news, 'Новость')
]

POSTS = {
    'post1':['Параметрические приемные антенны в задачах экологического мониторинга водной среды',

             """Высокая направленность приемных параметрических антенн с большой базой позволяет решить 
             задачу направленного приема на низких частотах в системах наблюдения за состоянием морской 
             среды. Применение относительно высоких частот накачки снижает габариты антенной системы. 
             Более того, использование приемных параметрических антенн в традиционных локаторах с широкой 
             характеристикой излучения на низких частотах в излучении позволяет повысить разрешающую 
             способность локатора по углу. Существенным при использовании приемной параметрической антенны 
             в локаторе является наличие излучающего преобразователя накачки со стороны прихода сигнала, 
             что конструктивно невозможно при транспортируемых системах. Поэтому рассмотрим возможность 
             использования приемных параметрических антенн локационного типа в гидроакустических системах, 
             предназначенных для обнаружения сигналов, пришедших с разных направлений в море.
             
             Локационная приемная параметрическая антенна на рассеянных волнах работает следующим образом. 
             Преобразователь накачки излучает в сторону предполагаемого направления прихода низкочастотного 
             сигнала волну накачки с частотой ю Поскольку частота накачки довольно высока, волна накачки от 
             объемных рассеива-телей среды распространяется в сторону приемного преобразователя накачки. 
             Волна накачки будет взаимодействовать с низкочастотными сигналами, пришедшими с некоторого 
             направления, вследствие нелинейности среды распространения. Результатом взаимодействия, как 
             это было показано ранее, будут волны с комбинационными частотами либо изменения фазы волны 
             накачки. Волна накачки совместно с волнами комбинационных частот, или промодулированная по 
             фазе сигналом, принимается приемным преобразователем накачки, расположенным в одной точке 
             пространства с излучающим преобразователем, причем приемным преобразователем накачки может 
             быть излучающий преобразователь накачки при работе антенны в импульсном режиме."""],

    'post2':['Излучающая акустическая параметрическая антенна для мониторинга приземного слоя атмосферы',

             """Рассматриваются вопросы нелинейного взаимодействия акустических волн в воздушной среде в 
             процессе распространения. Показывается, что коэффициент нелинейности в воздушной среде 
             значительно превышает таковой в воде, поэтому генерация вторичных волн в воздушной среде 
             эффективнее чем в воде. Рассчитываются основные характеристики взаимодействия. 
             Для реализации параметрической антенны для передачи информации узким лучом предлагается 
             использовать в качестве преобразователей в антенне накачки высокочастотные громкоговорители 
             с высокой чувствительностью в режиме излучения. Для уменьшения уровня боковых лепестков в 
             характеристике направленности антенны накачкидаются рекомендация по расположению 
             преобразователей в антенне накачки и согласованию их со средой с помощью акустических рупоров. 
             В качестве исходных параметров для расчетов выбираются паспортные данные громкоговорителей. 
             Анализируются характеристики параметрической антенны при расположении ее в воздушных потоках. 
             Взаимодействие волн в потоке описывается неоднородным волновым уравнением, в котором влияние 
             потока оценивается членом с конвективной производной.Рассмотрены неоднородные уравнения для 
             различных составляющих результирующего генерируемого сигнала параметрической антенной в среде 
             с воздушным потоком. Выведены выражения для расчета добавок к генерируемым в однородной среде 
             сигналам для перпендикулярного и параллельного направлению распространения волн потока. 
             Показано, что воздушный поток в ближней зоне антенны накачки увеличивает амплитуду генерируемых 
             нелинейным взаимодействием вторичных волн. Даются рекомендации по использованию параметрической 
             антенны для передачи информации в воздушной среде."""]
}

NEWS = {
    'news1':['Учёные обнаружили акулу с человеческими зубами',

             """Учёные обнаружили новый вид акул с человеческими зубами. 
             Как сообщил 11 августа журнал Diversity, они обитают на северо-восточном побережье Австралии. 
             Канберра, 11 августа, 2023, 16:00 — ИА Регнум. Учёные обнаружили новый вид акул с человеческими 
             зубами. Как сообщил 11 августа журнал Diversity, они обитают на северо-восточном побережье 
             Австралии.
             
             Diversity: в Австралии обнаружили новый вид акул с человеческими зубами. Новый вид получил 
             название Heterodontus marshallae (окрашенная рогатая акула). У таких акул два ряда зубов — 
             передний акулий, задний — с человеческими коренными.
             
             «Передние зубы заострённые, боковые относительно широкие, не очень удлиненные. Сдвиги зубов 
             присутствуют и характеризуют трансформацию зубных рядов от цепляющихся к перемалывающим», — 
             описано в статье. Отмечается, что такая особенность развития челюстей позволяет рогатым акулам 
             легко раскалывать ракообразных и моллюсков."""]
}

COMMENTS = {
    1: ['news1', 'Какой ужас!! Я больше никогда не поеду в Австралию!!!'],
    2: ['post1', """почему при такой конфигурации для ВЧ изменение фазы 
                как-то раньше наступает чем для НЧ"""],
    3: ['post1', """не сказал бы что эта модель достоверна, она будет 
                работать только в случае, если рассеянная волна распространяется 
                пучком."""],
    4: ['post1', 'Я ничего не понимать'],
    5: ['post2', 'эту статью надо добавить в раздел экологии'],
    6: ['post2', 'хотелось бы взгдянуть на приблеженное решение вашего волнового уровнения'],
}

screen_helper = """
AnchorLayout:
    anchor_x: 'left'
    anchor_y: 'top'
    
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: '                        OnBoard'
            
            opacity: 0
            id: top_bar
            md_bg_color: (255, 255, 255, 1)
            specific_text_color: (0, 0, 0, 1)
            
            
            right_action_items: [["dots-vertical", lambda x: lambda x: app.change_screen('home')]]
            elevation:8
        
        ScreenManager:
            
            id: manager
            Screen:
                name: 'auth'
                MDTextField:
                    id: login 
                    hint_text: "Логин"
                    helper_text: "Необходимое поле"
                    helper_text_mode: "on_focus"
                    icon_right: "account"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
                    size_hint_x:None
                    width:300
                MDTextField:
                    id: password
                    password: True
                    hint_text: "Пароль"
                    helper_text: "забыли пароль?"
                    icon_right: "textbox-password"
                    helper_text_mode: "on_focus"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x:None
                    width:300
                MDRectangleFlatButton:
                    text: 'Войти'
                    pos_hint:{'center_x': 0.5, 'center_y': 0.4}
                    on_release: app.login()
                   
            Screen:
                name: 'home'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: 50
                    BoxLayout:
                    
                        padding:35
                        orientation: 'vertical'
                        MDList:
                            MDLabel:         
                                text: 'Задачи на сегодня'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H5'
                                
                                text_color: (1, 1, 1, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]
                                        size: self.size[0], self.size[1] + 10
                                        pos: self.pos
                                size_hint: 1, None
                                height: 50
                                halign: 'center'
                            OneLineIconListItem:
                                text: 'Прохождение VR-задания'
                                bg_color: (55/255, 197/255, 219/255, 1)
                                IconLeftWidget:
                                    icon:'information-outline'
                                
                            OneLineIconListItem:
                                text: 'Общение с ментором'
                                bg_color: (55/255, 197/255, 219/255, 1)
                                
                                IconLeftWidget:
                                    icon:'information-outline'
                        MDList:
                            MDLabel:         
                                text: 'Расписание'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H5'
                                text_color: (1, 1, 1, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size
                                        pos: self.pos
                                size_hint: 1, None
                                height: 70
                            TwoLineIconListItem:
                                secondary_text: 'Практика в VR-лаборатории'
                                text: '11.30 - 12.00'
                                theme_text_color: 'Custom'
                                text_color: 1, 1, 1, 1
                                bg_color: (41/255, 160/255, 229/255,1)
                                height: 110
                                IconLeftWidget:
                                    icon:'clock-outline'
                            TwoLineIconListItem:
                                secondary_text: 'Обед'
                                theme_text_color: 'Custom'
                                text_color: 1, 1, 1, 1
                                text: '12.00 - 13.00'
                                height: 100
                                bg_color: (41/255, 160/255, 229/255,1)
                                height: 110
                                IconLeftWidget:
                                    icon:'clock-outline'
                            TwoLineIconListItem:
                                secondary_text: 'Общение с ментором'
                                text: '13.00 - 14.00'
                                theme_text_color: 'Custom'
                                text_color: 1, 1, 1, 1
                                bg_color: (41/255, 160/255, 229/255,1)
                                height: 100
                                height: 110
                                IconLeftWidget:
                                    icon:'clock-outline'
                            MDFlatButton:         
                                text: 'Прогресс недели:'
                                theme_text_color: "Custom"
                                text_color: 124/255, 124/255, 124/255, 1
                                italic: True
                                font_size: "18"
                                size_hint: None, None
                                halign: 'center'
                                on_press: manager.current = 'tasks'
                            ProgressBar:
                                max:100
                                
                                value: 76
            
                        GridLayout:
                            cols:2
                            row_force_default: True
                            row_default_height: 200    
                            GridLayout:
                                cols: 2
                                rows:2
                                MDIconButton:
                                    halign: "center"
                                    icon: "vk"
                                MDIconButton:
                                    halign: "center"
                                    icon: "instagram"
                                MDIconButton:
                                    halign: "center"
                                    icon: "twitter"
                                MDIconButton:
                                    halign: "center"
                                    icon: "facebook"
                            BoxLayout:
                                spacing: 10
                                orientation: 'vertical'
                                
                                MDRoundFlatButton:         
                                    text: 'Новости компании'
                                    theme_text_color: "Custom"
                                    text_color: 76/255, 19/255, 209/255, 1
                                    line_color: 0, 0, 0, 1
                                    
                                    size_hint: 1, 1
                                    halign: 'center'
                                MDRoundFlatButton:         
                                    text: 'Covid-19'
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: 55/255, 197/255, 219/255, 1
                                    font_size: "24"
                                    size_hint: 1, 1
                                    halign: 'center'
            Screen:
                name: 'messenger'
                BoxLayout:
                    spacing: 5
                    padding: 70
                    orientation: 'vertical'
                    BoxLayout:
                        MDLabel:         
                            text: ' Каналы'
                            theme_text_color: 'Custom'
                            halign: 'center'
                            font_style: 'H6'
                            text_color: (1, 1, 1, 1)
                            background_color: 0, 0, 0, 1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                RoundedRectangle:
                                    radius: [7]        
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                            height: 90
                        MDIconButton:
                            
                            icon: "plus-thick"
                    MDList:
                        
                        OneLineIconListItem:
                            
                            text: 'новости'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            bg_color: (124/255, 150/255, 190/255,1)
                            height: 110
                            IconLeftWidget:
                                icon:'wechat'
                        OneLineIconListItem:
                            
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            text: 'знакомства'
                            height: 100
                            bg_color: (100/255, 160/255, 229/255,1)
                            height: 110
                            IconLeftWidget:
                                icon:'wechat'
                        OneLineIconListItem:
                            
                            text: 'неделя_1'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            bg_color: (124/255, 150/255, 190/255,1)
                            height: 100
                            height: 110
                            IconLeftWidget:
                                icon:'wechat'
                        
                    MDList:
                        MDLabel:         
                            text: 'Личные сообщения'
                            theme_text_color: 'Custom'
                            halign: 'center'
                            font_style: 'H6'
                            text_color: (1, 1, 1, 1)
                            background_color: 0, 0, 0, 1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                RoundedRectangle:
                                    radius: [7]        
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                            height: 90
                        OneLineIconListItem:
                            
                            text: 'OnBoard_bot'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            bg_color: (124/255, 150/255, 190/255,1)
                            height: 110
                            IconLeftWidget:
                                icon:'qqchat'
                        OneLineIconListItem:
                            
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            text: 'Юлия (ментор)'
                            height: 100
                            bg_color: (100/255, 160/255, 229/255,1)
                            height: 110
                            IconLeftWidget:
                                icon:'chat'
                        OneLineIconListItem:
                            
                            text: 'Пригласить людей'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            bg_color: (124/255, 150/255, 190/255,1)
                            height: 100
                            height: 110
                            IconLeftWidget:
                                icon:'plus'
                        
                        
                        
               
            Screen:
                name: 'tasks'
                BoxLayout:
                    spacing: 5
                    padding: 10
                    orientation: 'vertical'
                
                    MDLabel:
                        text: 'Неделя 1'
                        theme_text_color: 'Custom'
                        halign: 'center'
                        font_style: 'H4'
                        text_color: (1, 1, 1, 1)
                        background_color: 9/255, 105/255, 161/255, 1
                        canvas.before:
                            Color:
                                rgba: self.background_color
                            RoundedRectangle:
                                radius: [7]        
                                size: self.size
                                pos: self.pos
                        size_hint: 1, None
                        height: 70
                    
                    MDList:
                        MDLabel:
                            text: 'Знакомство с рабочим местом'
                            theme_text_color: 'Custom'
                            halign: 'center'
                            font_style: 'H5'
                            text_color: (1, 1, 1, 1)
                            background_color: 9/255, 105/255, 161/255, 1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                RoundedRectangle:
                                    radius: [7]        
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                            height: 100
                            
                        TwoLineIconListItem:
                            
                            text: 'Видео'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            bg_color: (41/255, 160/255, 229/255,1)
                            height: 110
                            IconLeftWidget:
                                icon:'check'
                        TwoLineIconListItem:
                            secondary_text: 'Осталось 20 мин'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            text: 'Материалы для чтения'
                            height: 100
                            bg_color: (41/255, 160/255, 229/255,1)
                            height: 110
                            IconLeftWidget:
                                icon:'clock-outline'
                        TwoLineIconListItem:
                            secondary_text: 'Осталось 25 мин'
                            text: 'Другое'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            bg_color: (41/255, 160/255, 229/255,1)
                            height: 100
                            height: 110
                            IconLeftWidget:
                                icon:'clock-outline'
                        MDList:
                            MDLabel:
                                text: 'Обязательно:'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H5'
                                text_color: (1, 1, 1, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size
                                        pos: self.pos
                                size_hint: 1, None
                                height: 70
                                
                            TwoLineIconListItem:
                                secondary_text: 'Последняя оценка: 100%'
                                text: 'Тест "Техника безопасности"'
                                theme_text_color: 'Custom'
                                text_color: 1, 1, 1, 1
                                bg_color: (41/255, 160/255, 229/255,1)
                                height: 110
                                IconLeftWidget:
                                    icon:'check-circle'
                            TwoLineIconListItem:
                                secondary_text: 'Последняя оценка: 50%'
                                text: 'Тест "Тех процесс"'
                                theme_text_color: 'Custom'
                                text_color: 1, 1, 1, 1
                                
                                height: 100
                                bg_color: (41/255, 160/255, 229/255,1)
                                height: 110
                                IconLeftWidget:
                                    icon:'alert-circle'
                            TwoLineIconListItem:
                                secondary_text: ''
                                text: 'VR-практика'
                                theme_text_color: 'Custom'
                                text_color: 1, 1, 1, 1
                                bg_color: (41/255, 160/255, 229/255,1)
                                height: 100
                                height: 110
                                IconLeftWidget:
                                    icon:'sunglasses'
                    MDRoundFlatButton:         
                        text: 'Поставить оценку'
                        theme_text_color: "Custom"
                        text_color: 76/255, 19/255, 209/255, 1
                        line_color: 0, 0, 0, 1
                        halign: 'center'
                
            Screen:
                name: 'map'
                Image:
                    
                    source: 'map.jpeg'
                    
                    
                   
               
            Screen:
                name: 'profile'
                BoxLayout:
                    orientation: 'vertical'
                    padding: 30
                    
                    GridLayout:
                        
                        
                        cols: 2
                        FloatLayout:
                            canvas:
                                Color:
                                    rgb: 1, 1, 1
                                Ellipse:
                                    pos: 80, 800
                                    size: 230 , 231
                                    source: 'lapenko.jpeg'
                                    
                            
                        MDList:
                            OneLineListItem:
                            
                                text: 'Инженеров'
                                theme_text_color: 'Custom'
                                text_color: 1, 1, 1, 1
                                bg_color: 9/255, 105/255, 161/255, 1
                                height: 80
             
                            OneLineListItem:
                                text: 'Иван'
                                
                                theme_text_color: 'Custom'
                                text_color: 1, 1, 1, 1
                                bg_color: 9/255, 105/255, 161/255, 1
                                height: 80
                                
                            OneLineListItem:
                                text: 'Геннадьевич'
                                theme_text_color: 'Custom'
                                text_color: 1, 1, 1, 1
                                bg_color: 9/255, 105/255, 161/255, 1
                                height: 80
                    
                    MDList:
                        MDLabel:
                            text: '  АКМЭ-инжинириг, АО'
                            theme_text_color: 'Custom'
                            
                            font_style: 'Subtitle2'
                            text_color: (1, 1, 1, 1)
                            background_color: 41/255, 160/255, 229/255,1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                            height: 70
                        MDLabel:
                            text: '  Отдел: Заготовительный'
                            theme_text_color: 'Custom'
                            
                            font_style: 'Subtitle1'
                            text_color: (1, 1, 1, 1)
                            background_color: 41/255, 160/255, 229/255,1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                Rectangle:
                    
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                            height: 70
                        MDLabel:
                            text: '  Должность: Технолог'
                            theme_text_color: 'Custom'
                            
                            font_style: 'Subtitle2'
                            text_color: (1, 1, 1, 1)
                            background_color: 41/255, 160/255, 229/255,1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                Rectangle:
                    
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                            height: 70
                        MDLabel:
                            text: '  Контакты: +79726486137, evrika@mail.ru'
                            theme_text_color: 'Custom'
                            
                            font_style: 'Subtitle2'
                            text_color: (1, 1, 1, 1)
                            background_color: 41/255, 160/255, 229/255,1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                Rectangle:
                                
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                            height: 70
                        
                    BoxLayout:
                        orientation: 'vertical'
                        MDLabel:         
                            text: 'Общий прогресс адапатции:'
                            theme_text_color: 'Custom'
                            halign: 'center'
                            font_style: 'Subtitle2'
                            text_color: (1, 1, 1, 1)
                            background_color: 9/255, 105/255, 161/255, 1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                RoundedRectangle:
                                    radius: [7]        
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                            height: 70
                        ProgressBar:
                            max:100
                            value: 24
                            size_hint: 1, None
                            
                    MDList:
                        OneLineIconListItem:
                            
                            text: 'Мои бонусы: 24/100(7.500р)'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            bg_color: (41/255, 160/255, 229/255,1)
                            height: 110
                            IconLeftWidget:
                                icon:'sticker-plus'
                        TwoLineIconListItem:
                            secondary_text: '4 место'
                            text: 'Мой рейтинг в общем зачете:'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            
                            height: 100
                            bg_color: (41/255, 160/255, 229/255,1)
                            height: 110
                            IconLeftWidget:
                                icon:'account-multiple'
                        
                
                
        MDBottomNavigation:
            id: navigator
            size_hint: 1, None
            opacity: 0
            panel_color: 1, 1, 1, 1
            MDBottomNavigationItem:
                icon: 'home'
                on_tab_press: manager.current= "home"
            MDBottomNavigationItem:
                icon: 'message'
                on_tab_press: manager.current= "messenger"
            MDBottomNavigationItem:
                icon: 'file-document-box-check'
                on_tab_press: manager.current= "tasks"
            MDBottomNavigationItem:
                icon: 'map-marker'
                on_tab_press: manager.current= "map"
            MDBottomNavigationItem:
                icon: 'account-box'
                on_tab_press: manager.current= "profile"
    Image:
        id: atom
        source: 'atom.png'
        pos_hint: {'left': 1, 'top': 1}
        size_hint: None, None
        size: 130, 125
        opacity: 0            

            
"""

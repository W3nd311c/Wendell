import flet as ft 
import sqlite3

class ToDo:
    def __init__ (self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.BLUE
        self.page.window_width = 350
        self.page.window_height = 450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'Nave Maker '
        self.db_execute('CREATE TABLE IF NOT EXIST tasks(name, status)')
        self.main_page()
    def db_execute(self, query, params = []):
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur = execute(query, params)
            con.comit()
            return cur.fetchall()
            
    def tasks_conteiner(self):
        return ft.Container(
            height=self.page.height * 0.8,
            content = ft.Column(
                controls = [
                    ft.Checkbox(label='T1 ', value = True)
                ]
            )
        )
        
    def main_page(self):
        input_task = ft.TextField(hint_text = "Digite uma Tarefa", expand=True)
        
        input_bar = ft.Row(
            controls=[
                input_task,
                ft.FloatingActionButton(icon=ft.icons.ADD)
            ]
            
        )
        
        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text= "Jean"),
                ft.Tab(text="Wendell"),
                ft.Tab(text="William")
            ]
        )
        
        tasks = self.tasks_conteiner()
        self.page.add(input_bar, tabs, tasks)
ft.app(target = ToDo)
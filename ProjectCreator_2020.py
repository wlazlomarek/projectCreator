from appJar import gui
import os
import shutil
import sys
from string import punctuation

class MakeProject:
    def __init__(self):
        self.app = gui()
        self.template_folder_path = '/Volumes/terrablock/XXXX_PROJECT_TEMPLATE/'
        self.terrablock_path = '/Volumes/terrablock/'

    def network_connection(self):
        if os.path.exists(self.terrablock_path):
            return True
        else:
            return False

    def replace(self, text):
        polish_sign_dic = {
            'ą': 'a',
            'ć': 'c',
            'ę': 'e',
            'ł': 'l',
            'ń': 'n',
            'ó': 'o',
            'ś': 's',
            'ź': 'z',
            'ż': 'z',
            ' ': '_'
        }

        dictionary_charcters = {x: '_' for x in list(punctuation)}
        dictionary_charcters.update(polish_sign_dic)

        for el in text:
            for k, v in dictionary_charcters.items():
                if el == k:
                    text = text.replace(el, dictionary_charcters.get(k))

        return text.upper()

    def create_new_project(self, template_path, desination_path, project_name):
        try:
            shutil.copytree(template_path, desination_path + project_name, symlinks=False, ignore=None)
            self.app.infoBox('Success', f'Project {project_name} successfully created!')
        except Exception as error:
            self.app.errorBox('Error', f'{error}')

    def next_project_number(self, terrablock_path):

        project_list = os.listdir(terrablock_path)
        temp_list = [s.lstrip('0').split('_')[0] for s in project_list]

        for el in reversed(temp_list):
            try:
                int(el)
            except:
                temp_list.remove(el)
        next_number = int(max(temp_list)) + 1

        return f'0{str(next_number)}_'

    def prepare(self, app):
        app.setTitle("Milo Postproduction / Project Creator 2020")
        app.setSize("400x100")
        app.setResizable(canResize=False)
        app.setLocation("CENTER")
        app.setFont(size=12, family="Lato")
        app.setButtonFont(size=11, family="Lato")

        # Project Name Label
        app.startLabelFrame("  Input Project Name  ")
        app.setInPadding([90, 0])
        app.setPadding([10, 0])
        app.stretch = "both"
        app.sticky = "ew"
        app.addEntry("project_name", 0, 1, 2)
        app.stopLabelFrame()

        # Buttons
        app.addButtons(["Create Project"], self.press, 1, 0)
        app.enableEnter(self.press)

        if self.network_connection():
            app.setEntry("project_name", self.next_project_number(self.terrablock_path))
        else:
            app.errorBox("Error", "You don't have access to Terrablock!\nCheck connection!")
            sys.exit(0)

        return app

    def start(self):
        self.app = self.prepare(self.app)
        self.app.go()

    def press(self):
        project_name = self.app.getEntry("project_name")

        if self.next_project_number(self.terrablock_path) != project_name:
            project_name = self.replace(project_name)
            self.create_new_project(self.template_folder_path, self.terrablock_path, project_name)
            self.app.setEntry("project_name", self.next_project_number(self.terrablock_path))
        else:
            self.app.infoBox('Warrning', 'Enter name for a new project!')

            
if __name__ == '__main__':
    app = MakeProject()
    app.start()
    app.network_connection()

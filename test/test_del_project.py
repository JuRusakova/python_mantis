from model.project import Project
import random


def test_del_project(app):
    app.session.login("administrator", "root")
    old_project_list = app.project.get_project_list()
    if len(old_project_list) == 0:
        project = Project(name='name', description='description')
        app.project.create(project)
    project = random.choice(old_project_list)
    app.project.delete_project_by_name(project)
    new_project_list = app.project.get_project_list()
    old_project_list.remove(project)
    assert sorted(old_project_list, key=Project.sorting_name) == sorted(new_project_list, key=Project.sorting_name)
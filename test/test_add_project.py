from model.project import Project


def test_add_project(app):

    old_list = app.project.get_project_list()
    project = Project(name='name', description='disc')
    app.project.create(project)
    new_list = app.soap.get_project_list()
    old_list.append(project)
    assert sorted(old_list, key=Project.sorting_name) == sorted(new_list, key=Project.sorting_name)
from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    old_project_list = app.project.get_project_list()
    project = Project(name="new_project", description="description")
    app.project.create(project)
    new_project_list = app.project.get_project_list()
    old_project_list.append(project)
    assert sorted(old_project_list, key=Project.sorting_name) == sorted(new_project_list, key=Project.sorting_name)
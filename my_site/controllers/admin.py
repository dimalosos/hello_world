# Define the Blueprint for /admin

admin_blueprint = Blueprint(
    'admin',
    __name__,
    template_folder='templates'

# Admin functions

@admin_blueprint.route('/admin/edit', methods=['GET', 'POST'])
def edit_users():
    pass
    
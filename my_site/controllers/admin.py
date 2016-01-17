# Define the Blueprint for /admin

admin_blueprint = Blueprint(
    'admin',
    __name__,
    template_folder='templates'

# Admin functions

@admin_blueprint.route('/admin/delete/<int:id>', methods=['GET'])
def delete_user(id):
	user = User.query.get(id)
	if user:
		db.session.delete(user)
		db.session.commit()
	return redirect(url_for('show_users'))

    

@user_blueprint.route('/users/delete/<int:id>', methods=['GET'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('.show_users'))
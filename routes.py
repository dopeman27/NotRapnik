from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db
from models import User, Note
from forms import RegistrationForm, LoginForm

bp = Blueprint('main', __name__)

# --- AUTH ---
@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Email już istnieje.')
            return redirect(url_for('main.signup'))
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Konto utworzone – możesz się teraz zalogować.')
        return redirect(url_for('main.login'))
    return render_template('signup.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Nieprawidłowe dane.')
            return redirect(url_for('main.login'))
        login_user(user)
        return redirect(url_for('main.home'))
    return render_template('login.html', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

# --- NOTES ---
@bp.route('/')
@login_required
def home():
    notes = current_user.notes.order_by(Note.created_at.desc()).all()
    return render_template('home.html', notes=notes)

@bp.route('/api/notes', methods=['POST'])
@login_required
def api_create_note():
    note = Note(title="Bez tytułu", body="", author=current_user)
    db.session.add(note)
    db.session.commit()
    return jsonify({'id': note.id}), 201

@bp.route('/api/notes/<int:note_id>', methods=['PATCH'])
@login_required
def api_update_note(note_id):
    data = request.get_json() or {}
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        return jsonify({'error': 'Brak dostępu'}), 403
    if 'title' in data:
        note.title = data['title']
    if 'body' in data:
        note.body = data['body']
    db.session.commit()
    return jsonify({'status': 'ok'}), 200

@bp.route('/notes/<int:note_id>')
@login_required
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        flash('Brak dostępu.')
        return redirect(url_for('main.home'))
    return render_template('view_note.html', note=note)

@bp.route('/notes/<int:note_id>/delete', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.author == current_user:
        db.session.delete(note)
        db.session.commit()
    return redirect(url_for('main.home'))

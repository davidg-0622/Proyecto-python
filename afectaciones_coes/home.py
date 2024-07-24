from flask import Blueprint, render_template, request, redirect, url_for, flash, g
from .models import Registrar_afectacion, db
from datetime import datetime

bp = Blueprint('home', __name__)

@bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        tipo = request.form['tipo']
        numero_ticket = request.form['numero_ticket']
        descripcion = request.form['descripcion']
        fecha_inicio_afectacion = datetime.strptime(request.form['fecha_inicio_afectacion'], '%Y-%m-%d').date()
        hora = datetime.strptime(request.form['hora'], '%H:%M').time()
        id_usuario = g.user.id  # Obtener el ID del usuario logueado

        nueva_afectacion = Registrar_afectacion(
            tipo=tipo,
            numero_ticket=numero_ticket,
            descripcion=descripcion,
            fecha_inicio_afectacion=fecha_inicio_afectacion,
            hora=hora,
            id_usuario=id_usuario
        )

        try:
            db.session.add(nueva_afectacion)
            db.session.commit()
            flash('Afectación registrada con éxito', 'success')
            return redirect(url_for('home.registrar'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar la afectación: {str(e)}', 'danger')

    return render_template('index.html')

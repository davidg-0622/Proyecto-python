from flask import Blueprint, render_template, request, redirect, url_for, flash, g
from .models import Registrar_afectacion, Servicio, Agregar_servicio
from datetime import datetime
from . import db  # Asegúrate de importar db correctamente

bp = Blueprint('add_servicio', __name__)

@bp.route('/add_servicio', methods=['GET', 'POST'])
def add_servicio():
    selected_registro = None
    if request.method == 'POST':
        if 'numero_ticket' in request.form:
            numero_ticket = request.form.get('numero_ticket')
            selected_registro = Registrar_afectacion.query.filter_by(numero_ticket=numero_ticket).first()
        
        if 'servicio' in request.form:
            selected_servicio_id = request.form.get('servicio')
            if selected_servicio_id:
                flash(f'Servicio con ID {selected_servicio_id} seleccionado.', 'success')
                return redirect(url_for('add_servicio.add_servicio'))
            else:
                flash('Por favor selecciona un servicio.', 'danger')

    # Obtener todos los registros de la tabla Registrar_afectacion
    registros = Registrar_afectacion.query.all()
    # Obtener todos los servicios disponibles
    servicios = Servicio.query.all()

    return render_template('servicio/add_servicio.html', registros=registros, servicios=servicios, selected_registro=selected_registro)

@bp.route('/add_afectacion', methods=['GET', 'POST'])
def add_afectacion():
    if request.method == 'POST':
        try:
            estado = request.form['estado']
            servicio = request.form['servicio']
            tipo_afectacion = request.form['tipo_afectacion']
            hora_inicio_str = request.form.get('hora_inicio')
            hora_fin_str = request.form.get('hora_fin')

            # Manejo de hora_inicio
            if hora_inicio_str:
                hora_inicio = datetime.strptime(hora_inicio_str, '%H:%M').time()
            else:
                flash('La hora de inicio es requerida.', 'danger')
                return redirect(url_for('add_servicio.add_afectacion'))

            # Manejo de hora_fin (puede ser opcional)
            if hora_fin_str:
                hora_fin = datetime.strptime(hora_fin_str, '%H:%M').time()
            else:
                hora_fin = None  # Asigna None si no se proporciona la hora de fin

            id_usuario = g.user.id  # Obtener el ID del usuario logueado

            nueva_afectacion = Agregar_servicio(
                estado=estado,
                servicio=servicio,
                tipo_afectacion=tipo_afectacion,
                hora_inicio=hora_inicio,
                hora_fin=hora_fin
            )

            db.session.add(nueva_afectacion)
            db.session.commit()
            flash('Afectación registrada con éxito', 'success')
            return redirect(url_for('add_servicio.add_servicio'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar la afectación: {str(e)}', 'danger')

    return render_template('servicio/add_servicio.html')
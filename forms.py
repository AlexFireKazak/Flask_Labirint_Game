from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class GameForm(FlaskForm):
    way =SelectField(
        'Выберите сторону света, в которую желаете отправиться',
        coerce=int,
        choices=[(0, 'Север'),
                 (1, 'Восток'),
                 (2, 'Юг'),
                 (3, 'Запад')],
        render_kw={
            'class': 'form-control'
        }
    )
    number_steps = IntegerField(
        "Как далеко планируете продвинуться?",
        validators=[NumberRange(min=1), DataRequired()],
        default=1,
        render_kw={
            'class': 'form-control'
        }
    )

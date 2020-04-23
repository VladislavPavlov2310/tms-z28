from flask import Flask, redirect, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autoservice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Client(db.Model):
    client_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    automobiles = db.relationship('Automobile', backref=db.backref('client'))


class Automobile(db.Model):
    automobile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer)
    car_number = db.Column(db.String(20), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.client_id'))
    orders = db.relationship('Order', backref=db.backref('automobile'))


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(20), nullable=False)
    automobile_id = db.Column(db.Integer, db.ForeignKey('automobile.automobile_id'))
    issue_id = db.Column(db.Integer, db.ForeignKey('service.issue_id'))


class Service(db.Model):
    issue_id = db.Column(db.Integer, primary_key=True)
    issue = db.Column(db.String(255), nullable=False)
    fix_cost = db.Column(db.DECIMAL)
    detail_id = db.Column(db.Integer, db.ForeignKey('detail.detail_id'))
    orders = db.relationship('Order', backref=db.backref('service'))


class Detail(db.Model):
    detail_id = db.Column(db.Integer, primary_key=True)
    detail_name = db.Column(db.String(50), nullable=False)
    guarantee = db.Column(db.String(20), nullable=False)
    detail_cost = db.Column(db.DECIMAL, nullable=False)
    services = db.relationship('Service', backref=db.backref('detail'))


@app.route('/')
@app.route('/clients')
def clients():
    all_clients = Client.query.all()
    return render_template('clients.html', cl=all_clients)


@app.route('/automobiles')
def automobiles():
    all_automobiles = Automobile.query.all()
    return render_template('automobiles.html', au=all_automobiles)


@app.route('/orders')
def orders():
    all_orders = Order.query.all()
    return render_template('orders.html', ord=all_orders)


@app.route('/service')
def service():
    all_service = Service.query.all()
    return render_template('service.html', serv=all_service)


@app.route('/details')
def details():
    all_details = Detail.query.all()
    return render_template('details.html', dtl=all_details)


@app.route('/entity/<client_id>')
def entity(client_id):
    client = Client.query.filter_by(client_id=client_id).first_or_404()
    auto = Automobile.query.filter_by(client_id=client_id).all()
    return render_template('entity.html', client=client, automobile=auto)


@app.route('/delete/<client_id>')
def delete(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return redirect('/clients')


@app.route('/entity/edit/<ch><entity_id>', methods=['GET', 'POST'])
def edit(ch, entity_id):

    if ch == 'c':
        client = Client.query.get_or_404(entity_id)
        if request.method == 'POST':
            client.name = request.form['name']
            client.surname = request.form['surname']
            client.phone_number = request.form['number']
            db.session.commit()
            return redirect(f'/entity/{client.client_id}')
        else:
            return render_template('edit_form.html', client=client, ch=ch)
    else:
        automobile = Automobile.query.get_or_404(entity_id)
        if request.method == 'POST':
            automobile.brand = request.form['brand']
            automobile.model = request.form['model']
            automobile.year = request.form['year']
            automobile.car_number = request.form['car_number']
            db.session.commit()
            return redirect(f'/entity/{automobile.client_id}')
        else:
            return render_template('edit_form.html', auto=automobile, ch=ch)


if __name__ == '__main__':
    app.run(debug=True)

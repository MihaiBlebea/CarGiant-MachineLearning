import click

@click.command()
@click.option('--model', default='', help='The car\'s model')
@click.option('--body', prompt='Body type', help='The brand of the car.')
def predict_car(model, body):
    click.echo('Your selected car is ' + model + ' with ' + body + ' body type.')

if __name__ == '__main__':
    predict_car()

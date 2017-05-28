"""Main entry point for the demo generator"""

from demodata.scripts import patient as p
from demodata.scripts import facility as f
import click


@click.group()
@click.option('--output', default='STDOUT', help='location of output')
@click.pass_context
def cli(ctx, output):
    """Main entry point to the app"""
    ctx.obj = {'output': output}


@click.command()
@click.pass_context
@click.option('--count', default=1, help='number of patients')
def patients(ctx, count):
    """Generate patient data"""
    patient = p.generate_patients(count)
    sql = p.insert_patients(patient)

    # @todo Figure out a way to handle the --output option, probably a function called post_process()
    click.echo(sql)


@click.command()
@click.pass_context
@click.option('--count', default=1, help='number of facilities')
def facilities(ctx, count):
    """Generate faciliity data"""
    patient = f.generate_facility(count)
    # sql = p.insert_patients(patient)

    # @todo Figure out a way to handle the --output option, probably a function called post_process()
    click.echo(patient)


cli.add_command(patients)
cli.add_command(facilities)

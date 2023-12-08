import click
from spider.adafruit_servo_communication import Spider
from time import sleep
Arachnakiller = Spider()
@click.group()
def cmd_group():
    print('initializing...')
    sleep(.3)
    print('ready for commands')
    Arachnakiller = Spider()

@cmd_group.command()
@click.option(
        '-d',
        '--arr_deg',
        default = [90,180,90],
        help = 'input should be an array with 3 different angles for the 3 different servo motors',
        show_default=True, # show default in help
    )
def move_all_legs(arr_deg):
    Arachnakiller.move_all_legs(arr_deg)

@cmd_group.command()
@click.option(
        help = 'return all legs to their starting positions',
    )
def start_position():
    Arachnakiller.start_position()

@cmd_group.command()
@click.option(
        help = 'all middle motors will be reset to a starting position where they have no angles. [90,180,90]',
    )
def reset_servo_2():
    Arachnakiller.reset_pos()

@cmd_group.command()
@click.option(
        '-d',
        '--degree',
        default = 30,
        help = 'the degrees all legs will change their horizontal angles',
        show_default=True, # show default in help
    )
def change_legs(degree):
    Arachnakiller.change_all(degree)

@cmd_group.command()
@click.option(
        '-n',
        '--iterations',
        default = 1,
        help = 'amount of time you want to run the turn script',
        show_default=True, # show default in help
    )
def turn(iterations):
    Arachnakiller.turns(iterations)

if __name__ == "__main__":
    cmd_group()
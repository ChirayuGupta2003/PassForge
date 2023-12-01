import click
import string
import random
import pyperclip


@click.command()
@click.option("--length", default=16, help="Length of password (max=50).")
@click.option("--u", default=True, help="Include uppercase or not.")
@click.option("--l", default=True, help="Include lowercase or not.")
@click.option("--n", default=True, help="Include numbers or not.")
@click.option("--s", default=True, help="Include symbols or not.")
def hello(**kwargs):

    kwargs["length"] = min(kwargs["length"], 50)

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = r"""!@#$%^&*()-_+=[]{}|\;:'",./<>?`~"""

    result_string = ""

    if kwargs["u"]:
        result_string += uppercase

    if kwargs["l"]:
        result_string += lowercase

    if kwargs["n"]:
        result_string += numbers

    if kwargs["s"]:
        result_string += symbols

    password = ""

    for _ in range(kwargs["length"]):
        password += random.choice(result_string)

    pyperclip.copy(password)

    click.echo("Password copied to clipboard!")


if __name__ == "__main__":
    hello()

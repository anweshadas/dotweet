import sys
import twitter
import json
import click


@click.command()
@click.option("--tweet", "-t", is_flag=True, help="Does tweet.")
@click.option("--timeline", "-n", is_flag=True, help="Shows user's timeline.")
@click.option(
    "--directmessage", "-m", is_flag=True, help="Shows user's direct messages."
)
def main(tweet, timeline, directmessage):
    """This is an example script to do tweet and check status."""
    with open("config.json", "r") as fobj:
        data = fobj.read()
        config = json.loads(data)
        api = twitter.Api(
            consumer_key=config["consumer_key"],
            consumer_secret=config["consumer_secret"],
            access_token_key=config["access_token"],
            access_token_secret=config["access_token_secret"],
        )

    if tweet:
        s = input("What do you like to tweet? ")
        if len(s) > 280:
            click.echo("It crossed the word limit.")
            sys.exit(8)

        status = api.PostUpdate(s)
        click.echo(status.text)

    if timeline:
        timeline = api.GetUserTimeline()
        for t in timeline:
            click.echo(t.text)

    if directmessage:
        directmessage = api.GetDirectMessages()
        for m in directmessage:
            click.echo(m.text)


if __name__ == "__main__":
    main()

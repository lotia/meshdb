from invoke import task


@task
def format_check(context):
    context.run("uv run ruff format --check")


@task
def lint_check(context):
    context.run("uv run ruff check")


@task
def type_check(context):
    context.run("uv run mypy")


@task
def test(context):
    context.run("uv run pytest")


@task
def format(context):
    context.run("uv run ruff format")


@task
def all_check(context):
    format_check(context)
    lint_check(context)
    type_check(context)

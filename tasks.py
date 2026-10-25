from invoke import task


@task
def format(context):
    context.run("ruff format --check")


@task
def lint(context):
    context.run("ruff check")


@task
def typecheck(context):
    context.run("mypy")


@task
def typecheck_lint_format(context):
    typecheck(context)
    lint(context)
    format(context)


@task
def test(context):
    context.run("python src/manage.py test meshapi meshapi_hooks")

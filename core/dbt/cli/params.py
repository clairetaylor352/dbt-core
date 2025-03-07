from pathlib import Path, PurePath

import click
from dbt.cli.options import MultiOption
from dbt.cli.option_types import YAML, ChoiceTuple, WarnErrorOptionsType
from dbt.cli.resolvers import default_project_dir, default_profiles_dir
from dbt.version import get_version_information


args = click.option(
    "--args",
    envvar=None,
    help="Supply arguments to the macro. This dictionary will be mapped to the keyword arguments defined in the selected macro. This argument should be a YAML string, eg. '{my_variable: my_value}'",
    type=YAML(),
)

browser = click.option(
    "--browser/--no-browser",
    envvar=None,
    help="Wether or not to open a local web browser after starting the server",
    default=True,
)

cache_selected_only = click.option(
    "--cache-selected-only/--no-cache-selected-only",
    envvar="DBT_CACHE_SELECTED_ONLY",
    help="Pre cache database objects relevant to selected resource only.",
)

introspect = click.option(
    "--introspect/--no-introspect",
    envvar="DBT_INTROSPECT",
    help="Whether to scaffold introspective queries as part of compilation",
    default=True,
)

compile_docs = click.option(
    "--compile/--no-compile",
    envvar=None,
    help="Whether or not to run 'dbt compile' as part of docs generation",
    default=True,
)

compile_parse = click.option(
    "--compile/--no-compile",
    envvar=None,
    help="TODO: No help text currently available",
    default=True,
)

config_dir = click.option(
    "--config-dir",
    envvar=None,
    help="If specified, DBT will show path information for this project",
    type=click.STRING,
)

debug = click.option(
    "--debug/--no-debug",
    "-d/ ",
    envvar="DBT_DEBUG",
    help="Display debug logging during dbt execution. Useful for debugging and making bug reports.",
)

# TODO:  The env var and name (reflected in flags) are corrections!
# The original name was `DEFER_MODE` and used an env var called "DBT_DEFER_TO_STATE"
# Both of which break existing naming conventions.
# This will need to be fixed before use in the main codebase and communicated as a change to the community!
defer = click.option(
    "--defer/--no-defer",
    envvar="DBT_DEFER",
    help="If set, defer to the state variable for resolving unselected nodes.",
)

enable_legacy_logger = click.option(
    "--enable-legacy-logger/--no-enable-legacy-logger",
    envvar="DBT_ENABLE_LEGACY_LOGGER",
    hidden=True,
)

exclude = click.option(
    "--exclude", envvar=None, type=tuple, cls=MultiOption, help="Specify the nodes to exclude."
)

fail_fast = click.option(
    "--fail-fast/--no-fail-fast",
    "-x/ ",
    envvar="DBT_FAIL_FAST",
    help="Stop execution on first failure.",
)

favor_state = click.option(
    "--favor-state/--no-favor-state",
    envvar="DBT_FAVOR_STATE",
    help="If set, defer to the argument provided to the state flag for resolving unselected nodes, even if the node(s) exist as a database object in the current environment.",
)

full_refresh = click.option(
    "--full-refresh",
    "-f",
    envvar="DBT_FULL_REFRESH",
    help="If specified, dbt will drop incremental models and fully-recalculate the incremental table from the model definition.",
    is_flag=True,
)

indirect_selection = click.option(
    "--indirect-selection",
    envvar="DBT_INDIRECT_SELECTION",
    help="Select all tests that are adjacent to selected resources, even if they those resources have been explicitly selected.",
    type=click.Choice(["eager", "cautious", "buildable", "empty"], case_sensitive=False),
    default="eager",
)

log_cache_events = click.option(
    "--log-cache-events/--no-log-cache-events",
    help="Enable verbose adapter cache logging.",
    envvar="DBT_LOG_CACHE_EVENTS",
)

log_format = click.option(
    "--log-format",
    envvar="DBT_LOG_FORMAT",
    help="Specify the log format, overriding the command's default.",
    type=click.Choice(["text", "debug", "json", "default"], case_sensitive=False),
    default="default",
)

log_format_file = click.option(
    "--log-format-file",
    envvar="DBT_LOG_FORMAT_FILE",
    help="Specify the file log format, overriding the command's default and the value of --log-format.",
    type=click.Choice(["text", "debug", "json", "default"], case_sensitive=False),
    default="debug",
)

log_level = click.option(
    "--log-level",
    envvar="DBT_LOG_LEVEL",
    help="Specify the minimum severity of events that are logged.",
    type=click.Choice(["debug", "info", "warn", "error", "none"], case_sensitive=False),
    default="info",
)

log_level_file = click.option(
    "--log-level-file",
    envvar="DBT_LOG_LEVEL_FILE",
    help="Specify the minimum severity of events that are logged to file, overriding the value of --log-level-file.",
    type=click.Choice(["debug", "info", "warn", "error", "none"], case_sensitive=False),
    default="debug",
)

log_path = click.option(
    "--log-path",
    envvar="DBT_LOG_PATH",
    help="Configure the 'log-path'. Only applies this setting for the current run. Overrides the 'DBT_LOG_PATH' if it is set.",
    default=None,
    type=click.Path(resolve_path=True, path_type=Path),
)

macro_debugging = click.option(
    "--macro-debugging/--no-macro-debugging",
    envvar="DBT_MACRO_DEBUGGING",
    hidden=True,
)

output = click.option(
    "--output",
    envvar=None,
    help="TODO: No current help text",
    type=click.Choice(["json", "name", "path", "selector"], case_sensitive=False),
    default="selector",
)

output_keys = click.option(
    "--output-keys",
    envvar=None,
    help=(
        "Space-delimited listing of node properties to include as custom keys for JSON output "
        "(e.g. `--output json --output-keys name resource_type description`)"
    ),
    type=list,
    cls=MultiOption,
    default=[],
)

output_path = click.option(
    "--output",
    "-o",
    envvar=None,
    help="Specify the output path for the json report. By default, outputs to 'target/sources.json'",
    type=click.Path(file_okay=True, dir_okay=False, writable=True),
    default=PurePath.joinpath(Path.cwd(), "target/sources.json"),
)

parse_only = click.option(
    "--parse-only",
    envvar=None,
    help="TODO:  No help text currently available",
    is_flag=True,
)

partial_parse = click.option(
    "--partial-parse/--no-partial-parse",
    envvar="DBT_PARTIAL_PARSE",
    help="Allow for partial parsing by looking for and writing to a pickle file in the target directory. This overrides the user configuration file.",
    default=True,
)

port = click.option(
    "--port",
    envvar=None,
    help="Specify the port number for the docs server",
    default=8080,
    type=click.INT,
)

# envvar was previously named DBT_NO_PRINT
print = click.option(
    "--print/--no-print",
    envvar="DBT_PRINT",
    help="Output all {{ print() }} macro calls.",
    default=True,
)

deprecated_print = click.option(
    "--deprecated-print/--deprecated-no-print",
    envvar="DBT_NO_PRINT",
    help="Internal flag for deprecating old env var.",
    default=True,
    hidden=True,
    callback=lambda ctx, param, value: not value,
)

printer_width = click.option(
    "--printer-width",
    envvar="DBT_PRINTER_WIDTH",
    help="Sets the width of terminal output",
    type=click.INT,
    default=80,
)

profile = click.option(
    "--profile",
    envvar=None,
    help="Which profile to load. Overrides setting in dbt_project.yml.",
)

profiles_dir = click.option(
    "--profiles-dir",
    envvar="DBT_PROFILES_DIR",
    help="Which directory to look in for the profiles.yml file. If not set, dbt will look in the current working directory first, then HOME/.dbt/",
    default=default_profiles_dir,
    type=click.Path(exists=True),
)

# `dbt debug` uses this because it implements custom behaviour for non-existent profiles.yml directories
profiles_dir_exists_false = click.option(
    "--profiles-dir",
    envvar="DBT_PROFILES_DIR",
    help="Which directory to look in for the profiles.yml file. If not set, dbt will look in the current working directory first, then HOME/.dbt/",
    default=default_profiles_dir,
    type=click.Path(exists=False),
)

project_dir = click.option(
    "--project-dir",
    envvar="DBT_PROJECT_DIR",
    help="Which directory to look in for the dbt_project.yml file. Default is the current working directory and its parents.",
    default=default_project_dir,
    type=click.Path(exists=True),
)

quiet = click.option(
    "--quiet/--no-quiet",
    envvar="DBT_QUIET",
    help="Suppress all non-error logging to stdout. Does not affect {{ print() }} macro calls.",
)

record_timing_info = click.option(
    "--record-timing-info",
    "-r",
    envvar=None,
    help="When this option is passed, dbt will output low-level timing stats to the specified file. Example: `--record-timing-info output.profile`",
    type=click.Path(exists=False),
)

resource_type = click.option(
    "--resource-types",
    "--resource-type",
    envvar=None,
    help="TODO: No current help text",
    type=ChoiceTuple(
        [
            "metric",
            "source",
            "analysis",
            "model",
            "test",
            "exposure",
            "snapshot",
            "seed",
            "default",
            "all",
        ],
        case_sensitive=False,
    ),
    cls=MultiOption,
    default=(),
)

model_decls = ("-m", "--models", "--model")
select_decls = ("-s", "--select")
select_attrs = {
    "envvar": None,
    "help": "Specify the nodes to include.",
    "cls": MultiOption,
    "type": tuple,
}

inline = click.option("--inline", envvar=None, help="Pass SQL inline to dbt compile and preview")

# `--select` and `--models` are analogous for most commands except `dbt list` for legacy reasons.
# Most CLI arguments should use the combined `select` option that aliases `--models` to `--select`.
# However, if you need to split out these separators (like `dbt ls`), use the `models` and `raw_select` options instead.
# See https://github.com/dbt-labs/dbt-core/pull/6774#issuecomment-1408476095 for more info.
models = click.option(*model_decls, **select_attrs)
raw_select = click.option(*select_decls, **select_attrs)
select = click.option(*select_decls, *model_decls, **select_attrs)

selector = click.option(
    "--selector", envvar=None, help="The selector name to use, as defined in selectors.yml"
)

send_anonymous_usage_stats = click.option(
    "--send-anonymous-usage-stats/--no-send-anonymous-usage-stats",
    envvar="DBT_SEND_ANONYMOUS_USAGE_STATS",
    help="Send anonymous usage stats to dbt Labs.",
    default=True,
)

show = click.option(
    "--show", envvar=None, help="Show a sample of the loaded data in the terminal", is_flag=True
)

# TODO:  The env var is a correction!
# The original env var was `DBT_TEST_SINGLE_THREADED`.
# This broke the existing naming convention.
# This will need to be communicated as a change to the community!
#
# N.B. This flag is only used for testing, hence it's hidden from help text.
single_threaded = click.option(
    "--single-threaded/--no-single-threaded",
    envvar="DBT_SINGLE_THREADED",
    default=False,
    hidden=True,
)

skip_profile_setup = click.option(
    "--skip-profile-setup", "-s", envvar=None, help="Skip interactive profile setup.", is_flag=True
)

# TODO:  The env var and name (reflected in flags) are corrections!
# The original name was `ARTIFACT_STATE_PATH` and used the env var `DBT_ARTIFACT_STATE_PATH`.
# Both of which break existing naming conventions.
# This will need to be fixed before use in the main codebase and communicated as a change to the community!
state = click.option(
    "--state",
    envvar="DBT_STATE",
    help="If set, use the given directory as the source for json files to compare with this project.",
    type=click.Path(
        dir_okay=True,
        file_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
)

static_parser = click.option(
    "--static-parser/--no-static-parser",
    envvar="DBT_STATIC_PARSER",
    help="Use the static parser.",
    default=True,
)

store_failures = click.option(
    "--store-failures",
    envvar="DBT_STORE_FAILURES",
    help="Store test results (failing rows) in the database",
    is_flag=True,
)

target = click.option(
    "--target", "-t", envvar=None, help="Which target to load for the given profile"
)

target_path = click.option(
    "--target-path",
    envvar="DBT_TARGET_PATH",
    help="Configure the 'target-path'. Only applies this setting for the current run. Overrides the 'DBT_TARGET_PATH' if it is set.",
    type=click.Path(),
)

threads = click.option(
    "--threads",
    envvar=None,
    help="Specify number of threads to use while executing models. Overrides settings in profiles.yml.",
    default=None,
    type=click.INT,
)

use_colors = click.option(
    "--use-colors/--no-use-colors",
    envvar="DBT_USE_COLORS",
    help="Specify whether log output is colorized.",
    default=True,
)

use_colors_file = click.option(
    "--use-colors-file/--no-use-colors-file",
    envvar="DBT_USE_COLORS_FILE",
    help="Specify whether log file output is colorized overriding --use-colors/--no-use-colors.",
    default=True,
)

use_experimental_parser = click.option(
    "--use-experimental-parser/--no-use-experimental-parser",
    envvar="DBT_USE_EXPERIMENTAL_PARSER",
    help="Enable experimental parsing features.",
)

vars = click.option(
    "--vars",
    envvar=None,
    help="Supply variables to the project. This argument overrides variables defined in your dbt_project.yml file. This argument should be a YAML string, eg. '{my_variable: my_value}'",
    type=YAML(),
    default="{}",
)


# TODO: when legacy flags are deprecated use
# click.version_option instead of a callback
def _version_callback(ctx, _param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(get_version_information())
    ctx.exit()


version = click.option(
    "--version",
    callback=_version_callback,
    envvar=None,
    expose_value=False,
    help="Show version information",
    is_eager=True,
    is_flag=True,
)

version_check = click.option(
    "--version-check/--no-version-check",
    envvar="DBT_VERSION_CHECK",
    help="Ensure dbt's version matches the one specified in the dbt_project.yml file ('require-dbt-version')",
    default=True,
)

warn_error = click.option(
    "--warn-error",
    envvar="DBT_WARN_ERROR",
    help="If dbt would normally warn, instead raise an exception. Examples include --select that selects nothing, deprecations, configurations with no associated models, invalid test configurations, and missing sources/refs in tests.",
    default=None,
    is_flag=True,
)

warn_error_options = click.option(
    "--warn-error-options",
    envvar="DBT_WARN_ERROR_OPTIONS",
    default="{}",
    help="""If dbt would normally warn, instead raise an exception based on include/exclude configuration. Examples include --select that selects nothing, deprecations, configurations with no associated models, invalid test configurations,
    and missing sources/refs in tests. This argument should be a YAML string, with keys 'include' or 'exclude'. eg. '{"include": "all", "exclude": ["NoNodesForSelectionCriteria"]}'""",
    type=WarnErrorOptionsType(),
)

write_json = click.option(
    "--write-json/--no-write-json",
    envvar="DBT_WRITE_JSON",
    help="Writing the manifest and run_results.json files to disk",
    default=True,
)

write_manifest = click.option(
    "--write-manifest/--no-write-manifest",
    envvar=None,
    help="TODO: No help text currently available",
    default=True,
)

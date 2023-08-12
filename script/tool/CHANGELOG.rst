script/tool/CHANGELOG.md
========================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: md

    ## 0.13.4+1

* Makes `--packages-for-branch` detect any commit on `main` as being `main`,
  so that it works with pinned checkouts (e.g., on LUCI).

## 0.13.4

* Adds the ability to validate minimum supported Dart/Flutter versions in
  `pubspec-check`.

## 0.13.3

* Renames `podspecs` to `podspec-check`. The old name will continue to work.
* Adds validation of the Swift-in-Obj-C-projects workaround in the podspecs of
  iOS plugin implementations that use Swift.

## 0.13.2+1

* Replaces deprecated `flutter format` with `dart format` in `format`
  implementation.

## 0.13.2

* Falls back to other executables in PATH when `clang-format` does not run.

## 0.13.1

* Updates `version-check` to recognize Pigeon's platform test structure.
* Pins `package:git` dependency to `2.0.x` until `dart >=2.18.0` becomes our
  oldest legacy.
* Updates test mocks.

## 0.13.0

* Renames `all-plugins-app` to `create-all-packages-app` to clarify what it
  actually does. Also renames the project directory it creates from
  `all_plugins` to `all_packages`.

## 0.12.1

* Modifies `publish_check_command.dart` to do a `dart pub get` in all examples
  of the package being checked. Workaround for [dart-lang/pub#3618](https://github.com/dart-lang/pub/issues/3618).

## 0.12.0

* Changes the behavior of `--packages-for-branch` on main/master to run for
  packages changed in the last commit, rather than running for all packages.
  This allows CI to test the same filtered set of packages in post-submit as are
  tested in presubmit.
* Adds a `fix` command to run `dart fix --apply` in target packages.

## 0.11.0

* Renames `publish-plugin` to `publish`.
* Renames arguments to `list`:
    * `--package` now lists top-level packages (previously `--plugin`).
    * `--package-or-subpackage` now lists top-level packages (previously
      `--package`).

## 0.10.0+1

* Recognizes `run_test.sh` as a developer-only file in `version-check`.
* Adds `readme-check` validation that the example/README.md for a federated
  plugin's implementation packages has a warning about the intended use of the
  example instead of the template boilerplate.

## 0.10.0

* Improves the logic in `version-check` to determine what changes don't require
  version changes, as well as making any dev-only changes also not require
  changelog changes since in practice we almost always override the check in
  that case.
* Removes special-case handling of Dependabot PRs, and the (fragile)
  `--change-description-file` flag was only still used for that case, as
  the improved diff analysis now handles that case more robustly.

## 0.9.3

* Raises minimum `compileSdkVersion` to 32 for the `all-plugins-app` command.

## 0.9.2

* Adds checking of `code-excerpt` configuration to `readme-check`, to validate
  that if the excerpting tags are added to a README they are actually being
  used.

## 0.9.1

* Adds a `--downgrade` flag to `analyze` for analyzing with the oldest possible
  versions of packages.

## 0.9.0

* Replaces PR-description-based version/changelog/breaking change check
  overrides in `version-check` with label-based overrides using a new
  `pr-labels` flag, since we don't actually have reliable access to the
  PR description in checks.

## 0.8.10

- Adds a new `remove-dev-dependencies` command to remove `dev_dependencies`
  entries to make legacy version analysis possible in more cases.
- Adds a `--lib-only` option to `analyze` to allow only analyzing the client
  parts of a library for legacy verison compatibility.

## 0.8.9

- Includes `dev_dependencies` when overridding dependencies using
  `make-deps-path-based`.
- Bypasses version and CHANGELOG checks for Dependabot PRs for packages
  that are known not to be client-affecting.

## 0.8.8

- Allows pre-release versions in `version-check`.

## 0.8.7

- Supports empty custom analysis allow list files.
- `drive-examples` now validates files to ensure that they don't accidentally
  use `test(...)`.
- Adds a new `dependabot-check` command to ensure complete Dependabot coverage.
- Adds `skip-if-not-supporting-dart-version` to allow for the same use cases
  as `skip-if-not-supporting-flutter-version` but for packages without Flutter
  constraints.

## 0.8.6

- Adds `update-release-info` to apply changelog and optional version changes
  across multiple packages.
- Fixes changelog validation when reverting to a `NEXT` state.
- Fixes multiplication of `--force` flag when publishing multiple packages.
- Adds minimum deployment target flags to `xcode-analyze` to allow
  enforcing deprecation warning handling in advance of actually dropping
  support for an OS version.
- Checks for template boilerplate in `readme-check`.
- `readme-check` now validates example READMEs when present.

## 0.8.5

- Updates `test` to inculde the Dart unit tests of examples, if any.
- `drive-examples` now supports non-plugin packages.
- Commands that iterate over examples now include non-Flutter example packages.

## 0.8.4

- `readme-check` now validates that there's a info tag on code blocks to
  identify (and for supported languages, syntax highlight) the language.
- `readme-check` now has a `--require-excerpts` flag to require that any Dart
  code blocks be managed by `code_excerpter`.

## 0.8.3

- Adds a new `update-excerpts` command to maintain README files using the
  `code-excerpter` package from flutter/site-shared.
- `license-check` now ignores submodules.
- Allows `make-deps-path-based` to skip packages it has alredy rewritten, so
  that running multiple times won't fail after the first time.
- Removes UWP support, since Flutter has dropped support for UWP.

## 0.8.2+1

- Adds a new `readme-check` command.
- Updates `publish-plugin` command documentation.
- Fixes `all-plugins-app` to preserve the original application's Dart SDK
  version to avoid changing language feature opt-ins that the template may
  rely on.
- Fixes `custom-test` to run `pub get` before running Dart test scripts.

## 0.8.2

- Adds a new `custom-test` command.
- Switches from deprecated `flutter packages` alias to `flutter pub`.

## 0.8.1

- Fixes an `analyze` regression in 0.8.0 with packages that have non-`example`
  sub-packages.

## 0.8.0

- Ensures that `firebase-test-lab` runs include an `integration_test` runner.
- Adds a `make-deps-path-based` command to convert inter-repo package
  dependencies to path-based dependencies.
- Adds a (hidden) `--run-on-dirty-packages` flag for use with
  `make-deps-path-based` in CI.
- `--packages` now allows using a federated plugin's package as a target without
  fully specifying it (if it is not the same as the plugin's name). E.g.,
  `--packages=path_provide_ios` now works.
- `--run-on-changed-packages` now includes only the changed packages in a
  federated plugin, not all packages in that plugin.
- Fixes `federation-safety-check` handling of plugin deletion, and of top-level
  files in unfederated plugins whose names match federated plugin heuristics
  (e.g., `packages/foo/foo_android.iml`).
- Adds an auto-retry for failed Firebase Test Lab tests as a short-term patch
  for flake issues.
- Adds support for `CHROME_EXECUTABLE` in `drive-examples` to match similar
  `flutter` behavior.
- Validates `default_package` entries in plugins.
- Removes `allow-warnings` from the `podspecs` command.
- Adds `skip-if-not-supporting-flutter-version` to allow running tests using a
  version of Flutter that not all packages support. (E.g., to allow for running
  some tests against old versions of Flutter to help avoid accidental breakage.)

## 0.7.3

- `native-test` now builds unit tests before running them on Windows and Linux,
  matching the behavior of other platforms.
- Adds `--log-timing` to add timing information to package headers in looping
  commands.
- Adds a `--check-for-missing-changes` flag to `version-check` that requires
  version updates (except for recognized exemptions) and CHANGELOG changes when
  modifying packages, unless the PR description explains why it's not needed.

## 0.7.2

- Update Firebase Testlab deprecated test device. (Pixel 4 API 29 -> Pixel 5 API 30).
- `native-test --android`, `--ios`, and `--macos` now fail plugins that don't
  have unit tests, rather than skipping them.
- Added a new `federation-safety-check` command to help catch changes to
  federated packages that have been done in such a way that they will pass in
  CI, but fail once the change is landed and published.
- `publish-check` now validates that there is an `AUTHORS` file.
- Added flags to `version-check` to allow overriding the platform interface
  major version change restriction.
- Improved error handling and error messages in CHANGELOG version checks.
- `license-check` now validates Kotlin files.
- `pubspec-check` now checks that the description is of the pub-recommended
  length.
- Fix `license-check` when run on Windows with line ending conversion enabled.
- Fixed `pubspec-check` on Windows.
- Add support for `main` as a primary branch. `master` continues to work for
  compatibility.

## 0.7.1

- Add support for `.pluginToolsConfig.yaml` in the `build-examples` command.

## 0.7.0

- `native-test` now supports `--linux` for unit tests.
- Formatting now skips Dart files that contain a line that exactly
  matches the string `// This file is hand-formatted.`.

## 0.6.0+1

- Fixed `build-examples` to work for non-plugin packages.

## 0.6.0

- Added Android native integration test support to `native-test`.
- Added a new `android-lint` command to lint Android plugin native code.
- Pubspec validation now checks for `implements` in implementation packages.
- Pubspec valitation now checks the full relative path of `repository` entries.
- `build-examples` now supports UWP plugins via a `--winuwp` flag.
- `native-test` now supports `--windows` for unit tests.
- **Breaking change**: `publish` no longer accepts `--no-tag-release` or
  `--no-push-flags`. Releases now always tag and push.
- **Breaking change**: `publish`'s `--package` flag has been replaced with the
  `--packages` flag used by most other packages.
- **Breaking change** Passing both `--run-on-changed-packages` and `--packages`
  is now an error; previously it the former would be ignored.

## 0.5.0

- `--exclude` and `--custom-analysis` now accept paths to YAML files that
  contain lists of packages to exclude, in addition to just package names,
  so that exclude lists can be maintained separately from scripts and CI
  configuration.
- Added an `xctest` flag to select specific test targets, to allow running only
  unit tests or integration tests.
- **Breaking change**: Split Xcode analysis out of `xctest` and into a new
  `xcode-analyze` command.
- Fixed a bug that caused `firebase-test-lab` to hang if it tried to run more
  than one plugin's tests in a single run.
- **Breaking change**: If `firebase-test-lab` is run on a package that supports
  Android, but for which no tests are run, it now fails instead of skipping.
  This matches `drive-examples`, as this command is what is used for driving
  Android Flutter integration tests on CI.
- **Breaking change**: Replaced `xctest` with a new `native-test` command that
  will eventually be able to run native unit and integration tests for all
  platforms.
  - Adds the ability to disable test types via `--no-unit` or
    `--no-integration`.
- **Breaking change**: Replaced `java-test` with Android unit test support for
  the new `native-test` command.
- Commands that print a run summary at the end now track and log exclusions
  similarly to skips for easier auditing.
- `version-check` now validates that `NEXT` is not present when changing
  the version.

## 0.4.1

- Improved `license-check` output.
- Use `java -version` rather than `java --version`, for compatibility with more
  versions of Java.

## 0.4.0

- Modified the output format of many commands
- **Breaking change**: `firebase-test-lab` no longer supports `*_e2e.dart`
  files, only `integration_test/*_test.dart`.
- Add a summary to the end of successful command runs for commands using the
  new output format.
- Fixed some cases where a failure in a command for a single package would
  immediately abort the test.
- Deprecated `--plugins` in favor of new `--packages`. `--plugins` continues to
  work for now, but will be removed in the future.
- Make `drive-examples` device detection robust against Flutter tool banners.
- `format` is now supported on Windows.

## 0.3.0

- Add a --build-id flag to `firebase-test-lab` instead of hard-coding the use of
  `CIRRUS_BUILD_ID`. `CIRRUS_BUILD_ID` is the default value for that flag, for backward
  compatibility.
- `xctest` now supports running macOS tests in addition to iOS
  - **Breaking change**: it now requires an `--ios` and/or `--macos` flag.
- **Breaking change**: `build-examples` for iOS now uses `--ios` rather than
  `--ipa`.
- The tooling now runs in strong null-safe mode.
- `publish plugins` check against pub.dev to determine if a release should happen.
- Modified the output format of many commands
- Removed `podspec`'s `--skip` in favor of `--ignore` using the new structure.

## 0.2.0

- Remove `xctest`'s `--skip`, which is redundant with `--ignore`.

## 0.1.4

- Add a `pubspec-check` command

## 0.1.3

- Cosmetic fix to `publish-check` output
- Add a --dart-sdk option to `analyze`
- Allow reverts in `version-check`

## 0.1.2

- Add `against-pub` flag for version-check, which allows the command to check version with pub.
- Add `machine` flag for publish-check, which replaces outputs to something parsable by machines.
- Add `skip-conformation` flag to publish-plugin to allow auto publishing.
- Change `run-on-changed-packages` to consider all packages as changed if any
  files have been changed that could affect the entire repository.

## 0.1.1

- Update the allowed third-party licenses for flutter/packages.

## 0.1.0+1

- Re-add the bin/ directory.

## 0.1.0

- **NOTE**: This is no longer intended as a general-purpose package, and is now
  supported only for flutter/plugins and flutter/tools.
- Fix version checks
  - Remove handling of pre-release null-safe versions
- Fix build all for null-safe template apps
- Improve handling of web integration tests
- Supports enforcing standardized copyright files
- Improve handling of iOS tests

## v.0.0.45+3

- Pin `collection` to `1.14.13` to be able to target Flutter stable (v1.22.6).

## v.0.0.45+2

- Make `publish-plugin` to work on non-flutter packages.

## v.0.0.45+1

- Don't call `flutter format` if there are no Dart files to format.

## v.0.0.45

- Add exclude flag to exclude any plugin from further processing.

## v.0.0.44+7

- `all-plugins-app` doesn't override the AGP version.

## v.0.0.44+6

- Fix code formatting.

## v.0.0.44+5

- Remove `-v` flag on drive-examples.

## v.0.0.44+4

- Fix bug where directory isn't passed

## v.0.0.44+3

- More verbose logging

## v.0.0.44+2

- Remove pre-alpha Windows workaround to create examples on the fly.

## v.0.0.44+1

- Print packages that passed tests in `xctest` command.
- Remove printing the whole list of simulators.

## v.0.0.44

- Add 'xctest' command to run xctests.

## v.0.0.43

- Allow minor `*-nullsafety` pre release packages.

## v.0.0.42+1

- Fix test command when `--enable-experiment` is called.

## v.0.0.42

- Allow `*-nullsafety` pre release packages.

## v.0.0.41

- Support `--enable-experiment` flag in subcommands `test`, `build-examples`, `drive-examples`,
and `firebase-test-lab`.

## v.0.0.40

- Support `integration_test/` directory for `drive-examples` command

## v.0.0.39

- Support `integration_test/` directory for `package:integration_test`

## v.0.0.38

- Add C++ and ObjC++ to clang-format.

## v.0.0.37+2

- Make `http` and `http_multi_server` dependency version constraint more flexible.

## v.0.0.37+1

- All_plugin test puts the plugin dependencies into dependency_overrides.

## v.0.0.37

- Only builds mobile example apps when necessary.

## v.0.0.36+3

- Add support for Linux plugins.

## v.0.0.36+2

- Default to showing podspec lint warnings

## v.0.0.36+1

- Serialize linting podspecs.

## v.0.0.36

- Remove retry on Firebase Test Lab's call to gcloud set.
- Remove quiet flag from Firebase Test Lab's gcloud set command.
- Allow Firebase Test Lab command to continue past gcloud set network failures.
  This is a mitigation for the network service sometimes not responding,
  but it isn't actually necessary to have a network connection for this command.

## v.0.0.35+1

- Minor cleanup to the analyze test.

## v.0.0.35

- Firebase Test Lab command generates a configurable unique path suffix for results.

## v.0.0.34

- Firebase Test Lab command now only tries to configure the project once
- Firebase Test Lab command now retries project configuration up to five times.

## v.0.0.33+1

- Fixes formatting issues that got past our CI due to
  https://github.com/flutter/flutter/issues/51585.
- Changes the default package name for testing method `createFakePubspec` back
  its previous behavior.

## v.0.0.33

- Version check command now fails on breaking changes to platform interfaces.
- Updated version check test to be more flexible.

## v.0.0.32+7

- Ensure that Firebase Test Lab tests have a unique storage bucket for each test run.

## v.0.0.32+6

- Ensure that Firebase Test Lab tests have a unique storage bucket for each package.

## v.0.0.32+5

- Remove --fail-fast and --silent from lint podspec command.

## v.0.0.32+4

- Update `publish-plugin` to use `flutter pub publish` instead of just `pub
  publish`. Enforces a `pub publish` command that matches the Dart SDK in the
  user's Flutter install.

## v.0.0.32+3

- Update Firebase Testlab deprecated test device. (Pixel 3 API 28 -> Pixel 4 API 29).

## v.0.0.32+2

- Runs pub get before building macos to avoid failures.

## v.0.0.32+1

- Default macOS example builds to false. Previously they were running whenever
  CI was itself running on macOS.

## v.0.0.32

- `analyze` now asserts that the global `analysis_options.yaml` is the only one
  by default. Individual directories can be excluded from this check with the
  new `--custom-analysis` flag.

## v.0.0.31+1

- Add --skip and --no-analyze flags to podspec command.

## v.0.0.31

- Add support for macos on `DriveExamplesCommand` and `BuildExamplesCommand`.

## v.0.0.30

- Adopt pedantic analysis options, fix firebase_test_lab_test.

## v.0.0.29

- Add a command to run pod lib lint on podspec files.

## v.0.0.28

- Increase Firebase test lab timeouts to 5 minutes.

## v.0.0.27

- Run tests with `--platform=chrome` for web plugins.

## v.0.0.26

- Add a command for publishing plugins to pub.

## v.0.0.25

- Update `DriveExamplesCommand` to use `ProcessRunner`.
- Make `DriveExamplesCommand` rely on `ProcessRunner` to determine if the test fails or not.
- Add simple tests for `DriveExamplesCommand`.

## v.0.0.24

- Gracefully handle pubspec.yaml files for new plugins.
- Additional unit testing.

## v.0.0.23

- Add a test case for transitive dependency solving in the
  `create_all_plugins_app` command.

## v.0.0.22

- Updated firebase-test-lab command with updated conventions for test locations.
- Updated firebase-test-lab to add an optional "device" argument.
- Updated version-check command to always compare refs instead of using the working copy.
- Added unit tests for the firebase-test-lab and version-check commands.
- Add ProcessRunner to mock running processes for testing.

## v.0.0.21

- Support the `--plugins` argument for federated plugins.

## v.0.0.20

- Support for finding federated plugins, where one directory contains
  multiple packages for different platform implementations.

## v.0.0.19+3

- Use `package:file` for file I/O.

## v.0.0.19+2

- Use java as language when calling `flutter create`.

## v.0.0.19+1

- Rename command for `CreateAllPluginsAppCommand`.

## v.0.0.19

- Use flutter create to build app testing plugin compilation.

## v.0.0.18+2

- Fix `.travis.yml` file name in `README.md`.

## v0.0.18+1

- Skip version check if it contains `publish_to: none`.

## v0.0.18

- Add option to exclude packages from generated pubspec command.

## v0.0.17+4

- Avoid trying to version-check pubspecs that are missing a version.

## v0.0.17+3

- version-check accounts for [pre-1.0 patch versions](https://github.com/flutter/flutter/issues/35412).

## v0.0.17+2

- Fix exception handling for version checker

## v0.0.17+1

- Fix bug where we used a flag instead of an option

## v0.0.17

- Add a command for checking the version number

## v0.0.16

- Add a command for generating `pubspec.yaml` for All Plugins app.

## v0.0.15

- Add a command for running driver tests of plugin examples.

## v0.0.14

- Check for dependencies->flutter instead of top level flutter node.

## v0.0.13

- Differentiate between Flutter and non-Flutter (but potentially Flutter consumed) Dart packages.



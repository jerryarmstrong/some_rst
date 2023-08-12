packages/go_router_builder/CHANGELOG.md
=======================================

Last edited: 2023-03-17 07:52:27

Contents:

.. code-block:: md

    ## 1.1.7

* Supports default values for `Set`, `List` and `Iterable` route parameters.

## 1.1.6

* Generates the const enum map for enums used in `List`, `Set` and `Iterable`.

## 1.1.5

* Replaces unnecessary Flutter SDK constraint with corresponding Dart
  SDK constraint.

## 1.1.4

* Fixes the example for the default values in the README.

## 1.1.3

* Updates router_config to not passing itself as `extra`.

## 1.1.2

* Adds support for Iterables, Lists and Sets in query params for TypedGoRoute. [#108437](https://github.com/flutter/flutter/issues/108437).

## 1.1.1

* Support for the generation of the pushReplacement method has been added.

## 1.1.0

* Supports default value for the route parameters.

## 1.0.16

* Update the documentation to go_router v6.0.0.
* Bumps go_router version in example folder to v6.0.0.

## 1.0.15

* Avoids using deprecated DartType.element2.

## 1.0.14

* Bumps go_router version in example folder to v5.0.0.
* Bumps flutter version to 3.3.0.

## 1.0.13

* Supports the latest `package:analyzer`.

## 1.0.12

* Adds support for enhanced enums. [#105876](https://github.com/flutter/flutter/issues/105876).

## 1.0.11

* Replace mentions of the deprecated `GoRouteData.buildPage` with `GoRouteData.buildPageWithState`.

## 1.0.10

* Adds a lint ignore for deprecated member in the example.

## 1.0.9

* Fixes lint warnings.

## 1.0.8

* Updates `analyzer` to 4.4.0.
* Removes the usage of deprecated API in `analyzer`.

## 1.0.7

* Supports newer versions of `analyzer`.

## 1.0.6

* Uses path-based deps in example.

## 1.0.5

* Update example to avoid using `push()` to push the same page since is not supported. [#105150](https://github.com/flutter/flutter/issues/105150)

## 1.0.4

* Adds `push` method to generated GoRouteData's extension. [#103025](https://github.com/flutter/flutter/issues/103025)

## 1.0.3

* Fixes incorrect separator at location path on Windows. [#102710](https://github.com/flutter/flutter/issues/102710)

## 1.0.2

* Changes the parameter name of the auto-generated `go` method from `buildContext` to `context`.

## 1.0.1

* Documentation fixes. [#102713](https://github.com/flutter/flutter/issues/102713).

## 1.0.0

* First release.



packages/camera/camera_web/CHANGELOG.md
=======================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: md

    ## NEXT

* Updates minimum Flutter version to 3.0.

## 0.3.1+1

* Updates code for stricter lint checks.

## 0.3.1

* Updates to latest camera platform interface, and fails if user attempts to use streaming with recording (since streaming is currently unsupported on web).

## 0.3.0+1

* Updates imports for `prefer_relative_imports`.
* Updates minimum Flutter version to 2.10.
* Fixes avoid_redundant_argument_values lint warnings and minor typos.
* Ignores unnecessary import warnings in preparation for [upcoming Flutter changes](https://github.com/flutter/flutter/pull/106316).

## 0.3.0

* **BREAKING CHANGE**: Renames error code `cameraPermission` to `CameraAccessDenied` to be consistent with other platforms.

## 0.2.1+6

* Minor fixes for new analysis options.

## 0.2.1+5

* Fixes library_private_types_in_public_api, sort_child_properties_last and use_key_in_widget_constructors
  lint warnings.

## 0.2.1+4

* Migrates from `ui.hash*` to `Object.hash*`.
* Updates minimum Flutter version for changes in 0.2.1+3.

## 0.2.1+3

* Internal code cleanup for stricter analysis options.

## 0.2.1+2

* Fixes cameraNotReadable error that prevented access to the camera on some Android devices when initializing a camera.
* Implemented support for new Dart SDKs with an async requestFullscreen API.

## 0.2.1+1

* Update usage documentation.

## 0.2.1

* Add video recording functionality.
* Fix cameraNotReadable error that prevented access to the camera on some Android devices.

## 0.2.0

* Initial release, adapted from the Flutter [I/O Photobooth](https://photobooth.flutter.dev/) project.



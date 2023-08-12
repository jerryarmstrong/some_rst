packages/camera/camera_platform_interface/CHANGELOG.md
======================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: md

    ## 2.4.0

* Allows camera to be switched while video recording.
* Updates minimum Flutter version to 3.0.

## 2.3.4

* Updates code for stricter lint checks.

## 2.3.3

* Updates code for stricter lint checks.

## 2.3.2

* Updates MethodChannelCamera to have startVideoRecording call the newer startVideoCapturing.

## 2.3.1

* Exports VideoCaptureOptions to allow dependencies to implement concurrent stream and record.

## 2.3.0

* Adds new capture method for a camera to allow concurrent streaming and recording.

## 2.2.2

* Updates code for `no_leading_underscores_for_local_identifiers` lint.

## 2.2.1

* Updates imports for `prefer_relative_imports`.
* Updates minimum Flutter version to 2.10.
* Fixes avoid_redundant_argument_values lint warnings and minor typos.
* Ignores unnecessary import warnings in preparation for [upcoming Flutter changes](https://github.com/flutter/flutter/pull/104231).
* Ignores missing return warnings in preparation for [upcoming analysis changes](https://github.com/flutter/flutter/issues/105750).

## 2.2.0

* Adds image streaming to the platform interface.
* Removes unnecessary imports.

## 2.1.6

* Adopts `Object.hash`.
* Removes obsolete dependency on `pedantic`.

## 2.1.5

* Fixes asynchronous exceptions handling of the `initializeCamera` method.

## 2.1.4

* Removes dependency on `meta`.

## 2.1.3

*  Update to use the `verify` method introduced in platform_plugin_interface 2.1.0.

## 2.1.2

* Adopts new analysis options and fixes all violations.

## 2.1.1

* Add web-relevant docs to platform interface code.

## 2.1.0

* Introduces interface methods for pausing and resuming the camera preview.

## 2.0.1

* Update platform_plugin_interface version requirement.

## 2.0.0

- Stable null safety release.

## 1.6.0

- Added VideoRecordedEvent to support ending a video recording in the native implementation.

## 1.5.0

- Introduces interface methods for locking and unlocking the capture orientation.
- Introduces interface method for listening to the device orientation.

## 1.4.0

- Added interface methods to support auto focus.

## 1.3.0

- Introduces an option to set the image format when initializing.

## 1.2.0

- Added interface to support automatic exposure.

## 1.1.0

- Added an optional `maxVideoDuration` parameter to the `startVideoRecording` method, which allows implementations to limit the duration of a video recording.

## 1.0.4

- Added the torch option to the FlashMode enum, which when implemented indicates the flash light should be turned on continuously.

## 1.0.3

- Update Flutter SDK constraint.

## 1.0.2

- Added interface methods to support zoom features.

## 1.0.1

- Added interface methods for setting flash mode.

## 1.0.0

- Initial open-source release



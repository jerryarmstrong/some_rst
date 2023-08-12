packages/camera/camera_android/CHANGELOG.md
===========================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: md

    ## 0.10.4

* Temporarily fixes issue with requested video profiles being null by falling back to deprecated behavior in that case.

## 0.10.3

* Adds back use of Optional type.
* Updates minimum Flutter version to 3.0.

## 0.10.2+3

* Updates code for stricter lint checks.

## 0.10.2+2

* Fixes zoom computation for virtual cameras hiding physical cameras in Android 11+.
* Removes the unused CameraZoom class from the codebase.

## 0.10.2+1

* Updates code for stricter lint checks.

## 0.10.2

* Remove usage of deprecated quiver Optional type.

## 0.10.1

* Implements an option to also stream when recording a video.

## 0.10.0+5

* Fixes `ArrayIndexOutOfBoundsException` when the permission request is interrupted.

## 0.10.0+4

* Upgrades `androidx.annotation` version to 1.5.0.

## 0.10.0+3

* Updates code for `no_leading_underscores_for_local_identifiers` lint.

## 0.10.0+2

* Removes call to `join` on the camera's background `HandlerThread`.
* Updates minimum Flutter version to 2.10.

## 0.10.0+1

* Fixes avoid_redundant_argument_values lint warnings and minor typos.

## 0.10.0

* **Breaking Change** Updates Android camera access permission error codes to be consistent with other platforms. If your app still handles the legacy `cameraPermission` exception, please update it to handle the new permission exception codes that are noted in the README.
* Ignores missing return warnings in preparation for [upcoming analysis changes](https://github.com/flutter/flutter/issues/105750).

## 0.9.8+3

* Skips duplicate calls to stop background thread and removes unnecessary closings of camera capture sessions on Android.

## 0.9.8+2

* Fixes exception in registerWith caused by the switch to an in-package method channel.

## 0.9.8+1

* Ignores deprecation warnings for upcoming styleFrom button API changes.

## 0.9.8

* Switches to internal method channel implementation.

## 0.9.7+1

* Splits from `camera` as a federated implementation.



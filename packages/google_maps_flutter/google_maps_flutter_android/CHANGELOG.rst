packages/google_maps_flutter/google_maps_flutter_android/CHANGELOG.md
=====================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: md

    ## 2.4.5

* Fixes Initial padding not working when map has not been created yet.

## 2.4.4

* Fixes Points losing precision when converting to LatLng.
* Updates minimum Flutter version to 3.0.

## 2.4.3

* Updates code for stricter lint checks.

## 2.4.2

* Updates code for stricter lint checks.

## 2.4.1

* Update `androidx.test.espresso:espresso-core` to 3.5.1.

## 2.4.0

* Adds the ability to request a specific map renderer.
* Updates code for new analysis options.

## 2.3.3

* Update android gradle plugin to 7.3.1.

## 2.3.2

* Update `com.google.android.gms:play-services-maps` to 18.1.0.

## 2.3.1

* Updates imports for `prefer_relative_imports`.

## 2.3.0

* Switches the default for `useAndroidViewSurface` to true, and adds
  information about the current mode behaviors to the README.
* Updates minimum Flutter version to 2.10.

## 2.2.0

* Updates `useAndroidViewSurface` to require Hybrid Composition, making the
  selection work again in Flutter 3.0+. Earlier versions of Flutter are
  no longer supported.
* Fixes violations of new analysis option use_named_constants.
* Fixes avoid_redundant_argument_values lint warnings and minor typos.

## 2.1.10

* Splits Android implementation out of `google_maps_flutter` as a federated
  implementation.



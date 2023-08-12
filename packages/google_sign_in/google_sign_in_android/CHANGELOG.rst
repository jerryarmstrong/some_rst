packages/google_sign_in/google_sign_in_android/CHANGELOG.md
===========================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: md

    ## 6.1.6

* Minor implementation cleanup
* Updates minimum Flutter version to 3.0.

## 6.1.5

* Updates play-services-auth version to 20.4.1.

## 6.1.4

* Rolls Guava to version 31.1.

## 6.1.3

* Updates play-services-auth version to 20.4.0.

## 6.1.2

* Fixes passing `serverClientId` via the channelled `init` call

## 6.1.1

* Corrects typos in plugin error logs and removes not actionable warnings.
* Updates minimum Flutter version to 2.10.
* Updates play-services-auth version to 20.3.0.

## 6.1.0

* Adds override for `GoogleSignIn.initWithParams` to handle new `forceCodeForRefreshToken` parameter.

## 6.0.1

* Updates gradle version to 7.2.1 on Android.

## 6.0.0

* Deprecates `clientId` and adds support for `serverClientId` instead.
  Historically `clientId` was interpreted as `serverClientId`, but only on Android. On
  other platforms it was interpreted as the OAuth `clientId` of the app. For backwards-compatibility
  `clientId` will still be used as a server client ID if `serverClientId` is not provided.
* **BREAKING CHANGES**:
  * Adds `serverClientId` parameter to `IDelegate.init` (Java).

## 5.2.8

* Suppresses `deprecation` warnings (for using Android V1 embedding).

## 5.2.7

* Fixes library_private_types_in_public_api, sort_child_properties_last and use_key_in_widget_constructors
  lint warnings.

## 5.2.6

* Switches to an internal method channel, rather than the default.

## 5.2.5

* Splits from `google_sign_in` as a federated implementation.



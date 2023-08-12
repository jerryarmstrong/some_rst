packages/google_identity_services_web/CHANGELOG.md
==================================================

Last edited: 2023-03-17 07:52:27

Contents:

.. code-block:: md

    ## 0.2.0

* Adds `renderButton` API to `id.dart`.
* **Breaking Change:** Makes JS-interop API more `dart2wasm`-friendly.
  * Removes external getters for function types
  * Introduces an external getter for the whole libraries instead.
  * Updates `README.md` with the new way of `import`ing the desired libraries.

## 0.1.1

* Add optional `scope` to `OverridableTokenClientConfig` object.
* Mark some callbacks as optional properly.

## 0.1.0

* Initial release.



src/doc/unstable-book/src/compiler-flags/extern-options.md
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    # `--extern` Options

* Tracking issue for `--extern` crate modifiers: [#98405](https://github.com/rust-lang/rust/issues/98405)
* Tracking issue for `noprelude`: [#98398](https://github.com/rust-lang/rust/issues/98398)
* Tracking issue for `priv`: [#98399](https://github.com/rust-lang/rust/issues/98399)
* Tracking issue for `nounused`: [#98400](https://github.com/rust-lang/rust/issues/98400)

The behavior of the `--extern` flag can be modified with `noprelude`, `priv` or `nounused` options.

This is unstable feature, so you have to provide `-Zunstable-options` to enable it.

## Examples

Use your own build of the `core` crate.

`rustc main.rs -Z unstable-options --extern noprelude:core=libcore.rlib`

To use multiple options, separate them with a comma:

`rustc main.rs -Z unstable-options --extern noprelude,priv,nounused:mydep=mydep.rlib`

## Options

* `noprelude`: Do not add the crate to the external prelude. If used, it will need to be imported using `extern crate`.
  This is used by the [build-std project](https://github.com/rust-lang/wg-cargo-std-aware/) to simulate compatibility with sysroot-only crates.
* `priv`: Mark the crate as a private dependency for the [`exported_private_dependencies`](../../rustc/lints/listing/warn-by-default.html#exported-private-dependencies) lint.
* `nounused`: Suppress [`unused-crate-dependencies`](../../rustc/lints/listing/allowed-by-default.html#unused-crate-dependencies) warnings for the crate.



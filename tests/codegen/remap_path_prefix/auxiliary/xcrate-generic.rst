tests/codegen/remap_path_prefix/auxiliary/xcrate-generic.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //
// compile-flags: -g  --remap-path-prefix={{cwd}}=/the/aux-cwd --remap-path-prefix={{src-base}}/remap_path_prefix/auxiliary=/the/aux-src

#![crate_type = "lib"]

pub fn foo<T>() {}



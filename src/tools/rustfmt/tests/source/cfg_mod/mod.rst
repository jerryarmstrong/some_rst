src/tools/rustfmt/tests/source/cfg_mod/mod.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg_attr(feature = "foo", path = "foo.rs")]
#[cfg_attr(not(feture = "foo"), path = "bar.rs")]
mod sub_mod;

#[cfg_attr(target_arch = "wasm32", path = "dir/dir1/dir2/wasm32.rs")]
#[cfg_attr(not(target_arch = "wasm32"), path = "dir/dir1/dir3/wasm32.rs")]
mod wasm32;

#[some_attr(path = "somewhere.rs")]
mod other;



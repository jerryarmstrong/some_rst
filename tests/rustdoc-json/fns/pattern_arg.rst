tests/rustdoc-json/fns/pattern_arg.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @is "$.index[*][?(@.name=='fst')].inner.decl.inputs[0][0]" '"(x, _)"'
pub fn fst<X, Y>((x, _): (X, Y)) -> X {
    x
}

// @is "$.index[*][?(@.name=='drop_int')].inner.decl.inputs[0][0]" '"_"'
pub fn drop_int(_: i32) {}



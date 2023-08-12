tests/ui/consts/const_fn_return_nested_fn_ptr.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// aux-build:const_fn_lib.rs

extern crate const_fn_lib;

fn main() {
    const_fn_lib::bar()();
    const_fn_lib::bar_inlined()();
    const_fn_lib::bar_inlined_always()();
}



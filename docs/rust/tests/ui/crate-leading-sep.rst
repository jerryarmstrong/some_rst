tests/ui/crate-leading-sep.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

fn main() {
    use ::std::mem;
    mem::drop(2_usize);
}



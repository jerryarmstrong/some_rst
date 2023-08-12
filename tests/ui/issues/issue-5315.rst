tests/ui/issues/issue-5315.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

struct A(#[allow(unused_tuple_struct_fields)] bool);

pub fn main() {
    let f = A;
    f(true);
}



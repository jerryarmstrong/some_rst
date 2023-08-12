tests/ui/traits/bound/multiple.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

fn f<T:PartialEq + PartialOrd>(_: T) {
}

pub fn main() {
    f(3);
}



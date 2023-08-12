tests/ui/deriving/deriving-clone-generic-tuple-struct.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

#[derive(Clone)]
#[allow(unused_tuple_struct_fields)]
struct S<T>(T, ());

pub fn main() {
    let _ = S(1, ()).clone();
}



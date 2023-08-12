tests/ui/mir/mir_void_return_2.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn nil() {}

fn mir(){
    nil()
}

pub fn main() {
    mir();
}



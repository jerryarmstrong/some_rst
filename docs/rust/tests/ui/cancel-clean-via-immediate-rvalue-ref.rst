tests/ui/cancel-clean-via-immediate-rvalue-ref.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

fn foo(x: &mut Box<u8>) {
    *x = Box::new(5);
}

pub fn main() {
    foo(&mut Box::new(4));
}



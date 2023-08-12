tests/ui/binop/binary-op-on-fn-ptr-eq.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests equality between supertype and subtype of a function
// See the issue #91636
fn foo(_a: &str) {}

fn main() {
    let x = foo as fn(&'static str);
    let _ = x == foo;
}



tests/ui/moves/move-into-dead-array-2.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Ensure that we cannot move into an uninitialized fixed-size array.

struct D { _x: u8 }

fn d() -> D { D { _x: 0 } }

fn main() {
    foo([d(), d(), d(), d()], 1);
    foo([d(), d(), d(), d()], 3);
}

fn foo(mut a: [D; 4], i: usize) {
    drop(a);
    a[i] = d(); //~ ERROR use of moved value: `a`
}



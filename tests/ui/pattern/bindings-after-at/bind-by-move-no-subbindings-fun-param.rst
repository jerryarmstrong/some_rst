tests/ui/pattern/bindings-after-at/bind-by-move-no-subbindings-fun-param.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // See issue #12534.

fn main() {}

struct A(Box<u8>);

fn f(a @ A(u): A) -> Box<u8> {
    //~^ ERROR use of partially moved value
    drop(a);
    u
}



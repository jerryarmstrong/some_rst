tests/ui/rfc-2361-dbg-macro/dbg-macro-move-semantics.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test ensuring that `dbg!(expr)` will take ownership of the argument.

#[derive(Debug)]
struct NoCopy(usize);

fn main() {
    let a = NoCopy(0);
    let _ = dbg!(a);
    let _ = dbg!(a); //~ ERROR use of moved value
}



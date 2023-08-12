tests/ui/moves/moves-based-on-type-access-to-field.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that if you move from `x.f` or `x[0]`, `x` is inaccessible.
// Also tests that we give a more specific error message.

struct Foo { f: String, y: isize }
fn consume(_s: String) {}
fn touch<A>(_a: &A) {}

fn f20() {
    let x = vec!["hi".to_string()];
    consume(x.into_iter().next().unwrap());
    touch(&x[0]); //~ ERROR borrow of moved value: `x`
}

fn main() {}



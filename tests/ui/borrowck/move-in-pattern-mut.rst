tests/ui/borrowck/move-in-pattern-mut.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #63988
#[derive(Debug)]
struct S;
fn foo(_: Option<S>) {}

enum E {
    V {
        s: S,
    }
}
fn bar(_: E) {}

fn main() {
    let s = Some(S);
    if let Some(mut x) = s {
        x = S;
    }
    foo(s); //~ ERROR use of partially moved value: `s`
    let mut e = E::V { s: S };
    let E::V { s: mut x } = e;
    x = S;
    bar(e); //~ ERROR use of partially moved value: `e`
}



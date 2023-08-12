tests/ui/pattern/usefulness/issue-2111.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(a: Option<usize>, b: Option<usize>) {
    match (a, b) {
        //~^ ERROR: non-exhaustive patterns: `(None, None)` and `(Some(_), Some(_))` not covered
        (Some(a), Some(b)) if a == b => {}
        (Some(_), None) | (None, Some(_)) => {}
    }
}

fn main() {
    foo(None, None);
}



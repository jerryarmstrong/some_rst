tests/ui/nested-ty-params.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:can't use generic parameters from outer function
fn hd<U>(v: Vec<U> ) -> U {
    fn hd1(w: [U]) -> U { return w[0]; }

    return hd1(v);
}

fn main() {}



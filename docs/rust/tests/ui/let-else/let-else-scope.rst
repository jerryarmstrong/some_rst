tests/ui/let-else/let-else-scope.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let Some(x) = Some(2) else {
        panic!("{}", x); //~ ERROR cannot find value `x` in this scope
    };
}



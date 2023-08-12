tests/ui/feature-gates/feature-gate-generators.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    yield true; //~ ERROR yield syntax is experimental
                //~^ ERROR yield expression outside of generator literal
}

#[cfg(FALSE)]
fn foo() {
    yield; //~ ERROR yield syntax is experimental
    yield 0; //~ ERROR yield syntax is experimental
}



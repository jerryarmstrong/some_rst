tests/ui/test-attrs/test-attr-non-associated-functions.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #[test] attribute is not allowed on associated functions or methods
// reworded error message
// compile-flags:--test

struct A {}

impl A {
    #[test]
    fn new() -> A {
        //~^ ERROR `#[test]` attribute is only allowed on non associated functions
        A {}
    }
    #[test]
    fn recovery_witness() -> A {
        //~^ ERROR `#[test]` attribute is only allowed on non associated functions
        A {}
    }
}

#[test]
fn test() {
    let _ = A::new();
}

fn main() {}



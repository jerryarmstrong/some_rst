tests/ui/parser/issues/issue-67377-invalid-syntax-in-enum-discriminant.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {
    use std::marker::PhantomData;

    enum Bug {
        V = [PhantomData; { [ () ].len() ].len() as isize,
        //~^ ERROR mismatched closing delimiter: `]`
        //~| ERROR mismatched closing delimiter: `]`
        //~| ERROR mismatched closing delimiter: `]`
        //~| ERROR mismatched closing delimiter: `]`
    }
}

mod b {
    enum Bug {
        V = [Vec::new; { [].len()  ].len() as isize,
        //~^ ERROR mismatched closing delimiter: `]`
        //~| ERROR mismatched closing delimiter: `]`
        //~| ERROR mismatched closing delimiter: `]`
        //~| ERROR mismatched closing delimiter: `]`
        //~| ERROR type annotations needed
    }
}

mod c {
    enum Bug {
        V = [Vec::new; { [0].len() ].len() as isize,
        //~^ ERROR mismatched closing delimiter: `]`
        //~| ERROR mismatched closing delimiter: `]`
        //~| ERROR mismatched closing delimiter: `]`
        //~| ERROR mismatched closing delimiter: `]`
        //~| ERROR type annotations needed
    }
}

fn main() {}



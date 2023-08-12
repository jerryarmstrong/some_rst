tests/ui/parser/issues/issue-70583-block-is-empty-1.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum ErrorHandled {
    Reported,
    TooGeneric,
}

impl ErrorHandled {
    pub fn assert_reported(self) {
        match self {
            ErrorHandled::Reported => {}
            ErrorHandled::TooGeneric => panic!(),
        }
    }
}

fn struct_generic(x: Vec<i32>) {
    for v in x {
        println!("{}", v);
    }
    }
} //~ ERROR unexpected closing delimiter: `}`



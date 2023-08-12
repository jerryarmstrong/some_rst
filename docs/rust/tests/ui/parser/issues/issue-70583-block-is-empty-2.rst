tests/ui/parser/issues/issue-70583-block-is-empty-2.rs
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
            ErrorHandled::Reported => {}}
                                     //^~ ERROR block is empty, you might have not meant to close it
            ErrorHandled::TooGeneric => panic!(),
        }
    }
} //~ ERROR unexpected closing delimiter: `}`



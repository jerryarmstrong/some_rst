tests/ui/inline-const/macro-with-const.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! exp {
    (const $n:expr) => {
        $n
    };
}

macro_rules! stmt {
    (exp $e:expr) => {
        $e
    };
    (exp $($t:tt)+) => {
        exp!($($t)+)
    };
}

fn main() {
    stmt!(exp const 1);
}



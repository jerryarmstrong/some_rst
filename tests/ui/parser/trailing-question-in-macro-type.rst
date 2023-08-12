tests/ui/parser/trailing-question-in-macro-type.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! fn_expr {
    ($return_type:ty : $body:expr) => {
        (|| -> $return_type { $body })()
    };
    ($body:expr) => {
        (|| $body)()
    };
}


fn main() {
    fn_expr!{ o?.when(|&i| i > 0)?.when(|&i| i%2 == 0) };
    //~^ ERROR cannot find value `o` in this scope
}



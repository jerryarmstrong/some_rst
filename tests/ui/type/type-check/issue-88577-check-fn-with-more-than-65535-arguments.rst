tests/ui/type/type-check/issue-88577-check-fn-with-more-than-65535-arguments.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! many_args {
    ([$($t:tt)*]#$($h:tt)*) => {
        many_args!{[$($t)*$($t)*]$($h)*}
    };
    ([$($t:tt)*]) => {
        fn _f($($t: ()),*) {} //~ ERROR function can not have more than 65535 arguments
    }
}

many_args!{[_]########## ######}

fn main() {}



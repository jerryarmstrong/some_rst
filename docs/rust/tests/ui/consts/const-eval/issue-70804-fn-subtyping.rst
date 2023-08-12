tests/ui/consts/const-eval/issue-70804-fn-subtyping.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

const fn nested(x: (for<'a> fn(&'a ()), String)) -> (fn(&'static ()), String) {
    x
}

pub const TEST: (fn(&'static ()), String) = nested((|_x| (), String::new()));

fn main() {}



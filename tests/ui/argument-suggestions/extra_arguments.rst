tests/ui/argument-suggestions/extra_arguments.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn empty() {}
fn one_arg(_a: i32) {}
fn two_arg_same(_a: i32, _b: i32) {}
fn two_arg_diff(_a: i32, _b: &str) {}

fn main() {
  empty(""); //~ ERROR function takes

  one_arg(1, 1); //~ ERROR function takes
  one_arg(1, ""); //~ ERROR function takes
  one_arg(1, "", 1.0); //~ ERROR function takes

  two_arg_same(1, 1, 1); //~ ERROR function takes
  two_arg_same(1, 1, 1.0); //~ ERROR function takes

  two_arg_diff(1, 1, ""); //~ ERROR function takes
  two_arg_diff(1, "", ""); //~ ERROR function takes
  two_arg_diff(1, 1, "", ""); //~ ERROR function takes
  two_arg_diff(1, "", 1, ""); //~ ERROR function takes

  // Check with weird spacing and newlines
  two_arg_same(1, 1,     ""); //~ ERROR function takes
  two_arg_diff(1, 1,     ""); //~ ERROR function takes
  two_arg_same( //~ ERROR function takes
    1,
    1,
    ""
  );

  two_arg_diff( //~ ERROR function takes
    1,
    1,
    ""
  );
}



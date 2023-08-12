tests/ui/generic-associated-types/parse/trait-path-missing-gen_arg.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X {
    type Y<'a>;
}

const _: () = {
  fn f1<'a>(arg : Box<dyn X< : 32 >>) {}
      //~^ ERROR: expected one of `>`, a const expression, lifetime, or type, found `:`
      //~| ERROR: expected parameter name, found `>`
      //~| ERROR: expected one of `!`, `)`, `+`, `,`, or `::`, found `>`
      //~| ERROR: constant provided when a type was expected
};

const _: () = {
  fn f1<'a>(arg : Box<dyn X< = 32 >>) {}
      //~^ ERROR: expected one of `>`, a const expression, lifetime, or type, found `=`
};

fn main() {}



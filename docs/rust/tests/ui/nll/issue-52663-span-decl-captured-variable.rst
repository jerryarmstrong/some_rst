tests/ui/nll/issue-52663-span-decl-captured-variable.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn expect_fn<F>(f: F) where F : Fn() {
    f();
}

fn main() {
   {
       let x = (vec![22], vec![44]);
       expect_fn(|| drop(x.0));
       //~^ ERROR cannot move out of `x.0`, as `x` is a captured variable in an `Fn` closure [E0507]
   }
}



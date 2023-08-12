tests/ui/error-codes/E0033-teach.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z teach
trait SomeTrait {
    fn foo(&self);
}
struct S;
impl SomeTrait for S {
    fn foo(&self) {}
}
fn main() {
    let trait_obj: &dyn SomeTrait = &S;

    let &invalid = trait_obj;
    //~^ ERROR E0033
}



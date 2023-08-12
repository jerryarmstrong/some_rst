tests/ui/structs-enums/enum-nullable-simplifycfg-misopt.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

/*!
 * This is a regression test for a bug in LLVM, fixed in upstream r179587,
 * where the switch instructions generated for destructuring enums
 * represented with nullable pointers could be misoptimized in some cases.
 */

enum List<X> { Nil, Cons(X, #[allow(unused_tuple_struct_fields)] Box<List<X>>) }
pub fn main() {
    match List::Cons(10, Box::new(List::Nil)) {
        List::Cons(10, _) => {}
        List::Nil => {}
        _ => panic!()
    }
}



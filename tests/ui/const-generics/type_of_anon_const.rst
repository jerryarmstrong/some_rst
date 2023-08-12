tests/ui/const-generics/type_of_anon_const.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
trait T<const A: usize> {
    fn l<const N: bool>() -> usize;
    fn r<const N: bool>() -> bool;
}

struct S;

impl<const N: usize> T<N> for S {
    fn l<const M: bool>() -> usize { N }
    fn r<const M: bool>() -> bool { M }
}

fn main() {
   assert_eq!(<S as T<123>>::l::<true>(), 123);
   assert!(<S as T<123>>::r::<true>());
}



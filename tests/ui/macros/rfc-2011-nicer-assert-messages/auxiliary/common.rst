tests/ui/macros/rfc-2011-nicer-assert-messages/auxiliary/common.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! test {
  (
    let mut $elem_ident:ident = $elem_expr:expr;
    [ $($assert:tt)* ] => $msg:literal
  ) => {
    {
      #[allow(unused_assignments, unused_mut, unused_variables)]
      let rslt = std::panic::catch_unwind(|| {
        let mut $elem_ident = $elem_expr;
        assert!($($assert)*);
      });
      let err = rslt.unwrap_err();
      if let Some(elem) = err.downcast_ref::<String>() {
        assert_eq!(elem, &$msg);
      }
      else if let Some(elem) = err.downcast_ref::<&str>() {
        assert_eq!(elem, &$msg);
      }
      else {
        panic!("assert!( ... ) should return a string");
      }
    }
  }
}



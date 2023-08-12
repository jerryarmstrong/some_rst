library/core/src/fmt/nofloat.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::fmt::{Debug, Formatter, Result};

macro_rules! floating {
    ($ty:ident) => {
        #[stable(feature = "rust1", since = "1.0.0")]
        impl Debug for $ty {
            fn fmt(&self, _fmt: &mut Formatter<'_>) -> Result {
                panic!("floating point support is turned off");
            }
        }
    };
}

floating! { f32 }
floating! { f64 }



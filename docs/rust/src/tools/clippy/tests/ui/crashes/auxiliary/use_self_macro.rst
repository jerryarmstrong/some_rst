src/tools/clippy/tests/ui/crashes/auxiliary/use_self_macro.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! use_self {
    (
        impl $ty:ident {
            fn func(&$this:ident) {
                [fields($($field:ident)*)]
            }
        }
    ) => (
        impl  $ty {
            fn func(&$this) {
                let $ty { $($field),* } = $this;
            }
        }
    )
}



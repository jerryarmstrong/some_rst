tests/ui/lint/auxiliary/unaligned_references_external_crate.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! mac {
    (
        $(#[$attrs:meta])*
        pub struct $ident:ident {
            $(
                $(#[$pin:ident])?
                $field_vis:vis $field:ident: $field_ty:ty
            ),+ $(,)?
        }
    ) => {
        $(#[$attrs])*
        pub struct $ident {
            $(
                $field_vis $field: $field_ty
            ),+
        }

        const _: () = {
            #[deny(unaligned_references)]
            fn __f(this: &$ident) {
                $(
                    let _ = &this.$field;
                )+
            }
        };
    };
}



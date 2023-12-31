library/core/src/num/shells/int_macros.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![doc(hidden)]

macro_rules! int_module {
    ($T:ident) => (int_module!($T, #[stable(feature = "rust1", since = "1.0.0")]););
    ($T:ident, #[$attr:meta]) => (
        #[doc = concat!(
            "The smallest value that can be represented by this integer type. Use ",
            "[`", stringify!($T), "::MIN", "`] instead."
        )]
        ///
        /// # Examples
        ///
        /// ```rust
        /// // deprecated way
        #[doc = concat!("let min = std::", stringify!($T), "::MIN;")]
        ///
        /// // intended way
        #[doc = concat!("let min = ", stringify!($T), "::MIN;")]
        /// ```
        ///
        #[$attr]
        #[deprecated(since = "TBD", note = "replaced by the `MIN` associated constant on this type")]
        pub const MIN: $T = $T::MIN;

        #[doc = concat!(
            "The largest value that can be represented by this integer type. Use ",
            "[`", stringify!($T), "::MAX", "`] instead."
        )]
        ///
        /// # Examples
        ///
        /// ```rust
        /// // deprecated way
        #[doc = concat!("let max = std::", stringify!($T), "::MAX;")]
        ///
        /// // intended way
        #[doc = concat!("let max = ", stringify!($T), "::MAX;")]
        /// ```
        ///
        #[$attr]
        #[deprecated(since = "TBD", note = "replaced by the `MAX` associated constant on this type")]
        pub const MAX: $T = $T::MAX;
    )
}



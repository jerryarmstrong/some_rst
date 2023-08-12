src/core/src/task/mod.rs
========================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #![stable(feature = "futures_api", since = "1.36.0")]

//! Types and Traits for working with asynchronous tasks.

mod poll;
#[stable(feature = "futures_api", since = "1.36.0")]
pub use self::poll::Poll;

mod wake;
#[stable(feature = "futures_api", since = "1.36.0")]
pub use self::wake::{Context, RawWaker, RawWakerVTable, Waker};

mod ready;
#[unstable(feature = "ready_macro", issue = "70922")]
pub use ready::ready;



tests/rustdoc/viewpath-self.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

pub mod io {
    pub trait Reader { fn dummy(&self) { } }
}

pub enum Maybe<A> {
    Just(A),
    Nothing
}

// @has foo/prelude/index.html
pub mod prelude {
    // @has foo/prelude/index.html '//code' 'pub use io;'
    // @has foo/prelude/index.html '//code' 'pub use io::Reader;'
    #[doc(no_inline)] pub use io::{self, Reader};
    // @has foo/prelude/index.html '//code' 'pub use Maybe;'
    // @has foo/prelude/index.html '//code' 'pub use Maybe::Just;'
    // @has foo/prelude/index.html '//code' 'pub use Maybe::Nothing;'
    #[doc(no_inline)] pub use Maybe::{self, Just, Nothing};
}



tests/rustdoc/intra-doc/crate-relative-assoc.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod io {
    pub trait Read {
        fn read(&mut self);
    }
}

pub mod bufreader {
    // @has crate_relative_assoc/bufreader/index.html '//a/@href' 'struct.TcpStream.html#method.read'
    //! [`crate::TcpStream::read`]
    use crate::io::Read;
}

pub struct TcpStream;

impl crate::io::Read for TcpStream {
    fn read(&mut self) {}
}



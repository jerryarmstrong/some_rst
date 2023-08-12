tests/pretty/import-renames.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type=lib

// pp-exact

use std::io::{self, Error as IoError};
use std::net::{self as stdnet, TcpStream};



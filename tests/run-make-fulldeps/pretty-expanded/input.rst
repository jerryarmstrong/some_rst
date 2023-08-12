tests/run-make-fulldeps/pretty-expanded/input.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[crate_type="lib"]

// #13544

extern crate rustc_serialize;

#[derive(RustcEncodable)] pub struct A;
#[derive(RustcEncodable)] pub struct B(isize);
#[derive(RustcEncodable)] pub struct C { x: isize }
#[derive(RustcEncodable)] pub enum D {}
#[derive(RustcEncodable)] pub enum E { y }
#[derive(RustcEncodable)] pub enum F { z(isize) }


